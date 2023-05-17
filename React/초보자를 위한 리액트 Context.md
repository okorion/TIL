## 🗂️ 초보자를 위한 리액트 Context



**Original article:** [React Context for Beginners – The Complete Guide (2021)](https://www.freecodecamp.org/news/react-context-for-beginners/)

#### 리액트 context는 모든 리액트 개발자들이 필수적으로 알아야 하는 개념입니다. context는 앱에서 state를 쉽게 공유할 수 있게 해줍니다.

이 글에서는 리액트 context가 무엇인지, 어떻게 사용하는지, 언제 사용하고 사용해서는 안 되는지 등에 대해서 알아보도록 하겠습니다.

리액트 context를 다뤄본 적이 없어도 괜찮습니다. 쉬운 단계별 예시를 통해 필요한 모든 내용을 알게 될 것입니다.

그럼 시작해 봅시다!

> 리액트를 처음부터 끝까지 배울 수 있는 가이드가 필요하시다면 [The React Bootcamp](https://reactbootcamp.com/)를 확인하세요.

## 목차

- [리액트 context란](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/#what-is-react-context)
- [리액트 context를 사용해야 할 때](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/#when-should-you-use-react-context)
- [리액트 context가 해결해주는 문제](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/#what-problems-does-react-context-solve)
- [리액트 context 사용 방법](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/#how-do-I-use-react-context)
- [useContext 훅이란](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/#what-is-the-useContext-hook)
- [context가 필요 없을 때](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/#you-may-not-need-context)
- [리액트 context가 리덕스를 대체하는가](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/#does-react-context-replace-redux)
- [리액트 context 사용 시 주의사항](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/#react-context-caveats)

## 

### 리액트 context란

리액트 context는 앱에서 컴포넌트에게 props를 사용하지 않고 필요한 데이터를 넘겨주며 사용할 수 있게 해줍니다.

*다시 말해, 리액트 context는 컴포넌트들이 데이터(state)를 더 쉽게 공유할 수 있도록 해줍니다.*

## 

### 리액트 context를 사용해야 할 때

리액트 context는 앱의 모든 컴포넌트에서 사용할 수 있는 데이터를 전달할 때 유용합니다.

**데이터 종류는 다음과 같습니다.**

- 테마 데이터 (다크 모드 혹은 라이트 모드)
- 사용자 데이터 (현재 인증된 사용자)
- 로케일 데이터 (언어 혹은 지역)

데이터는 자주 업데이트할 필요가 없는 리액트 context에 위치해야 합니다.

왜일까요? context는 전체적인 상태 관리를 위해 만들어진 시스템이 아니기 때문입니다. context는 데이터를 쉽게 사용하기 위해 만들어졌습니다.

*리액트 context는 리액트 컴포넌트를 위한 전역 변수와 같다고 생각하면 됩니다.*

## 

### 리액트 context가 해결해주는 문제

리액트 context는 props drilling을 막는 데 도움을 줍니다.

**Props drilling**이란 중첩된 여러 계층의 컴포넌트에게 props를 전달해 주는 것을 의미합니다. 해당 props를 사용하지 않는 컴포넌트들에게까지 말이죠.

props drilling의 예시를 보여드리겠습니다. 이 앱에서 모든 컴포넌트에 prop으로 전달된 theme 데이터에 접근할 수 있습니다.

하지만 보시다시피 `Header`와 같은 `App`의 직계 자식 컴포넌트 또한 props를 사용해 테마 데이터를 내려주어야 합니다.

```js
export default function App({ theme }) {
  return (
    <>
      <Header theme={theme} />
      <Main theme={theme} />
      <Sidebar theme={theme} />
      <Footer theme={theme} />
    </>
  );
}
function Header({ theme }) {
  return (
    <>
      <User theme={theme} />
      <Login theme={theme} />
      <Menu theme={theme} />
    </>
  );
}
```

*이 예제의 문제는 무엇일까요?*

문제는 `theme` prop을 사용하지 않는 많은 컴포넌트들에게까지 해당 prop을 내려주고 있다는 점입니다.

`Header` 컴포넌트는 자식 컴포넌트에게 `theme`을 내려주기만 할 뿐 직접 필요로 하지 않습니다. 다시 말해, `User`, `Login`, `Menu` 컴포넌트가 `theme` 데이터를 직접 사용하는 게 더 나을 것입니다.

이렇듯 모든 곳에 props를 사용하는 것을 우회할 수 있어 props drilling 문제를 피할 수 있는 것이 리액트 context의 장점입니다.

## 

### 리액트 context 사용 방법

context는 리액트 버전 16부터 사용 가능한 리액트 내장 API입니다.

즉, 어떤 리액트 프로젝트라도 리액트를 import하면 context를 바로 생성하고 사용할 수 있습니다.

**리액트 context를 사용하기 위한 네 단계는 다음과 같습니다.**

1. `createContext` 메서드를 사용해 context를 생성한다.
2. 생성된 context를 가지고 context provider로 컴포넌트 트리를 감싼다.
3. `value` prop을 사용해 context provider에 원하는 값을 입력한다.
4. context consumer를 통해 필요한 컴포넌트에서 그 값을 불러온다.

*조금 헷갈리나요?* 생각보다 간단합니다.

다음 예제 코드를 보면 `App`에서 context를 사용해 이름을 전달해주고 `User`라는 하위 컴포넌트에서 불러옵니다.

```js
import React from 'react';
export const UserContext = React.createContext();
export default function App() {
  return (
    <UserContext.Provider value="Reed">
      <User />
    </UserContext.Provider>
  )
}
function User() {
  return (
    <UserContext.Consumer>
      {value => <h1>{value}</h1>} 
      {/* prints: Reed */}
    </UserContext.Consumer>
  )
}
```

위의 코드를 한 줄씩 살펴봅시다.

1. `App` 컴포넌트에서 `React.createContext()`를 사용해 context를 만들고 `UserContext` 변수에 결과를 담아두었습니다. 대부분의 경우, 컴포넌트는 다른 파일에 있기 때문에 여기서와 같이 export해 사용할 것입니다. `React.createContext()`를 사용하면 `value` prop에 초깃값을 정해줄 수 있다는 점에 유의하세요.
2. `App` 컴포넌트에서 `UserContext`를 사용하고 있습니다. 정확히 말하면 `UserContext.Provider`입니다. 이렇게 만들어진 context는 컴포넌트인 `Provider`와 `Consumer`라는 두 가지 프로퍼티를 갖는 객체입니다. 앱의 모든 컴포넌트에 값을 내려주기 위해서는 Provider 컴포넌트로 감싸주어야 합니다(위 예제의 `User` 컴포넌트).
3. `UserContext.Provider`에는 컴포넌트 트리 전체에 전달해주고 싶은 값을 넣습니다. 이를 위해 `value` prop을 사용했습니다(위 예제의 Reed).
4. `User` 혹은 context에서 제공하는 값을 사용하고 싶은 컴포넌트에서는 `UserContext.Consumer`라는 consumer 컴포넌트를 사용해야 합니다. 전달된 값을 사용하기 위해서는 **render props 패턴**을 사용해야 합니다. 이는 단지 consumer 컴포넌트가 prop처럼 전달하는 함수입니다. 함수의 결괏값으로 `value`를 반환해 사용할 수 있습니다.

## 

### useContext 훅이란

위의 예시를 보면 context를 사용하기 위해 render props 패턴을 사용하는 것이 조금 이상해 보일 수 있습니다.

리액트 훅이 도입된 리액트 16.8부터는 context를 사용하는 다른 방법이 등장했습니다. 이제는 **useContext 훅**을 사용해 context를 사용할 수 있습니다.

render props를 사용하는 대신, context를 사용할 때 컴포넌트 최상단에서 `React.useContext()`에 전체 context 객체를 내려줄 수 있습니다.

useContext 훅을 사용한 예시는 다음과 같습니다.

```js
import React from 'react';
export const UserContext = React.createContext();
export default function App() {
  return (
    <UserContext.Provider value="Reed">
      <User />
    </UserContext.Provider>
  )
}
function User() {
  const value = React.useContext(UserContext);  
    
  return <h1>{value}</h1>;
}
```

*useContext 훅의 장점은 컴포넌트가 더욱 간결해지고 나만의 커스텀 훅을 만들 수 있다는 점입니다.*

선호하는 패턴에 따라서 consumer 컴포넌트를 직접 사용할 수도 있고 useContext 훅을 사용할 수도 있습니다.

## 

### context가 필요 없을 때

많은 개발자들이 하는 실수는 여러 레벨의 컴포넌트에 props를 내려줘야 하는 경우에 매번 context를 사용하는 것입니다.

여기 `App` 컴포넌트의 `username`과 `avatarSrc` 두 가지 props가 필요한 `Avatar`라는 중첩 컴포넌트가 있습니다.

```js
export default function App({ user }) {
  const { username, avatarSrc } = user;
  return (
    <main>
      <Navbar username={username} avatarSrc={avatarSrc} />
    </main>
  );
}
function Navbar({ username, avatarSrc }) {
  return (
    <nav>
      <Avatar username={username} avatarSrc={avatarSrc} />
    </nav>
  );
}
function Avatar({ username, avatarSrc }) {
  return <img src={avatarSrc} alt={username} />;
}
```

가능하다면 props가 필요 없는 컴포넌트들에게 여러 개의 props를 굳이 전달하고 싶지 않을 것입니다.

*어떻게 하면 될까요?*

prop drilling 하고 있다는 이유로 바로 context에 의지하는 것보다는 컴포넌트를 더 잘 구성함으로써 해결할 수 있습니다.

최상위 컴포넌트인 `App`만 `Avatar` 컴포넌트에 대해 알고 있으면 되기 때문에 `App` 내에 바로 avatar를 만드는 것입니다.

이렇게 하면 두 개의 props를 내려주는 것 대신 `avatar`라는 하나의 prop만 내려주면 됩니다.

```js
export default function App({ user }) {
  const { username, avatarSrc } = user;
  const avatar = <img src={avatarSrc} alt={username} />;
  return (
    <main>
      <Navbar avatar={avatar} />
    </main>
  );
}
function Navbar({ avatar }) {
  return <nav>{avatar}</nav>;
}
```

*요약하자면, 바로 context를 사용하지는 마세요. prop drilling을 피하기 위해 컴포넌트를 개선하여 설계할 수 있는지를 먼저 살펴보세요.*

## 

### 리액트 context가 리덕스를 대체하는가

맞기도 하고 틀리기도 합니다.

많은 리액트 초보자들에게 리덕스는 데이터를 더 쉽게 전달해 주는 도구로 여겨지곤 합니다. 리덕스는 리액트 context 자체와 함께 제공되기 때문입니다.

하지만 state를 *업데이트*하는 것이 아니라 컴포넌트에 전달만 해주는 경우라면 리덕스와 같은 전역 상태 관리 라이브러리는 필요하지 않을 수도 있습니다.

## 

### 리액트 context 사용 시 주의사항

*리액트 context가 내려주는 값을 업데이트하는 것은 왜 불가능할까요?*

리액트 context를 useReducer와 같은 훅과 결합해 서드파티 라이브러리 없이 임시 상태 관리 라이브러리를 생성하는 것이 가능하지만, 보통 성능상의 문제로 권장되지 않습니다.

이런 접근법은 리액트 context가 재렌더링을 초래한다는 문제가 있습니다.

만약 리액트 context provider에 객체를 내려주고 있고 그 객체의 프로퍼티가 업데이트된다면 무슨 일이 일어날까요? *그 context를 사용하고 있는 모든 컴포넌트에서 재렌더링이 일어날 것입니다.*

state가 거의 없는 작은 앱의 경우(위 예제의 theme 데이터), 이러한 성능 이슈가 일어나지 않을 것입니다. 테마 데이터처럼 업데이트가 자주 되지 않는 경우라면 말이죠. 하지만 트리의 많은 컴포넌트에서 state 변경이 자주 일어난다면 문제가 될 것입니다.

<br>

<br>

#### 참고링크: [초보자를 위한 리액트 Context - 완벽 가이드 (2021) (freecodecamp.org)](https://www.freecodecamp.org/korean/news/cobojareul-wihan-riaegteu-context-wanbyeog-gaideu-2021/)

<br>