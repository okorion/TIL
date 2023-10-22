## 📱 Strict Mode란?

> - React.StrictMode는 애플리케이션의 잠재적인 문제를 알아내기 위한 도구이다.
> - 와 마찬가지로, 는 추가적으로 DOM을 렌더링하지 않고, **자손들에 대한 부가적인 검사와 경고를 활성화**한다.
> - StrictMode는 자손 컴포넌트의 부가적인 검사와 경고를 할 뿐이다.

```null
// index.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App /> // React.StrictMode는 하위의 모든 자손 컴포넌트에 적용된다.
  </React.StrictMode>
);
```

- StrictMode는 개발 모드에서만 활성화 되기에, 빌드가 된 후의 프로젝트에서 StrictMode는 **비활성화**된다.
- 개발을 진행하는 중 console.log()가 두 번 찍히는 이유는 **StrictMode**가 활성화되어있기 때문이다.
  🍸 다만, react 버전 17 이상에서는 Strict 모드에서도 자동으로 console.log()가 두 번찍히지 않는다.

### 🧃 잠재적인 문제의 종류로는 다음과 같은 것들이 있다.

**1. 안전하지 않은 생명주기를 사용하는 컴포넌트 발견**

- 비동기 React 애플리케이션에서 특정 생명주기 메서드들은 안전하지 않다.
- Strict 모드가 활성화되면, 안전하지 않은 생명주기 메서드를 사용하는 컴포넌트 목록이 담긴 경고 로그가 출력된다.

**2. 레거시 문자열 ref 사용에 대한 경고**

- 레거시 문자열 ref API은 여러 단점이 있고, 이러한 단점없이 **객체 ref**를 사용하는 방법이 있다.
- 따라서, Strict 모드가 활성화 되었을 때, 레거시 문자열 ref API가 사용되면 경고 로그가 출력된다.

**3. 권장되지 않는 findDOMNode 사용에 대한 경고**

- findDOMNode는 변하지 않는 단일 DOM에서만 정상적으로 작동한다.
- 리액트와 같이 렌더링이 자주 일어날 수 있는 환경에서 findDOMNode는 변경사항에 대응할 방법이 없으므로 적절하지 않다.
- ref 객체를 사용하는 방법을 대신 사용할 수 있다.

**4. 예상치 못한 부작용 검사**

🌹 React는 **렌더링 단계(변경사항 탐지)**와 **커밋 단계(실제 변경사항 반영)**로 나뉘어진다.

- 커밋 단계는 빠르게 진행되나, 렌더링 단계는 느릴 수 있다.
- 렌더링 단계의 여러 생명주기 메서드들이 여러번 호출될 수 있기에, 메모리 누수와 같은 부작용이 없는 것이 중요하다.
- Strict 모드가 모든 부작용을 자동으로 찾아줄 수는 없다.
- 하지만, 일부 함수를 이중으로 호출하여 부작용을 에측하고 문제가 되는 부분을 찾을 수 있게 돕는다.
  🥛 물론, 개발모드에서만 이중으로 호출된다.

> 이중으로 호출되는 함수는 다음과 같다.
>
> - 클래스 컴포넌트의 constructor, render 그리고 shouldComponentUpdate 메서드
> - 클래스 컴포넌트의 getDerivedStateFromProps static 메서드 함수 컴포넌트 바디
> - State updater 함수 (setState의 첫 번째 인자)
> - useState, useMemo 그리고 useReducer에 전달되는 함수
>   🌶 출처 : https://ko.reactjs.org/docs/strict-mode.html#detecting-unexpected-side-effects

**5. 레거시 context API 검사**

- 레거시 context API는 오류가 발생하기 쉽기에 Strict 모드에서 사용되면 경고 로그를 출력한다.
- 새로운 context API를 사용하는 것이 권장된다.
  🍄 새로운 context API: https://ko.reactjs.org/docs/context.html

참고 자료 : https://ko.reactjs.org/docs/strict-mode.html



<br>

<br>

#### 참고링크: [React의 StrictMode에 대해서 (velog.io)](https://velog.io/@citron03/React의-StrictMode에-대해서)

<br>