

## 🎛️ 코드 스플리팅(Code Splitting)

## 스플리팅 발단

리액트 어플리케이션의 경우 **빌드를 통해서 배포**한다. 이 과정에서 **파일 크기를 가능하면 최소화**하는 것이 바람직하다.

왜냐하면 파일 크기가 성능을 결정하고 결과적으로 **사용자 경험**에까지 영향을 미치기 때문이다.

또한 브라우저에서 `JSX`나 최신 자바스크립트 문법 등이 문제없이 잘 실행될 수 있도록 **트랜스파일링**하는 작업도 해주어야 한다.

> 💡 일반적으로 이러한 작업은 `웹팩(webpack)`에서 담당한다.
> 따로 웹팩을 설정해주지 않으면 프로젝트의 모든 자바스크립트 파일은 하나의 파일로 합쳐지고, CSS 역시 하나의 파일로 합쳐지게 된다.
>
> 하나의 파일로 모든 자바스크립트를 묶어서 빌드하면 파일의 크기가 매우 크고, 한 줄의 자바스크립트 코드만 수정해도 다시 모든 자바스크립트 코드들을 새로 빌드해야 하기 때문에 비효율성을 가지게 된다.

## 코드 스플리팅

------

### 파일을 분리하는 작업

**❗더 나은 사용자 경험을 위해 코드를 비동기적으로 로딩하는 방법**

예를 들어 페이지가 `/main`, `/about`, `/post` 이렇게 세 가지 페이지로 이루어진 `SPA`를 개발한다고 할 때

`/main`으로 들어가는 동안 `/about`이나 `/post` 페이지 정보는 사용자에게 필요하지 않을 확률이 높다.

> 💡 그러한 파일들을 분리하여 지금 사용자에게 필요한 파일만 불러올 수가 있다면 로딩도 빠르게 이루어지고 트래픽도 줄어 사용자 경험이 좋아질 수가 있다.
>
> 지금 당장 필요한 코드가 아니면 따로 분리시켜서, 나중에 필요할 때 불러와서 사용할 수 있다.

## 리액트에서 코드 스플리팅

------

### `React.lazy`

> 💡 컴포넌트를 렌더링하는 시점에 비동기적으로 로딩할 수 있게 해주는 유틸 함수이다.

### `Suspense`

> 💡 리액트 내장 컴포넌트로 코드 스플리팅 된 컴포넌트를 로딩하고, 로딩이 끝나지 않았을 때 보여줄 UI를 설정할 수 있다.
>
> `fallback`이라는 `props`를 통해 로딩 중에 보여줄 `JSX` 문법을 지정할 수 있다.

### `React.lazy` + `Suspense`

```tsx
import React, { Suspense } from 'react';

const SomeComponent = React.lazy(() => import('./SomeComponent'));

const myComponent = {
	return (
		<Suspense fallback={<div>Loading...</div>}>
			<SomeComponent />
		</Suspense>
	)
}
```

### 만약 `React.lazy`를 쓰지 않고 스플리팅을 해야 한다면? 🙄

16.6버전 이전에 했던 방식으로 분리할 컴포넌트를 `state`에 선언하여 해당 모듈을 불러와야할 때 `state`를 바꾸어 주는 식으로 진행한다.

## 코드 분할을 결정하는 요소

------

그 중 가장 많이 쓰이는 방법 중 하나는 라우트 기반 분할이다.

1. **Route level**

```tsx
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

const Home = lazy(() => import('./routes/Home'));
const About = lazy(() => import('./routes/About'));

const App = () => (
  <Router>
    <Suspense fallback={<div>Loading...</div>}>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route path="/about" component={About}/>
      </Switch>
    </Suspense>
  </Router>
);
```

> 💡 라우트마다 다른 컴포넌트로 관리를 하고 있을 경우, 각 라우트를 `import` 함수를 통해 분리된 빌드 파일로 관리 할 수 있다.
>
> 유저가 다른 페이지로 넘어갈때만 그 페이지를 비동기적으로 로딩할 수 있다.

1. Component level

   > 💡 페이지 안에 있지만 보이지 않는 컴포넌트가 존재할 수 있다.
   >
   > 예를 들어 유저가 이메일 페이지에서 새로운 메일을 작성하고자 할 때, 작성하기 버튼을 눌러 모달이 뜨게 된다면 그 모달을 `import()`로 스플리팅해서 관리할 수 있다.

**모달 대신 `alert` 함수 스플리팅하기**

```tsx
Notify.tsx
const Notify = () => {
	window.alert('notify!');
};

export default Notify;
App.tsx
import React, {useState} from 'react';
import {TextField, Box, Button} from '@mui/material';

const App = () => {
	const handleNotify = () => {
			import('./Notify').then(({default: Notify}) => {
				Notify();
			});
		};

	return (
		<Button variant='contained' onClick={handleNotify}>
			추가
		</Button>
	)
}

export default App
```

> 💡 `Button`을 눌렀을 때 `example.chunk.js`라는 파일을 불러오게 된다.
>
> `import` 함수를 사용하면 웹팩이 알아서 코드를 분리해서 저장해주고, `import`가 호출할 때 불러와서 사용할 수 있게 해준다.

**❗여기서는 함수 level을 스플리팅했다.**


`**chuck` 파일 생성 차이**

**스플리팅 전**
![img](https://velog.velcdn.com/cloudflare/s_sangs/f6bbd597-356b-4565-b5a4-d29d8411739d/22.PNG)

**스플리팅 후**
![img](https://velog.velcdn.com/cloudflare/s_sangs/8c9997f2-6086-42b8-882c-c82907d22388/11.PNG)

1. 하나의 페이지를 스플리팅하기

   > 💡 페이지 하나가 되게 긴 경우,
   > 그 페이지에 들어갈 때 당장 보이는 부분을 나머지와 분리하고 그 뒷부분을 다른 컴포넌트로 만들어 스플리팅할 수 있다.

## Webpack: Entry Point

------

`Entry Point`는 웹팩이 앱에서 번들링하려는 모듈의 진입파일이다.

리액트 앱이 여러 엔트리 포인트를 설정한다면 각각의 엔트리 포인트 마다 코드 스플리팅이 가능하다.

```tsx
// webpack.config.js
const path = require('path');

module.exports = {
  mode: 'development',
  entry: {
    index: './src/index.js',
    another: './src/another-module.js',
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};
```

> 💡 `entry` 프로퍼티를 작성하면 웹팩에서 자동으로 `index`와 `another`를 다른 `chunk`로 관리를 해서 로딩한다.
> 웹팩은 둘 간의 의존성(dependency)도 분리를 해서 관리를 하는데, 만약 같은 의존성을 여러 `entry point`에서 가지고 있다면, 중복된 로딩이 많아져서 성능 저하를 일으킬 수 있다.
> 중복 되는 `dependencies`는 다른 `chunk`로 관리해주는 것이 바람직하다.



<br>

<br>

#### 참고링크: [[React\] 코드 스플리팅 (Code Splitting) (velog.io)](https://velog.io/@s_sangs/코드-스플리팅-Code-Splitting)

<br>



------



## 리액트에서 코드 스플리팅

## **1. 코드 스플리팅 code splitting**

코드 스플리팅이 무엇인지에 대해서 먼저 알아보겠습니다. 리액트 카테고리에 집어넣긴 했지만, 웹팩(webpack)을 이용한 다른 어플리케이션에서도 모두 사용 가능한 언어입니다. 웹팩도 간단히 설명하자면, 어플리케이션의 모든 파일들을 묶고 압축하여 하나의 결과물을 만들어주는 웹 개발 도구입니다.

자바스크립트로 개발을 하고 배포하는 과정에서 빌드(build) 과정을 거치게 되는데, 이 과정에서 모든 파일들이 하나로 합쳐지게 됩니다. 우리가 index.js, components들로 나눴던 소스 코드들이 하나의 거대한 소스 코드로 합쳐진다는 말입니다. 간단한 프로젝트라면 영향이 적겠지만, 거대한 프로젝트라면(특히 SPA 페이지에서) 길고 많은 자바스크립트 코드(.css, .html도 마찬가지)가 탄생합니다. 이 경우 인터넷 환경이 좋지 못한 곳에서는 거대한 소스 코드들을 불러오는데 상당한 로딩시간을 갖게 됩니다. 이를 개선하고자 코드에서 당장 사용하는 부분만을 로딩하고, 현재 필요하지 않은 코드 부분은 따로 분리시켜 나중에 로드함으로써 로딩시간을 개선하는 것이 코드 스플리팅입니다.

실습을 위해 새로운 프로젝트를 create react-app으로 만들었습니다. 기본적으로 아래와 같은 파일 구조가 생성됩니다.



![img](https://blog.kakaocdn.net/dn/yefHh/btrspJygCtO/K75sKU6KuKGIj4sZVELkTK/img.png)



여기서 build를 위한 명령어 yarn build를 입력해보겠습니다. 기다리면 빌드가 완료되고, 프로젝트에 build라는 폴더가 하나 생깁니다.

```
yarn build
```



![img](https://blog.kakaocdn.net/dn/D55Kn/btrsxfWrLBJ/kSQhGqOUOmjHyivOUmkn9K/img.png)



이 폴더 내부에는 다음과 같은 16진수로된 파일명을 가진 해시 값이 적혀있습니다. 



![img](https://blog.kakaocdn.net/dn/ciqCwL/btrstXB4NWi/HDOC6Ja37e0XDUdlsXiKf1/img.png)



App.js를 아무렇게나 수정하고 다시 빌드하면 main이라고 적힌 부분의 파일명이 변경되었습니다. 즉, App.js처럼 많이 사용되고 변경되는 부분은 main으로 그 외 부분은 787.~파일로 들어가서 파일이 분리되고, 필요한 경우 787.~부분을 로딩해서 사용하는 식으로 이용하는데, 이것을 코드 스플리팅이라고 합니다.



![img](https://blog.kakaocdn.net/dn/KHbDv/btrsxFnbDfN/xKknbVJJnkmKqGMZaiTPi1/img.png)



리액트 코드 스플리팅에는 여러 방법들이 존재하고 있지만, 이번에는 세가지 방식만 알아보도록 하겠습니다.

 

 

## **2. 코드 비동기 로딩**

첫 번째 방법은 코드 비동기 로딩입니다. 이 방식은 필요한 부분에서 파일을 import함으로써 필요한 순간에 코드를 불러오게 합니다. 즉, import를 함수형으로 사용하는 문법인데, dynamic import(동적 import)라고 부릅니다. 정식 문법인가 하고 확인해봤는데, ES2022, import 구문 문서에 아직 등재되지 않은걸로 보아 정식 문법으로 채택되지는 않은 상태인 것 같습니다.

다음과 같은 분리된 코드의 함수를 준비해주세요.

```js
export default function notify() {
    alert('code-splitting');
}
```

다음으로는 App.js를 수정해주세요. code-splitting이라는 글자(p 태그)를 글릭하면 onClick 함수가 실행되고, onClick은 notify() 함수를 불러오는 역할을 합니다. 그런데 이렇게 작성하면, 이미 notify()가 선언되어 있어서, 누르기 전에도 notify() 함수 코드가 로드되어있는 상태입니다. 이런 상태가 사용하지 않는데 코드를 불러온 불필요한 사례입니다.

```js
import logo from './logo.svg';
import './App.css';
import notify from './notify';

function App() {
    const onClick = () => {
        notify();
    };

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>
                <p onClick={onClick}>code-splitting</p>
            </header>
        </div>
    );
}

export default App;
```

 

그럼 이제 코드를 비동기적으로 로드해보겠습니다. 동적 import의 사용법은 import를 함수처럼 사용합니다. 함수 처럼 사용한 import 구문은 **[Promise](https://bamtory29.tistory.com/entry/Javascript-프로미스promise-객체)**를 반환합니다. 코드를 다음과 같이 수정하고 어플리케이션을 실행해주세요. 그리고 개발자도구의 네트워크 탭을 열고 어떻게 동작하는지 살펴보세요.

```js
import logo from './logo.svg';
import './App.css';

function App() {
    const onClick = () => {
        import('./notify').then(result => result.default());
    };

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>
                <p onClick={onClick}>code-splitting</p>
            </header>
        </div>
    );
}

export default App;
```



![img](https://blog.kakaocdn.net/dn/bR5FEA/btrsvdkLoEs/S0dQ18H4fReOnEdeGbYtTK/img.png)![img](https://blog.kakaocdn.net/dn/YNOLc/btrsrlYoc8B/k0md6jlLbjkq99IC3Qi2k1/img.png)

왼쪽은 클릭 전, 오른쪽은 클릭 후



처음에 main만 불러왔던 것이 클릭을 하니 또 다른 코드를 불러왔습니다. 이렇게 동적 import를 통해서 필요할 때만 코드를 불러올 수 있습니다. 그리고 다시 build를 하면 notify와 관련된 새로운 코드가 들어있음을 볼 수 있습니다.



![img](https://blog.kakaocdn.net/dn/LJELo/btrsvdkPACE/cApfceEECHRH6qGNruUm71/img.png)



 

 

 

## **3. React.Lazy, Suspense를 사용한 코드 스플리팅**

React.Lazy와 Suspense는 리액트 V16.6부터 추가된 기능입니다. 기존 버전에서는 동적 import를 통해 불러오고 컴포넌트를 state에 넣어서 구현했다고 합니다.

우선 기존 방식부터 알아보겠습니다. SplitMe.js라는 컴포넌트를 하나 만들어주세요.

```react
import React from 'react';

const SplitMe = () => {
    return (
        <div>SplitMe</div>
    );
};

export default SplitMe;
```

App.js도 수정해주세요. App에서는 handClick이라는 메소드에서 동적 import로 SplitMe 컴포넌트를 불러옵니다. 그리고 불러온 컴포넌트를 state에 넣어줍니다. 그리고 불러온 컴포넌트는 render에서 렌더링 해줍니다.

```react
import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react';

class App extends Component {
    state = {
        SplitMe: null,
    };

    handClick = async () => {
        const loadedModule = await import('./SplitMe');

        this.setState({
            SplitMe: loadedModule.default,
        });
    };

    render() {
        const {SplitMe} = this.state;

        return (
            <div className={"App"}>
                <header className={"App-header"}>
                    <img src={logo} className={"App-logo"} alt={"logo"}/>
                    <p onClick={this.handClick}>code splitting</p>
                    {SplitMe && <SplitMe/>}
                </header>
            </div>
        );
    }
}

export default App;
```



![img](https://blog.kakaocdn.net/dn/U8WFN/btrspKEa7O1/8eAKgWaQ0WwOIpySIgONh0/img.png)![img](https://blog.kakaocdn.net/dn/HupDI/btrsrmiLGhz/wr4mCBBkFnvKI8LiYEZLm1/img.png)



실행했을때 다음과 같이 코드 스플리팅이 잘 이루어졌음을 확인할 수 있습니다. 이 방식이 V16.6이전의 코드 스플리팅 방법이었습니다. state를 매번 선언하는 과정이 번거로울 수 있습니다.

------

자 그럼 V16.6에서 추가된 React.lazy와 Suspense를 사용해서 코드 스플리팅을 구현해보도록 하겠습니다. 이 두 기능의 역할은 기존 방식에서 state를 매번 선언해야하는 번거로움을 없애준 역할입니다.

React.lazy부터 소개하자면, React.lazy는 컴포넌트를 렌더링 할 때 비동기적으로 로딩하게 해주는 함수입니다. 다음과 같이 사용합니다.

```react
React.lazy(() => 컴포넌트);
```

Suspense는 코드 스플리팅되어 로딩되지 않은 컴포넌트를 로딩하게 만들어주는 컴포넌트입니다.. 또 옵션으로 로딩이 끝나지 않았을 때 보여줄 ui를 따로 구성할 수도 있습니다. Suspense는 다음과 같이 사용합니다.

fallback은 로딩중 일 때 보여줄 ui의 코드를 넣는 공간입니다. Suspense 컴포넌트 사이에 로딩하고자 하는 컴포넌트를 삽입하면 됩니다.

```react
import React, {Suspense} from 'react';

<Suspense fallback={fallback 코드}>
</Suspense>
```

 

이제, 두 기능의 사용법을 익혔으니 방금 전에 작성한 코드를 React.lazy와 Suspense를 이용한 코드로 변경해보겠습니다.

```react
import logo from './logo.svg';
import './App.css';
import React, {useState, Suspense} from 'react';

const SplitMe = React.lazy(() => import('./SplitMe'));

const App = () => {
    const [visible, setVisible] = useState(false);
    const onClick = () => {
        setVisible(true);
    };

    return (
        <div className={"App"}>
            <header className={"App-header"}>
                <img src={logo} className={"App-logo"} alt={"logo"}/>
                <p onClick={onClick}>code splitting</p>
                <Suspense fallback={<div>로딩중...</div>}>
                    {visible && <SplitMe/>}
                </Suspense>
            </header>
        </div>
    );
}

export default App;
```

이제 실행해봅시다. 제대로 스플리팅이 되었나요?



![img](https://blog.kakaocdn.net/dn/sKUBB/btrsvdkRZzH/IKToLhJaK38Kyt1qMcXD10/img.png)![img](https://blog.kakaocdn.net/dn/7M2qZ/btrsrlKYI2Q/skP1Zr0jlkjzYT7H7i96L0/img.png)



로딩중이라는 문구도 확인해봐야겠죠? 개발자도구의 네트워크 탭의 설정에서 속도를 느리게 할 수 있습니다.



![img](https://blog.kakaocdn.net/dn/vYmB1/btrsxiFR8hb/RLKECEiqNb14ZFmqw3k2G0/img.png)



여기서 느린 3G로 설정하면 다음과 같이 로딩하면서 로딩중이라는 문구를 확인할 수 있습니다.



![img](https://blog.kakaocdn.net/dn/DTyrC/btrswVYwleX/YyNf6Yjwk5pq8h4gUkuLJK/img.png)



 

 

 

## **4. Loadable Components 라이브러리**

마지막으로 소개할 방식은 Loadable Components 라이브러리입니다. 이 라이브러리는 코드 스플리팅을 편하게 도와주는 동시에 서버 사이드 렌더링이 가능하게 해줍니다. 리액트의 공식 문서에서도 서버 사이드 렌더링을 할 경우 이 라이브러리를 사용하도록 권고하고 있습니다.

서버 사이드 렌더링은 추후에 다룰예정이니 지금은 간략하게만 설명하고 넘어가자면, UI를 서버에서 렌더링 하는 것을 의미합니다. 우리가 지금까지 만들었던 리액트 앱들은 클라이언트 사이드 렌더링 앱이었습니다.

우선 지금은 코드 스플리팅 방법만 소개하고, 서버 사이드 렌더링과 자세한 스플리팅은 서버 사이드 렌더링과 함께 다시 소개드리도록 하겠습니다. 먼저 라이브러리를 다운로드 해 주세요.

```
yarn add @loadable/component
```

 

사용법 자체는 React.lazy에서 Suspense가 빠진 형태와 유사합니다. 코드가 줄어서 더 간결해보입니다.

```react
import logo from './logo.svg';
import './App.css';
import React, {useState, Suspense} from 'react';
import loadable from '@loadable/component';

const SplitMe = loadable(() => import('./SplitMe'));

const App = () => {
    const [visible, setVisible] = useState(false);
    const onClick = () => {
        setVisible(true);
    };

    return (
        <div className={"App"}>
            <header className={"App-header"}>
                <img src={logo} className={"App-logo"} alt={"logo"}/>
                <p onClick={onClick}>code splitting</p>
                {visible && <SplitMe/>}
            </header>
        </div>
    );
}

export default App;
```

 

Suspense 컴포넌트의 fallback 처럼 로딩중에 보여주고 싶은 UI가 있다면 loadable을 다음과 같이 사용해줍니다.

```react
//변경 전
const SplitMe = loadable(() => import('./SplitMe'));

//변경 후
const SplitMe = loadable(() => import('./SplitMe'), {
  fallback: <div>로딩중...</div>
});
```

 

마지막으로 더 좋은 UX를 제공하는 preload방식도 알아보겠습니다. 여태까진 클릭을 하면 로딩이 시작되었는데, 이 방식은 클릭 하기 전에 컴포넌트에 마우스 커서가 올라가는 순간부터 로딩이 시작됩니다. 말로만 하면 복잡해보이지만, 마우스 오버 이벤트를 등록해주면 됩니다.

```react
import logo from './logo.svg';
import './App.css';
import React, {useState, Suspense} from 'react';
import loadable from '@loadable/component';

const SplitMe = loadable(() => import('./SplitMe'));

const App = () => {
    const [visible, setVisible] = useState(false);
    const onClick = () => {
        setVisible(true);
    };
    const onMouseOver = () => {
        SplitMe.preload();
    };

    return (
        <div className={"App"}>
            <header className={"App-header"}>
                <img src={logo} className={"App-logo"} alt={"logo"}/>
                <p onClick={onClick} onMouseOver={onMouseOver}>code splitting</p>
                {visible && <SplitMe/>}
            </header>
        </div>
    );
}

export default App;
```

------

이렇게 프론트엔드에서 가장 중요한 UI/UX를 개선시켜주는 리액트의 코드 스플리팅 방법을 알아보았습니다.

※ 이번 포스트는 Velopert님의 '리액트를 다루는 기술 개정판' 19장 코드 스플리팅 부분을 대거 참고하여 작성하였습니다.

### **참조**

https://velog.io/@velopert/react-code-splitting

https://devowen.com/342



<br>

<br>

#### 참고링크: [[React\] 리액트에서 코드 스플리팅 (tistory.com)](https://bamtory29.tistory.com/entry/React-리액트에서-코드-스플리팅)

<br>