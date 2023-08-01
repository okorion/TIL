## 🔨 만들어 가며 알아보는 React

[npm trends](https://www.npmtrends.com/)(npm에 등록된 패키지의 트렌드를 확인하고 비교할 수 있는 사이트) 기준 프런트엔드 UI 개발 라이브러리 순위는 [1.React](https://ko.reactjs.org/), [2.jQuery](https://jquery.com/), [3.Vue](https://kr.vuejs.org/)입니다



불과 몇 년 전만 하더라도 UI 개발 라이브러리는 jQuery가 가장 인기가 있었습니다. 2018년 즈음부터 React가 jQuery를 앞서기 시작했는데요*(npm trends 기준)* 왜 **jQuery에서 React로 프런트엔드 UI 개발 라이브러리의 흐름이 변경**되었는지 간단히 알아보고, **React의 기능들을 JavaScript로 직접 구현**해 보고자 합니다. 라이브러리를 직접 구현해 보는 것은 해당 라이브러리를 더 잘 이해하고 사용할 수 있게 도와주기 때문입니다.

> 이 글은 React 라이브러리에 대해 어느 정도 알고 있는 개발자를 위해 작성되었습니다.

![npm-trneds차트](https://techblog.woowahan.com/wp-content/uploads/2022/06/popular.png)

출처: [npm trends](https://www.npmtrends.com/)

## jQuery와 React를 비교하기 전 알아두면 좋은 사전 지식

웹은 [DOM(Document Object Model)](https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model/Introduction)으로 구성되어 있습니다. 그리고 이 DOM의 동적 변경을 위해서 웹은 API를 제공하는데 그것이 DOM API입니다.

문제는 이 **DOM API를 다루는 것이 매우 까다롭다**는 것인데요.

간단한 예시를 살펴보겠습니다.

DOM을 선택하는 주요 방법으로, ID 선택자를 활용하는 `getElementById`와 Class 선택자를 활용한 `getElementByClassName`이 있습니다.
둘 다 DOM을 가지고 오는 함수이지만 이 둘은 서로 다른 타입의 값을 리턴합니다.

> getElementById: HTMLElement를 상속받은 객체를 리턴합니다.

```javascript
const container = document.getElementById('container');
console.log(container);  return <div id="container"></div>
console.log(container.__proto__); return HTMLDivElement {Symbol: 'HTMLDivElement'}
console.log(container.__proto__.__proto__); return HTMLElement
console.log(container.__proto__.__proto__.__proto__); return Element
```

> getElementByClassName: HTMLCollection (live)를 리턴합니다.

```javascript
const container = document.getElementsByClassName('container');
console.log(container); return HTMLCollection [className: 'container']
console.log(container.__proto__); return HTMLCollection {Symbol: 'HTMLCollection'}
console.log(container.__proto__.__proto__); return {constructor: Object()}
console.log(container.__proto__.__proto__.__proto__); return null
```

또한 브라우저별로 DOM API와 스펙이 각각 다른데요. 위와 같은 사항들을 고려하여 웹 개발을 해야 한다면 그 복잡성으로 인해 신경 써야 할 것들이 굉장히 많을 것입니다.
따라서, 프런트엔드 UI 개발 라이브러리는 **다루기 까다로운 DOM API를 쉽게 다룰 수 있게** 만들어졌고, DOM API를 어떻게 성공적으로 잘 다룰 수 있는지가 핵심이라 볼 수 있습니다.

그나마 다행인 것은 최근 JavaScript 진영에서는 이러한 문제점을 인식하고 있다는 것인데요. 쉽게 DOM에 접근 가능하도록 메서드를 추가하고 있고, 또, 대부분의 모던 브라우저들이 ES2015 등의 표준을 따르고 있습니다. 때문에 크로스 브라우징 같은 이슈들도 크게 개선되고는 있습니다.

### 쉽고 직관적으로 DOM API를 다룰 수 있는 jQuery

jQuery는 DOM Selector API로 DOM을 선택하여 특정 이벤트가 발생하면 변화를 주는 방식으로 매우 쉽고 직관적입니다.

하지만 애초에 성능을 고려한 라이브러리는 아니었던 jQuery의 가장 큰 단점 중 하나는 **매우 느리다**는 것에 있습니다. 간단하게 P 태그를 3만 줄 추가하는 예제로 JavaScript 와 jQuery의 정량적인 속도 차이를 비교해 보았습니다.

![제이쿼리,자바스크립트성능비교](https://techblog.woowahan.com/wp-content/uploads/2022/06/performance3-scaled.jpeg)

Chrome의 **Performance** 탭으로 측정해 본 결과, **jQuery는 소요 시간이 약 1199ms, JavaScript는 48ms가 걸렸습니다.**

즉 DOM 을 선택하는 단순한 메서드 만으로도 **JavaScript가 약 25배 더 빠른 결과가 나왔습니다.** ~~(jQuery가 25배 더 느립니다)~~

이렇게 차이가 나는 이유는 JavaScript는 Call tree가 굉장히 단순하지만, jQuery의 Call tree는 굉장히 복잡합니다.

위의 예제에서도 jQuery의 Call tree가 굉장히 복잡한 것을 확인할 수 있는데요. 이유는 **여러 코드로 wrapping되어 있어, 실제 태그를 추가하기까지 상당히 많은 과정을 거치기 때문입니다.** 크로스 브라우징 등의 이슈를 해결하기 위해 기존 네이티브 코드를 수없이 많은 코드들로 wrapping해서 제공해 주다 보니, 단순한 DOM을 선택하는 기능일 뿐인데도 이렇게 많은 속도 차이가 나는 것이죠.

현대의 대규모 동적인 웹사이트는 많은 데이터를 실시간으로 처리합니다. 느린 라이브러리를 사용하는 것은 경쟁력이 떨어지는 비즈니스를 개발하는 것이고, 이는 고객의 이탈을 심화시킬 수 있습니다.

![img](https://techblog.woowahan.com/wp-content/uploads/2022/06/flash.gif)

~~하지만 이런 유저라면?~~
출처: https://zoningout.tistory.com/317

그리고, 다루어야 할 데이터가 많아질수록 더 많은 DOM을 선택해야 하기 때문에, 페이지가 복잡해질수록 코드가 기하급수적으로 늘어나게 되고 코드 관리가 힘들어지는 단점 또한 있습니다. 코드 관리가 어려워지면 디버깅, 에러 핸들링도 점차 어려워지고 유지 보수도 어렵게 됩니다.

즉 **요약하자면 jQuery는 과거에는 DOM API를 손쉽게 다룰 수 있는 썩 괜찮은 라이브러리였지만 현재는 느리며, 개발 생산성**에도 좋지 않습니다.

## 그럼 React는 어떻게 DOM API를 효과적으로 다루었을까요?

React는 **개발자에게, DOM API를 쓸 필요가 없게** 만들었습니다.

개발자는 React 문법에 맞춰 **상태(state)만 관리하면, 상태를 기준으로 DOM API는 React에서 알아서 처리하여 DOM을 렌더링합니다.**

> 상태(State) 란? 변하는 데이터

소프트웨어는 현실의 문제를 해결하기 위한 솔루션이고, 현실은, 매번 변화합니다. 이 **변하는 데이터 상태**를 개발자는 **React의 선언적인 문법**으로 관리해 주면, 나머지는 React가 알아서 처리하는 방식입니다.

그렇다면 React는 위와 같은 기능을 어떻게 구현하였는지 React의 핵심 기능 5가지(가상돔, JSX, RealDOM 렌더링, Diffing Update, Hooks)를 JavaScript로 직접 구현해 보겠습니다.

다만, 아래의 코드들은 실제 React 개발 코드와는 차이가 있습니다. 이해를 돕기 위해 많은 부분이 생략되었고, 구현 방식이 조금 다를 수 있습니다. JavaScript 레벨에서 어떤 방식으로 React 기능들을 구현할 수 있는지에 초점을 두고 봐 주세요.

## React 핵심 기능 5가지

1. 가상돔(VirtualDOM)
2. JSX(JavaScript And Xml)
3. 가상돔을 리얼돔으로 렌더링하기(VirtualDOM → RealDOM)
4. Diffing Update 적용하기
5. Hooks 구현해 보기

### 1) 가상돔(VirtualDOM)

가상돔은 **DOM의 형태를 본떠 만든 객체입니다**.

가령, 아래와 같은 태그 정보가 있다고 가정하겠습니다.

```jsx
<div id="container">
  <p>VirtualDOM</p>
</div>
```

아래와 같은 객체로 추상화합니다.

```jsx
const VirtualDOM = {
    tag: 'div',
    props: {
      id: 'container'
    },
    children: [
      {
        tag: 'p',
        props: {},
        children: ["VirtualDOM"],
      },
    ],
};
```

위와 같은 객체 형태로 데이터를 계속 추가하기 위해 createElement 함수를 만들어 줍니다.

```jsx
function createElement(tagName, props, ...children) {
  return { tagName, props, children: children.flat() }
}

const VirtualDOM2 = (
  createElement('div', { id: 'container' }, 
    createElement('p', { style: 'color: red' }, '제목 입니다'),
  )
)
```

하지만, createElement 함수로 매번, 복잡한 UI를 웹 개발자가 VirtualDOM을 생성해 줄 수는 없는 일입니다. ~~(객체 리터럴보다는 낫지만요)~~ 이 createElement를 쉽게 사용할 수 있게 해 주는 것이 바로 JSX입니다.

### 2) JSX(JavaScript And Xml)

JSX는 **개발자는 익숙한 마크업 문법으로 개발**하고, JavaScript 컴파일러인 **Babel 에서 createElement 함수로 변환(transpile)** 해 주는 역할을 합니다.

![바벨캡쳐화면](https://techblog.woowahan.com/wp-content/uploads/2022/06/babel.png)

[Babel 바로 가기](https://babeljs.io/repl#?browsers=defaults%2C not ie 11%2C not ie_mob 11&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=PQKgBAAgVgzgHmAxgJwKYEMAuqCiAbVAW1QDtMwRgAoKgHgBMBLANzEfoF4AiRAezPSMSqZFwB8VMGFoAHMYBwJwJVdYQKHjgCabAJ021gcusCbMxQA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env%2Creact%2Cstage-3&prettier=false&targets=&version=7.17.11&externalPlugins=&assumptions={})

**React 없이 JSX 사용하기**

JSX는 @babel/preset-react 플러그인에 의해 JSX를 위의 createElement 함수로 변환합니다.

React 없이 JSX를 Babel로 Transpile하려면 소스코드 주석에 `@jsx ‘함수명'`을 기입해야 합니다.

![react없이JSX사용하는이미지](https://techblog.woowahan.com/wp-content/uploads/2022/06/babelWithoutReact.png)

상단의 Babel Transpile 두 이미지 중 첫 이미지 결과물은 React.createElement, 두 번째 이미지 Transpile 결과물은 createElement로 변환된 부분이 보이시나요? 위에서 직접 만들었던 createElement 함수를 사용할 수 있다는 의미입니다. React 라이브러리를 사용하지 않으므로, React.createElement 함수로 Transpile 된다면 에러를 반환하게 됩니다. `@jsx '함수명'`을 기입해, 직접 만든 createElement 함수로 Transpile할 수 있습니다.

JSX를 사용한 마크업 형식을 통해, createElement 함수 호출을 사용하는 것보다 간단하게 가상돔을 만들 수 있게 되었습니다.

### Q. React 17 버전 이전 **함수 컴포넌트에서 반드시 React를 import해야 하는 이유**

```jsx
함수 컴포넌트에서 react를 import하지 않는다면?
// import React from 'react';

const Title = () => {
  return <p>타이틀 입니다</p>
};

export default Title;
```

함수 컴포넌트에서 React를 사용하지 않음에도, React를 import하지 않으면 `React is not defined` 에러를 만날 수 있습니다. 혹시 왜 이 에러가 반환되는지 궁금한 적은 없으셨나요?

**JSX를 transpile하려면 React.createElement 함수**를 사용해야 하는데, React를 import하지 않으면 **React 패키지에 createElement 함수를 사용**할 수가 없게 됩니다. 좀 더 정확히는 **런타임에 빌드된 코드** 안에서 React.createElement 함수를 찾을 수가 없습니다.

![babelCreateElement함수이미지](https://techblog.woowahan.com/wp-content/uploads/2022/06/babelCreateElement.png)

하지만 React 17 버전부터는 함수 컴포넌트에서 React를 import하지 않아도 에러를 반환하지 않고 잘 작동합니다. 왜일까요?

![img](https://techblog.woowahan.com/wp-content/uploads/2022/06/why-564x600.jpeg)

React 17 버전부터는, **새로운 JSX Transform** 덕분에, React를 import하지 않고도 **React 패키지 자체의 _jsxRuntime 함수**를 불러와 JSX 문법을 사용 가능하게 해 줍니다.

![jsxRunTime](https://techblog.woowahan.com/wp-content/uploads/2022/06/jsxRunTime.png)
출처: https://babeljs.io/

### 3) 가상돔을 리얼돔으로 렌더링하기

JSX를 활용해 VirtualDOM까지 생성하였습니다. 하지만 **VirtualDOM은 어디까지나 객체일 뿐입니다**.

이 **객체를 리얼돔으로 렌더링하려면 DOM API를 사용**해야 합니다.

renderRealDOM 함수로 RealDOM에 반영해 줄 DOM을 생성해 보겠습니다.

```jsx
export function createElement(tagName, props, ...children) {
  return { tagName, props, children: children.flat() }
}

const jsxDOM = <div id="container">
  <p>제목 입니다</p>
</div>

export function renderRealDOM(VirtualDOM){
  // 가장 끝 하위 요소 String 예외 처리
  if(typeof VirtualDOM === 'string'){
    return document.createTextNode(VirtualDOM)
  }

  // tag 생성
  const $Element = document.createElement(VirtualDOM.tagName);

    // 재귀 호출
  VirtualDOM.children
    .map(renderRealDOM)
    .forEach(node => $Element.appendChild(node));
  return $Element;
}
```

이 renderRealDOM 함수가 하는 일은 아래와 같습니다.

1. VirtualDOM의 tagName을 바탕으로 document.createElement API를 이용하여 **태그를 생성**해 줍니다.
2. VirtualDOM의 **자식(children) 구조가 동일하므로 재귀 호출**로 renderRealDOM 을 호출해 줍니다.
3. 각각의 **Children Node 데이터를 appendChild API로 Element를 추가**해 줍니다.
4. 가장 끝 **하위 요소 Children은 String이기 때문에**, 예외 처리를 해 주고, **createTextNode**로 TextNode를 생성해 줍니다.

> 요약하면, 재귀 호출로 DOM API를 이용해 태그를 생성해 줍니다.

### 4) Diffing Update 적용

VirtualDOM은 객체이기 때문에, 이전에 적용된 Old VirtualDOM과 New VirtualDOM을 비교해서 변경된 부분만을 손쉽게 업데이트할 수 있습니다.

![virtualDom](https://techblog.woowahan.com/wp-content/uploads/2022/06/vdom.png)
출처: https://minemanemo.tistory.com/120

Diffing Update 구현하기

쉬운 예시를 위해, 텍스트가 변경된 경우에 한해서만, Diffing Update를 구현해 보겠습니다.

```jsx
export function diffingUpdate (parent, nextNode, previousNode, parentIndex = 0) {
// Node가 string일 때 업데이트해 줍니다
  if (typeof nextNode === "string" && typeof previousNode === "string") {
    // 만약 해당 문자열이 동일하다면, replace해 줄 이유가 없습니다.
    if (nextNode === previousNode) return;
    return parent.replaceChild(
      renderRealDOM(nextNode),
      parent.childNodes[parentIndex]
    )
  }

  // nextNode와 previousNode의 모든 자식 태그를 순회하며 diffingUpdate 함수를 반복해 줍니다.
  for (const [index] of nextNode.children.entries()) {
    diffingUpdate(
      parent.childNodes[parentIndex],
      nextNode.children[index],
      previousNode.children[index],
      index
    )
  }
}
```

1. VirtualDOM 객체의 구조(tag, props, children)는 동일하기 때문에 **diffingUpdate 함수를 재귀 호출**함으로써, 모든 자식 태그를 순회합니다.
2. 함수의 인자로 부모 노드, 변경할 노드, 이전 노드, parentIndex를 받아서, **replaceChild DOM API로 변경된 부분만을 업데이트**합니다.

Chrome 디버깅 모드를 통해서 변경된 상태(State)만 업데이트되는 것을 확인할 수 있습니다.

![diffUpdate result](https://techblog.woowahan.com/wp-content/uploads/2022/06/diffUpdate.png)

비교적 용량이 큰 **RealDOM 과 업데이트된 RealDOM을 비교하여 변경된 부분을 적용시키는 것이 아닌, 비교적 용량이 작은 객체인 VirtualDom과 업데이트된 VirtualDom을 비교하여 충분히 빠르게 업데이트해 주는 것이 핵심입니다.**

아래는 React 없이 직접 만든 createElement, renderRealDOM, diffingUpdate 메서드를 활용하여, JSX로 VirtualDOM을 구현하고, renderRealDOM으로 렌더링했으며, diffingUpdate까지 적용한 코드입니다.

react.js

```javascript
export function createElement(tagName, props, ...children) {
  return { tagName, props, children: children.flat() }
}

export function renderRealDOM(VirtualDOM){
  if(typeof VirtualDOM === 'string'){
    return document.createTextNode(VirtualDOM)
  }

  const $Element = document.createElement(VirtualDOM.tagName);

  VirtualDOM.children
    .map(renderRealDOM)
    .forEach(node => $Element.appendChild(node));
  return $Element;
}

export function diffingUpdate (parent, nextNode, previousNode, parentIndex = 0) {
  if (typeof nextNode === "string" && typeof previousNode === "string") {
    if (nextNode === previousNode) return;
    return parent.replaceChild(
      renderRealDOM(nextNode),
      parent.childNodes[parentIndex]
    )
  }

  for (const [index] of nextNode.children.entries()) {
    diffingUpdate(
      parent.childNodes[parentIndex],
      nextNode.children[index],
      previousNode.children[index],
      index
    )
  }
}
```

app.js

```jsx
/* @jsx createElement */
import { createElement, renderRealDOM, diffingUpdate } from './react';

const previousState = [
  { title: '에스프레소' },
  { title: '아메리카노' },
];

const nextState = [
  { title: '에스프레소' },
  { title: '아메리카노 샷추가1' },
];

const CoffeeList = (state) => (
  <ul>
    { state.map(({ title }) => (
      <li>{ title }</li>
    )) }
    </ul>
)

const previousNode = CoffeeList(previousState);
const nextNode = CoffeeList(nextState);

const $root = document.querySelector('#root');
$root.appendChild(renderRealDOM(previousNode));

setTimeout(() => 
  diffingUpdate($root, nextNode, previousNode),
  2000
);
```

### 5) Hook 구현하기

[클래스 컴포넌트](https://ko.reactjs.org/docs/react-component.html)같은 경우, 최초로 생성되는 컴포넌트만 새롭게 인스턴스를 만들고, 컴포넌트가 삭제되기 전까지 만들어진 인스턴스를 통해 render 메서드를 이용하여 상태 변경을 감지(setState)합니다. 즉, **해당 인스턴스에서 필요한 부분만을 업데이트하여 context 상태를 계속 유지**할 수 있습니다. 하지만 [함수 컴포넌트(function componen)](https://ko.reactjs.org/docs/components-and-props.html)의 경우 props를 인자로 받아서, JSX 문법에 맞는 React Component를 반환해 주기 때문에 **함수 컴포넌트의 호출은 무조건 렌더링**을 일으킵니다. 이미 만들어진 인스턴스를 가지고 render만 호출하는 클래스 컴포넌트와는 다르게, 함수 컴포넌트는 상태가 변경될 때마다 새로운 인스턴스를 생성하기 때문입니다. 따라서 **함수 컴포넌트는 호출될 때마다 늘 동일한 상태, 초기화된 상태**만 가질 수 있었습니다.
하지만, [React 16.8](https://ko.reactjs.org/blog/2019/02/06/react-v16.8.0.html) 버전부터는 함수 컴포넌트에서도 상태(State)를 갖고 유지할 수 있는 [Hook](https://ko.reactjs.org/docs/hooks-intro.html)을 제공해 주었습니다. 즉, Hook은 함수 컴포넌트에서 상태를 정의하고 수정할 수 있는 기능입니다.
조금 더 정확히는 **함수 컴포넌트가 다시 실행되어도, 해당 함수의 상태(State) 값이 초기화되지 않고, React에 의해 사라지지 않는 것입니다.**
Hook을 사용할 때 쓰는 함수인 useState 함수를 간단히 구현해 보겠습니다.

```javascript
// 4, useState 함수 외부에 두어서 데이터를 유지(클로저)
let hookState = undefined;
export function useState (initState) {
    // 1. 초기값 설정
  if (hookState === undefined) hookState = initState;
    // 2. 상태를 수정할수 있는 메서드 제공(Hooks의 두 번째 인자)
  const setState = (nextState) => {
    hookState = nextState;
        // 상태 수정 후 렌더링
    rendering();
  }
  //3. 상태와 상태를 변경할 핸들러를 배열로 반환
  return [ hookState, setState ];
 }
```

1. 초깃값이 설정되어 있지 않을 시 초깃값을 설정합니다.
2. setState로 상태를 수정 및 수정 후에는 렌더링합니다.
3. 상태와 상태를 변경할 핸들러의 배열을을 반환하여, destructuring한 형태의 배열로 받아서 사용합니다.
4. **hookState는 useState 함수 외부에 두어, useState 호출과는 상관없이 데이터를 유지해 줍니다.**

> 정리: hookState를 useState 함수 외부에 두어, [클로저](https://developer.mozilla.org/ko/docs/Web/JavaScript/Closures)로 데이터를 유지시켜, 함수가 다시 호출되더라도 이전 상태를 기억할 수 있습니다.

### 다중 상태 관리

하지만, 위와 같은 형태는 1개 이상의 상태는 다룰 수 없습니다. 각기 다른 컴포넌트에서 setState로 hookState의 값을 수정하더라도, 수정되는 값은 동일한 hookState 변수를 바라보기 때문입니다.
![img](https://techblog.woowahan.com/wp-content/uploads/2022/06/RPReplay_Final1655281299.gif)

따라서, 1개 이상의 상태를 다루기 위해 hookState를 배열로 변경해야 합니다.

[React hooks: not magic, just arrays](https://medium.com/@ryardley/react-hooks-not-magic-just-arrays-cd4f1857236e) `(Hook은 마법이 아니며, 배열일 뿐이다)`

좀 더 덧붙이자면, **Hook은 클로저로 구현된 배열**일 뿐입니다.

![프로그래밍은마법이아니다](https://techblog.woowahan.com/wp-content/uploads/2022/06/magic2.png)

출처: [https://www.instagram.com/waterglasstoon](https://www.instagram.com/waterglasstoon/)

hookStates를 배열로 변경한 코드

```javascript
let currentIndex = 0; // Hook을 사용하는 컴포넌트의 배열 위치 값
const hookStates = []; // Hook 데이터를 보관할 배열
function useState(initialState) {
  const index = currentIndex;
  if (hookStates.length === index) {
    hookStates.push(initialState);
  }
  const setState = (newState) => {
    hookStates[index] = newState;
    rendering();
  }
  currentIndex++;
  return [ hookStates[index], setState ];
}
```

1. 각각의 함수 컴포넌트들이 useState를 호출할 때마다 **currentIndex로 해당 컴포넌트의 배열 위치 값을 관리합니다. useState를 호출하는 각각의 컴포넌트를 순서대로 currentIndex 즉, 일종의 ‘Key’로 구분**해 줍니다.
2. setState로 데이터를 수정 시, 해당 배열 내부의 값을 변경해 줍니다.
3. useState 함수가 종료되기 전 currentIndex 값을 증가시켜 다음 hookStates 배열의 Index 값을 업데이트해 줍니다.

> useState를 사용하는 컴포넌트들의 상태는 hookState 배열에 **‘순서대로’ 저장**됩니다. Hook이 [사용 규칙](https://ko.reactjs.org/docs/hooks-rules.html)이 있는 이유입니다.

Hook을 간단히 구현한 전체 코드는 아래와 같습니다.

```javascript
let currentIndex = 0; 
const hookStates = []; 
function useState(initialState) {
  const index = currentIndex;
  if (hookStates.length === index) {
    hookStates.push(initialState);
  }
  const setState = (newState) => {
    hookStates[index] = newState;
    rendering();
  }
  currentIndex++;
  return [ hookStates[index], setState ];
}

function Espresso () {
  const [espresso, setEspresso] = useState(2000);

  window.addEspresso = () => setEspresso(espresso + 2000);

  return `
    <div>
      <button onclick="addEspresso()">에스프레소 추가</button>
      <strong>금액: ${espresso} </strong>
    </div>
  `;
}

function Americano () {
  const [americano, setAmericano] = useState(3000);

  window.addAmericano = () => setAmericano(americano + 3000);

  return `
    <div>
      <button onclick="addAmericano()">아메리카노 추가</button>
      <strong>금액: ${americano}</strong>
    </div>
  `;
}

const rendering = () => {
  const $root = document.querySelector('#root');
  $root.innerHTML = `
    <div>
      ${Espresso()}
      ${Americano()}
    </div>
  `;
  currentIndex = 0
}

rendering();
```

각각의 useState 함수로 관리되는 금액들이 잘 추가되는 것을 확인할 수 있습니다.

![hookResult](https://techblog.woowahan.com/wp-content/uploads/2022/06/hookResult.gif)

Hook은 2가지 사용 규칙이 있습니다.

> 최상위(at the Top Level)에서만 Hook을 호출해야 합니다.

Hook은 순서대로 배열에 저장됩니다. 만약 최상위 레벨이 아닌 조건문이나, 반복문, 중첩 함수에서 Hook을 사용한다면 **맨 처음 함수가 실행될 때 저장되었던 순서와 맞지 않게 됩니다.** 따라서 최초에 저장되었던 Hook의 상태 테이블에서 다른 상태 값을 참조하게 되는 버그를 유발할 수 있습니다. Hook의 상태 테이블은 useState 내부가 아닌 외부 상태를 참조하고 있기 때문입니다.

> 오직 React 함수 내에서 Hook을 호출해야 합니다.

Hook은 **React 함수 컴포넌트가 상태를 가질 수 있게 제공하는 기능**입니다. 따라서 React 함수가 아닌, 일반 함수는 Hook을 저장할 수도, 위치 값을 알 수도 없습니다. 클래스 컴포넌트는 상태가 변경될 때 인스턴스를 새롭게 만들지 않고, render 메서드를 통해 상태가 업데이트됩니다. 따라서 Hook의 호출 시점을 만들 수 없으므로 Hook을 사용할 수 없습니다. ~~(클래스 컴포넌트에서는 훅을 사용할 이유가 없습니다)~~

## 마치며

위의 내용들을 간단히 정리해 보겠습니다.

1. jQuery는 다루기 까다로운 DOM API를 직관적으로 손쉽게 다룰 수 있는 모델을 제시했습니다. 하지만, 성능 최적화의 아쉬움과 개발 생산성의 문제가 있었습니다.
2. **React는 개발자가 DOM API를 다룰 필요가 없게 만들고, 상태(State)를 기반으로 DOM을 업데이트**시켜 줍니다. 따라서, 충분히 빠른 성능과 개발 생산성에도 효과적인 모델을 제시했습니다.
3. 가상돔은 DOM의 형태를 본떠 만든 객체입니다.
4. JSX는 개발자는 익숙한 마크업 문법으로 개발하고, 바벨에서 createElement 함수로 변환해 VirtualDOM을 손쉽게 만들어 줍니다.
5. Diffing Update는 비교적 무거운 RealDOM의 비교가 아닌, 가벼운 VirtualDOM의 비교를 통해 적은 비용으로 충분히 빠르게 UI를 업데이트해 줍니다.
6. **Hook은 일종의 배열 데이터로, 클로저에 의해 저장**됩니다. React 함수 컴포넌트에서도 상태를 가질 수 있고, 렌더링 순서가 일정한 특성을 이용해 구현된 기능이므로, 2가지 규약이 있습니다.

웹 프런트엔드 UI 개발 라이브러리의 흐름이 jQuery에서 React로 왜 전환되었고, React 기능들이 어떻게 JavaScript 레벨에서 구현되는지 간단히 알아보았습니다. React를 사용하는 개발자들이, React를 더 잘 이해하고, 사용할 수 있는 데 이 글이 조금이나마 도움이 되었기를 바랍니다.

<br>

<br>

#### 참고링크: [Web Frontend | 우아한형제들 기술블로그 만들어 가며 알아보는 React: React는 왜 성공했나 (woowahan.com)](https://techblog.woowahan.com/8311/)

<br>