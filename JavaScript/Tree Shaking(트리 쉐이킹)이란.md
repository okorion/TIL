## 🏝 Tree Shaking(트리 쉐이킹)이란?

![img](https://blog.kakaocdn.net/dn/lpB4r/btq082LjyWL/b0BbUxlqOA5ABFtgTdU9s1/img.jpg)



 <br>

 

최근 웹 성능 최적화 관련해서 계속해서 공부 중인데, **Tree Shaking**이라는 새로운 개념에 대해 알게 되어서 블로그로 정리해 보려고 한다.

##  <br>

## 한 줄 소개

나무를 흔들어서 죽은 나뭇잎들을 떨어뜨리듯, 코드를 빌드할 때도 실제로 쓰지 않는 코드들을 제외한다는 뜻으로 Tree Shaking이란 이름이 붙여졌다고 한다.

##  <br>

## 개념 소개

자바스크립트에서 주로 작업할 때, 여러 코드를 모듈 형식으로 파일 별로 관리하며 ES6 문법을 통해 export, import 해서 사용하게 된다.

```
import * as util from '../utilFile';
```

 <br>

위 코드를 보면, utilFile이라는 파일에 있는 모듈을 import 해서 가져오게 된다.
여기서 궁금한건, 저 utilFile 내에 얼마나 많은 모듈 코드가 있을 것이고, 우리가 저기에 포함된 모든 모듈을 사용할 것인지이다.

저 상태로 빌드를 하게 되면, uilFile의 모든 코드가 포함돼서 빌드가 되겠지만, 실제론 utilFile의 일부만 사용하게 된다면 이는 굉장히 많은 리소스를 낭비하게 되는 셈이다.

그러면 해당 모듈에서 실제로 사용하고 있는 코드만 빌드하려면 어떻게 할 수 있을까? 이럴 때 사용하는 것이 **Tree Shaking**이다

지금부터 이러한 Tree Shaking에 대해 알아보자.

 <br>

<br>

## 

## Tree Shaking 적용 방법

Tree Shaking을 적용하기 위해서는 몇 가지 조건이 있다.

####  <br>

**1. Babelrc 파일 설정**

<br>
그중 첫 번째가 '*ES6 문법을 CommonJS로 변환되지 않도록 막기*'이다.
**Babel**은 자바스크립트 문법이 브라우저에서 호환이 가능하도록 ES5 문법으로 변환하는 라이브러리이다. 이 작업을 우리는 **polyfill**이라 부르고 이는 현재 웹 개발에 있어서 필수 요소 중 하나라고 봐도 무방하다.

그러나 이 Babel의 역할은 Tree Shaking 작업을 하는 데 있어서 걸림돌이 되는 요소이다. Babel은 import를 **require()** 구문으로 변환을 시키는데, require은 export 하는 모든 모듈을 가져오게 된다.

이를 방지하기 위해 Babelrc 파일을 아래처럼 설정할 수 있다.

```
{
  “presets”: [ 
    [
      “@babel/preset-env”,
      {
	    "modules": false
      }
    ]
 ]
}
```

 <br>

babel-preset-env에 modules를 false로 하면, import, export의 구문을 ES5의 문법으로 변환시키지 않는다. 

<br>

 <br>

#### **2. 모듈 내 Side-Effect 발생 여부 확인**

Tree Shaking을 위한 두 번째 조건은 **Side-Effect**가 발생하는 요소가 있는지이다.

<br>

> Side-Effect란, 현재 모듈 외에 다른 코드에 영향을 끼치는 요소가 있으면, 이를 Side-Effect가 있다고 할 수 있다.

```
let animals = ['dog', 'cat'];

const addAnimals = (name) => {
  animals.push(name);
}
```

<br>
위 코드가 Side-Effect가 발생하고 있는 예시이다. 실제로 addAnimals() 라는 함수가 쓰이지 않아 다른 코드에 영향을 주지 않는다 해도, addAnimals() 함수 바깥의 변수를 변경하는 작업으로 인해 Side-Effect를 일으킨다고 판단하여 트리 쉐이킹을 하지 못하게 된다.

Side-Effect를 일으키지 않는 모듈은, 바깥의 변수의 값을 변경하지 않고, 모듈 내 코드로만 봤을 때 인풋 파라미터 값에 의해 아웃풋 결과값을 예측할 수 있도록 되어 있어야 Tree-Shaking 하기에 안전한 모듈이다.

<br>
그럼에도 개발자가 봤을 때, 해당 모듈이 Side-Effect를 발생시키지 않는다고 판단할 경우, Side-Effect가 일어나지 않는 모듈이라고 설정할 수 있다.

우선 **package.json**에 아래처럼 설정한다.

```
{
  "name": "webpack-tree-shaking-example",
  "version": "1.0.0",
  "sideEffects": false
}
```

여기까지만 한다면, 모든 모듈이 사이드 이펙트를 발생하지 않는다고 정의한다.

혹은 특정 파일만 사이드 이펙트를 발생하지 않는 모듈이라고 따로 선언할 수 있다.

```
{
  "name": "webpack-tree-shaking-example",
  "version": "1.0.0",
  "sideEffects": [
    "./src/utils/utils.js"
  ]
}
```

 <br>

####  <br>

#### **3. 필요한 모듈만 Import 해서 가져오기**

 

 <br>



![img](https://blog.kakaocdn.net/dn/bRxkZK/btq1dAe25sB/H70o0qtFY6ImqOPWZ0rGnk/img.png)tree shaking에 필요한 import 하는 방식



 

 <br>

마지막으로는 import 하는 모듈에서 원하는 모듈만 import 선언을 하는 것이다.

```
import { module1, module2 } from '../utilFile';
```

 <br>

위 코드에서는 uilFile 내에 일부만 import를 해서 가져온다.

대부분 이 정도면 최신 웹팩 환경에서 Tree Shaking 조건을 갖추었기 때문에 사용하지 않는 불필요한 코드를 빌드하지 않도록 Shaking 할 수 있다.

 <br>

#### **만약 Tree Shaking이 되지 않는다면?**

모든 조건을 맞췄는데, 사용하려는 외부 코드 혹은 라이브러리가 Tree Shaking이 되지 않을 때가 있다.

그럴 땐 import 해서 불러오려는 코드가 **ES6(export)**로 내보내고 있는지 확인할 필요가 있다.
만약 ES6가 아니라 **CommonJS (modules.export)**으로 내보내고 있다면, 이는 Tress Shaking을 할 수 없는 모듈인 것이다.
가장 대표적인 예시로 표준 lodash 라이브러리가 있다. 대신 **lodash-es**라는 모듈을 이용하면 Tree Shaking이 가능한 것 같다.

찾아보니 CommonJS로도 TreeShaking을 할 수 있는 플러그인이 있는 것 같은데, (예: [webpack-common-shake](https://github.com/indutny/webpack-common-shake)) 아직 완벽하지 않아 특별한 케이스 외에는 많이 사용되고 있지는 않은 것 같다.

 <br>

그럼 직접 Tree Shaking을 해보면서, 프로젝트 빌드에 얼마나 효과적인지 확인해보자.

 <br>

<br>

## 직접 실습

[ malchata/webpack-tree-shaking-exampleA simple tree shaking example app using webpack. Contribute to malchata/webpack-tree-shaking-example development by creating an account on GitHub.github.com](https://github.com/malchata/webpack-tree-shaking-example)

친절하게 해당 Repo에서 가볍게 Tree-Shaking을 실습해 볼 수 있는 코드가 공유되어 있다.

해당 Repo를 Clone 해서 다운로드를 받는다.

```
$ git clone https://github.com/malchata/webpack-tree-shaking-example.git
```

 <br>

그리고 해당 프로젝트의 Dependency를 설치 후, 한번 실행시켜본다.

```
$ npm install

$ npm start
```

 <br>

**# 실행 화면 (http://localhost:8080)**

 

<br>

![img](https://blog.kakaocdn.net/dn/dc40Lj/btq0816I8Qx/zMChgroRNlcLaF6mv7UeJ1/img.png)



 <br>

우선 실행시키면 가볍게 위와 같은 화면을 볼 수 있다.

 <br>

이제 안의 내부를 확인해보자.

**#** **src/utils/utils.js 파일**

 <br>



![img](https://blog.kakaocdn.net/dn/dIrVpU/btq08002gAG/mT6nxzHPpKlEBJqrAjYMNk/img.png)



 <br>

'*src/utils/utils.js*'파일을 먼저 확인해보면, 해당 파일에 약 1300줄이나 되는 굉장히 많은 코드가 들어가 있고, 각 함수 별로 모듈 처리가 되어 있다. 그럼 이 모듈은 어디서 쓰이고 있을까.

<br>

**# src/components****/FilterablePedalList.js 파일**



 <br>



![img](https://blog.kakaocdn.net/dn/Z4DmL/btq1aRV5yfD/2ugEkn2XnZt6hkiwKZzxK0/img.png)



 

 <br>

'*src/components**/FilterablePedalList.js*' 파일을 확인해보니 해당 파일에서 utils 모듈을 import해서 사용하고 있는 것을 알 수 있다.
utils 파일에 있는 그 많던 모듈들을 모두 불러와서 utils 변수에 담아서 사용하도록 되어 있다.
그러면 이 utils는 얼마나 많이 사용되고 있을까, 

직접 확인해보면 해당 모듈은 딱 3번밖에 불려서 사용되고 있으며, 그것도 딱 하나의 함수만 사용 중이다.. 다른 코드는 아예 사용하고 있지 않는 것이다. 

이는 확실히 사용하지 않는 불필요한 코드가 대폭 들어가 있으므로 Tree Shaking의 대상이다.

우선 이 상태로 Build를 해서 코드 사이즈를 확인해보자.

```
$ npm run build
```

 

<br>

![img](https://blog.kakaocdn.net/dn/b7JjD5/btq1be4CIEN/gwlF7y9eVSMteVhRgy2xSK/img.png)



 <br>

사용하지 않는 불필요한 코드가 포함된 상태로 Build 해서 나온 Chunk 파일의 크기는 위와 같다.

 <br>

그럼 이 코드를 Tree Shaking을 해보자.

우선 utils의 모든 모듈을 불러오던 방식을, 필요한 모듈만 불러오도록 변경한다.

 

<br>

![img](https://blog.kakaocdn.net/dn/d25svb/btq0816KnSJ/RU4Y9AtTA6BlO3oCSOePlk/img.png)



 

 

 <br>

그리고 *.babelrc* 파일에 import를 CommonJS 문법 변환을 막자.

**# .babelrc 파일**

```
{
  "presets": [
    [ "es2015", { "modules": false } ]
  ],
  "plugins": [
    ["transform-react-jsx", {"pragma": "h"}],
    "emotion"
  ]
}
```

 <br>

그리고 위에 소개한 조건 중에 Side-Effect가 발생하는지도 확인해야하지만, 해당 묘듈에는 Side-Effect가 일어나는 부분이 없으므로 생략한다.

 

 <br>

그러면 이제 다시 Build를 해서 코드 사이즈를 확인해보자.

```
$ npm run build
```

 <br>

#### **Tree Shaking 적용 후 변경된 Chunk 파일 사이즈**

 

<br>

![img](https://blog.kakaocdn.net/dn/OSNML/btq1bepZ6QZ/ltE42OY8ydjL37tQ1EwZhk/img.png)



 <br>

Build 후에 생성된 Chunk 파일의 사이즈를 확인해보니 결과는 아래와 같다..!!

<br>

**verdors.js 파일 (해당 프로젝트 실행에 필요한 공통적으로 사용되는 모듈)**
37.1 KB -> 36.9 KB

**main.js 파일** **(해당 프로젝트의 메인 모듈)**
20.8 KB -> 7.94 KB

utils 파일에서 사용되지 않는 모듈을 모두 제외되고 빌드하니 엄청나게 사이즈가 줄어든 것을 확인할 수 있다.

실제 서드파티 라이브러리를 사용할 때, 해당 라이브러리의 모든 모듈을 사용하지 않을때가 많다.
항상 특정 라이브러리를 사용하려 할때마다 needs 대비 Overflow Stack이 아닌가 걱정을 많이 했었는데, 이제 해당 라이브러리가 Tree Shaking이 가능하다면 맘 편히 사용할 수 있을 것 같다!

 <br>

정말 웹 성능 향상 방법은 생각보다 많구나... 찾을때마다 계속해서 나온다..

<br>

<br>

#### 참고링크: https://helloinyong.tistory.com/305

<br>