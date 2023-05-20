## 🤫 배칭(Batching)이란?

리액트의 useState는 비동기로 작동한다. 그 이유는 성능을 위해 여러 호출을 모아 한번에 업데이트 한다. 즉, 배칭은 React Event 단위로 발생한다.

![img](https://velog.velcdn.com/images/dongha1992/post/67f95246-7135-4e68-89f4-ef638cdc99ff/image.png)

하나의 클릭 이벤트 내부에 여러 state 업데이트가 있으면 배칭 작업으로 클릭 이벤트 함수 실행이 끝나고 일괄 업데이트 한다(React 17기준)

배칭으로 인해 성능 상으로도 이점이 많고 아직 상태가 덜 렌더링된 컴포넌트의 리렌더링을 방지해서 여러모로 좋은 점이 많은데 배칭의 시점이 일관적이지 않아 문제가 많았다고 한다(제대로 겪진 못함)

<br>

가령, 아래와 같이 비동기로 데이터를 받고 데이터를 받은 후 어떠한 status(idle, pending, resolved, rejected) 를 변경하여 UI를 변경해야 한다고 했을 때, 상태는 독립적으로 업데이트가 되었다.

![img](https://velog.velcdn.com/images/dongha1992/post/d036c903-3736-4093-b797-8f72452ab7ae/image.png)

그 이유는 React가 클릭과 같은 브라우저 이벤트의 업데이트만 배칭을 하고, fetch 콜백에서 이벤트가 완료된 후 상태가 업데이트 되기 때문에 배칭이 적용되지 않는 것이다.

<br>

알기 쉬운 예제로는 어떤 데이터를 받아 status에 따라 다른 UI를 보여주는 앱이 있다고 가정 했을 때,

<br>

![img](https://velog.velcdn.com/images/dongha1992/post/f7eda91f-5a76-4923-aa5e-c9f07de7c054/image.png)

`status === 'resovled'`가 되어야 데이터를 View에 뿌린다.

<br>

![img](https://velog.velcdn.com/images/dongha1992/post/91bdb612-8ad3-4e09-99fc-30e62e507df2/image.png)

하지만 fetch하는 부분에서 status가 resloved가 되면 `setStatus` 상태를 업데이트 하고 `setPokemon`에 데이터를 넣기 전에 렌더를 하게 된다.

<br>

![img](https://velog.velcdn.com/images/dongha1992/post/96986fdd-b31b-4f83-96f5-321bf267e5c7/image.png)

즉, 아직 데이터 상태가 업데이트 되지 않았는데 UI가 렌더외어서 에러를 뱉게 되는 것이다.

** state를 object로 관리해서 status와 데이터를 같이 업데이트하면 해결되긴 한다.

<br>

<br>

## React18

React18에서 부터 createRoot를 통해 모든 업데이트에 자동 배칭이 적용되었다. (createRoot를 통해?)

![img](https://velog.velcdn.com/images/dongha1992/post/380948e0-c117-4950-86c2-4c76d42241a2/image.png)

** 리액트는 배칭이 '안전할 때'만 수행한다. 가령, click, keypress와 같은 유저가 실행한 이벤트의 경우 다음 이벤트 수행 이전에 DOM이 완벽히 업데이트가 되도록 보장한다. 이 과정을 통해 submit 버튼을 눌렀을 때 Form을 비활성화시켜 중복 전송을 방지한다.

** 배칭을 사용하고 싶지 않으면 `ReactDOM.flushSync()`을 쓰면 된다.

** 배칭을 이용해서 렌더링 최적화도 가능하다. input update가 생길 때마다 validation 해야 한다면 useEffect 말고 아래와 같이 사용하는 것이 좋다.

```null
const onChange = (e) => {
  setValue(e.target.value);
  setValidation(validate(e.target.value)); 
}

const validate = (value) => {
    ...
}
```

<br>

<br>

#### 참고링크: [React Batching (velog.io)](https://velog.io/@dongha1992/React-Batching)

<br>