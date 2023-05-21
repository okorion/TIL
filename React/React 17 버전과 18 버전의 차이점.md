# 🗃 React 17 버전과 18 버전의 차이점

## 📌 ReactDOM.render VS createRoot

React 18에서는 기존에 사용하던 ReactDOM.render 대신 ReactDOM.createRoot가 도입되었다.

```javascript
import * as ReactDOMClient from 'react-dom/client';
ReactDOMClient.createRoot(...);
```

<br>

### 📍 Root 생성여부

#### 📝 Root 란?

React에서 Root란 렌더 트리의 가장 최상위 레벨이 되는 포인터를 말한다.

<br>

#### 📝 ReactDOM.render

React 코드를 DOM에 붙이는 역할을 한다.
18 이전 버전에서는 Root를 DOM 노드를 통해 접근하기 때문에 사용자에게 노출되지 않는다.
Root를 생성할 때 container를 넘겨주는 형태로 사용하기 때문에 container에 변경이 없더라도 계속해서 DOM에 접근해야 한다.

```javascript
import * as ReactDOM from 'react-dom';
import App from 'App';

const container = document.getElementById('app');
// 최초 렌더링 시
ReactDOM.render(<App />, container);
// 업데이트가 발생해서 다시 렌더링해도 DOM 엘리먼트를 통해 Root에 접근한다.
ReactDOM.render(<App />, container);
```

<br>

#### 📝 createRoot

18 버전부터는 Root를 생성하고 Root에서 render 함수를 호출한다.

```javascript
import * as ReactDOMClient from 'react-dom/client';
import App from 'App';

const container = document.getElementById('app');
// Root를 생성한다.
const root = ReactDOMClient.createRoot(container)
// 최초 렌더링 시
root.render(<App />);
// 업데이트가 발생했을 때, container를 다시 넘겨줄 필요가 없다.
root.render(<App />);
```

<br>

<br>

## 📌 hydration

### 📍 hydration 이란?

SSR의 경우 서버에서 정적 HTML 소스를 받아 페이지를 먼저 렌더링한다.
그 후 자바스크립트 코드가 실행되면서 동적인 엘리먼트 및 이벤트 리스너가 등록된다.

<br>

### 📍 ReactDOM.hydrate VS hydrateRoot

#### 📝 ReactDOM.hydrate

ReactDOM.render 함수는 리액트 엘리먼트를 렌더링한다.
첫 번째 인자에는 리액트 컴포넌트를 전달하는데, 기존에 이미 렌더링된 컴포넌트가 있다면 새로 렌더링하는 것이 아니라 업데이트만 해준다.

ReactDOM.hydrate 함수는 render 메소드와 비슷하지만, 렌더링은 하지 않고 이벤트 핸들러 등록 등의 hydration만 수행한다.
SSR의 경우 마크업이 이미 채워져있다면 렌더링을 다시 할 필요가 없다.
따라서 **SSR 프레임워크와 함께 React를 사용할 경우 hydrate 메소드를 사용한다.**

```javascript
import * as ReactDOM from 'react-dom';
import App from 'App';

const container = document.getElementById('app');
ReactDOM.hydrate(<App />, container);
```

<br>

#### 📝 hydrateRoot

hydrateRoot 함수는 두 번째 인자로 초기 JSX 즉,컴포넌트를 받는다.

```javascript
import * as ReactDOMClient from 'react-dom/client';
import App from 'App';

const container = document.getElementById('app');
// root를 생성하고 렌더링
const root = ReactDOMClient.hydrateRoot(container, <App />);
// render 함수는 따로 사용할 필요가 없다.
```

만약 hydration 이후에 Root를 다시 업데이트하고 싶다면, 변수로 저장한 Root를 통해 render 함수를 다시 호출할 수도 있다.

```javascript
const root = ReactDOMClient.hydrateRoot(container, <App />);
root.render(<App />);
```

<br>

<br>

## 📌 Render Callback

### 📍 ReactDOM.render

기존 ReactDOM.render에서는 컴포넌트가 렌더링된 후 실행될 콜백 함수를 넘겨준다.

```javascript
function App () {
  return (
    <div>
    	<h1> Hello World </h1>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOMClient.render(<App />, rootElement, () => console.log("rendered"));
```

<br>

### 📍 createRoot

18 버전에서 도입된 createRoot에서는 콜백이 제거되었다.
부분적으로 SSR이 도입된 경우 콜백이 실행되는 시점이 유저가 예상한 타이밍과 다를 수 있다.
이를 피하기 위해 문서에서는 `ref`를 사용하라고 소개한다.

```javascript
function App ({callback}) {
  return (
    <div ref = {callback}>
    	<h1> Hello World </h1>
    </div>
  );
}

const rootElement = document.getElementById("root");
const root = ReactDOMClient.createRoot(rootElement);
root.render(<App callback = {() => console.log("rendered")} />);
```

<참고 : [https://velog.io/@ggong/React-18%EC%97%90%EC%84%9C-ReactDOM.render-%EB%8C%80%EC%8B%A0-createRoot-%EC%93%B0%EA%B8%B0](https://velog.io/@ggong/React-18에서-ReactDOM.render-대신-createRoot-쓰기) >

<br>

<br>

#### 참고링크: [[React\] React 17 버전과 18 버전의 차이점 (velog.io)](https://velog.io/@hyerin0930/React-React-17-버전과-18-버전의-차이점)

<br>