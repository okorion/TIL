# Hooks API Reference

*Hook*는 React 16.8에서 새로 추가된 개념입니다. Hook을 통해 class를 작성하지 않고도 state와 같은 React 기능들을 사용할 수 있습니다.

이 페이지는 React에 내장된 Hook API를 설명합니다.

Hook이 생소하다면 [Hook 개요](https://ko.reactjs.org/docs/hooks-overview.html)를 먼저 읽어 보기 바랍니다. 혹은 [frequently asked questions](https://ko.reactjs.org/docs/hooks-faq.html)에서 유용한 정보를 찾을 수도 있습니다.

- [기본 Hook](https://ko.reactjs.org/docs/hooks-reference.html#basic-hooks)
  - [`useState`](https://ko.reactjs.org/docs/hooks-reference.html#usestate)
  - [`useEffect`](https://ko.reactjs.org/docs/hooks-reference.html#useeffect)
  - [`useContext`](https://ko.reactjs.org/docs/hooks-reference.html#usecontext)
- [추가 Hooks](https://ko.reactjs.org/docs/hooks-reference.html#additional-hooks)
  - [`useReducer`](https://ko.reactjs.org/docs/hooks-reference.html#usereducer)
  - [`useCallback`](https://ko.reactjs.org/docs/hooks-reference.html#usecallback)
  - [`useMemo`](https://ko.reactjs.org/docs/hooks-reference.html#usememo)
  - [`useRef`](https://ko.reactjs.org/docs/hooks-reference.html#useref)
  - [`useImperativeHandle`](https://ko.reactjs.org/docs/hooks-reference.html#useimperativehandle)
  - [`useLayoutEffect`](https://ko.reactjs.org/docs/hooks-reference.html#uselayouteffect)
  - [`useDebugValue`](https://ko.reactjs.org/docs/hooks-reference.html#usedebugvalue)
  - [`useDeferredValue`](https://ko.reactjs.org/docs/hooks-reference.html#usedeferredvalue)
  - [`useTransition`](https://ko.reactjs.org/docs/hooks-reference.html#usetransition)
  - [`useId`](https://ko.reactjs.org/docs/hooks-reference.html#useid)
- [Library Hooks](https://ko.reactjs.org/docs/hooks-reference.html#library-hooks)
  - [`useSyncExternalStore`](https://ko.reactjs.org/docs/hooks-reference.html#usesyncexternalstore)
  - [`useInsertionEffect`](https://ko.reactjs.org/docs/hooks-reference.html#useinsertioneffect)

## 기본 Hook

### `useState`

> Try the new React documentation for [`useState`](https://beta.reactjs.org/reference/react/useState).
>
> The new docs will soon replace this site, which will be archived. [Provide feedback.](https://github.com/reactjs/reactjs.org/issues/3308)

```
const [state, setState] = useState(initialState);
```

상태 유지 값과 그 값을 갱신하는 함수를 반환합니다.

최초로 렌더링을 하는 동안, 반환된 state(`state`)는 첫 번째 전달된 인자(`initialState`)의 값과 같습니다.

`setState` 함수는 state를 갱신할 때 사용합니다. 새 state 값을 받아 컴포넌트 리렌더링을 큐에 등록합니다.

```
setState(newState);
```

다음 리렌더링 시에 `useState`를 통해 반환받은 첫 번째 값은 항상 갱신된 최신 state가 됩니다.

> 주의
>
> React는 `setState` 함수 동일성이 안정적이고 리렌더링 시에도 변경되지 않을 것이라는 것을 보장합니다. 이것이 `useEffect`나 `useCallback` 의존성 목록에 이 함수를 포함하지 않아도 무방한 이유입니다.

#### 함수적 갱신

이전 state를 사용해서 새로운 state를 계산하는 경우 함수를 `setState` 로 전달할 수 있습니다. 그 함수는 이전 값을 받아 갱신된 값을 반환할 것입니다. 여기에 `setState`의 양쪽 형태를 사용한 카운터 컴포넌트의 예가 있습니다.

```
function Counter({initialCount}) {
  const [count, setCount] = useState(initialCount);
  return (
    <>
      Count: {count}
      <button onClick={() => setCount(initialCount)}>Reset</button>
      <button onClick={() => setCount(prevCount => prevCount - 1)}>-</button>
      <button onClick={() => setCount(prevCount => prevCount + 1)}>+</button>
    </>
  );
}
```

”+“와 ”-” 버튼은 함수 형식을 사용하고 있습니다. 이것은 갱신된 값이 갱신되기 이전의 값을 바탕으로 계산되기 때문입니다. 반면, “Reset” 버튼은 카운트를 항상 0으로 설정하기 때문에 일반적인 형식을 사용합니다.

업데이트 함수가 현재 상태와 정확히 동일한 값을 반환한다면 바로 뒤에 일어날 리렌더링은 완전히 건너뛰게 됩니다.

> 주의
>
> 클래스 컴포넌트의 `setState` 메서드와는 다르게, `useState`는 갱신 객체(update objects)를 자동으로 합치지는 않습니다. 함수 업데이터 폼을 객체 전개 연산자와 결합함으로써 이 동작을 복제할 수 있습니다.
>
> ```
> const [state, setState] = useState({});
> setState(prevState => {
>   // Object.assign would also work
>   return {...prevState, ...updatedValues};
> });
> ```
>
> 다른 방법으로는 `useReducer`가 있는데 이는 여러개의 하윗값들을 포함한 state 객체를 관리하는 데에 더 적합합니다.

#### 지연 초기 state

`initialState` 인자는 초기 렌더링 시에 사용하는 state입니다. 그 이후의 렌더링 시에는 이 값은 무시됩니다. 초기 state가 고비용 계산의 결과라면, 초기 렌더링 시에만 실행될 함수를 대신 제공할 수 있습니다.

```
const [state, setState] = useState(() => {
  const initialState = someExpensiveComputation(props);
  return initialState;
});
```

#### state 갱신의 취소

State Hook을 현재의 state와 동일한 값으로 갱신하는 경우 React는 자식을 렌더링 한다거나 무엇을 실행하는 것을 회피하고 그 처리를 종료합니다. (React는 [`Object.is` 비교 알고리즘](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/is#Description)을 사용합니다.)

실행을 회피하기 전에 React에서 특정 컴포넌트를 다시 렌더링하는 것이 여전히 필요할 수도 있다는 것에 주의하세요. React가 불필요하게 트리에 그 이상으로 「더 깊게」는 관여하지 않을 것이므로 크게 신경 쓰지 않으셔도 됩니다만, 렌더링 시에 고비용의 계산을 하고 있다면 `useMemo`를 사용하여 그것들을 최적화할 수 있습니다.

#### Batching of state updates

React may group several state updates into a single re-render to improve performance. Normally, this improves performance and shouldn’t affect your application’s behavior.

Before React 18, only updates inside React event handlers were batched. Starting with React 18, [batching is enabled for all updates by default](https://ko.reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html#automatic-batching). Note that React makes sure that updates from several *different* user-initiated events — for example, clicking a button twice — are always processed separately and do not get batched. This prevents logical mistakes.

In the rare case that you need to force the DOM update to be applied synchronously, you may wrap it in [`flushSync`](https://ko.reactjs.org/docs/react-dom.html#flushsync). However, this can hurt performance so do this only where needed.

### `useEffect`

> Try the new React documentation for [`useEffect`](https://beta.reactjs.org/reference/react/useEffect).
>
> The new docs will soon replace this site, which will be archived. [Provide feedback.](https://github.com/reactjs/reactjs.org/issues/3308)

```
useEffect(didUpdate);
```

명령형 또는 어떤 effect를 발생하는 함수를 인자로 받습니다.

변형, 구독, 타이머, 로깅 또는 다른 부작용(side effects)은 (React의 *렌더링 단계에* 따르면) 함수 컴포넌트의 본문 안에서는 허용되지 않습니다. 이를 수행한다면 그것은 매우 혼란스러운 버그 및 UI의 불일치를 야기하게 될 것입니다.

대신에 `useEffect`를 사용하세요. `useEffect`에 전달된 함수는 화면에 렌더링이 완료된 후에 수행되게 될 것입니다. React의 순수한 함수적인 세계에서 명령적인 세계로의 탈출구로 생각하세요.

기본적으로 동작은 모든 렌더링이 완료된 후에 수행됩니다만, [어떤 값이 변경되었을 때만](https://ko.reactjs.org/docs/hooks-reference.html#conditionally-firing-an-effect) 실행되게 할 수도 있습니다.

#### effect 정리

effect는 종종 컴포넌트가 화면에서 제거될 때 정리해야 하는 리소스를 만듭니다. 가령 구독이나 타이머 ID와 같은 것입니다. 이것을 수행하기 위해서 `useEffect`로 전달된 함수는 정리(clean-up) 함수를 반환할 수 있습니다. 예를 들어 구독을 생성하는 경우는 아래와 같습니다.

```
useEffect(() => {
  const subscription = props.source.subscribe();
  return () => {
    // Clean up the subscription
    subscription.unsubscribe();
  };
});
```

정리 함수는 메모리 누수 방지를 위해 UI에서 컴포넌트를 제거하기 전에 수행됩니다. 더불어, 컴포넌트가 (그냥 일반적으로 수행하는 것처럼) 여러 번 렌더링 된다면 **다음 effect가 수행되기 전에 이전 effect는 정리됩니다**. 위의 예에서, 매 갱신마다 새로운 구독이 생성된다고 볼 수 있습니다. 갱신마다 불필요한 수행이 발생하는 것을 회피하기 위해서는 다음 절을 참고하세요.

#### effect 타이밍

`componentDidMount`와 `componentDidUpdate`와는 다르게, `useEffect`로 전달된 함수는 지연 이벤트 동안에 레이아웃 배치와 그리기를 완료한 **후** 발생합니다. 이것은 구독이나 이벤트 핸들러를 설정하는 것과 같은 다수의 공통적인 부작용에 적합합니다. 왜냐면 대부분의 작업이 브라우저에서 화면을 업데이트하는 것을 차단해서는 안 되기 때문입니다.

그렇지만, 모든 effect가 지연될 수는 없습니다. 예를 들어 사용자에게 노출되는 DOM 변경은 사용자가 노출된 내용의 불일치를 경험하지 않도록 다음 화면을 다 그리기 이전에 동기화 되어야 합니다. (그 구분이란 개념적으로는 수동적 이벤트 리스너와 능동적 이벤트 리스너의 차이와 유사합니다) 이런 종류의 effect를 위해 React는 [`useLayoutEffect`](https://ko.reactjs.org/docs/hooks-reference.html#uselayouteffect)라는 추가적인 Hook을 제공합니다. 그것은 `useEffect`와 동일한 시그니처를 가지고 있고 그것이 수행될 때에만 차이가 납니다.

Additionally, starting in React 18, the function passed to `useEffect` will fire synchronously **before** layout and paint when it’s the result of a discrete user input such as a click, or when it’s the result of an update wrapped in [`flushSync`](https://ko.reactjs.org/docs/react-dom.html#flushsync). This behavior allows the result of the effect to be observed by the event system, or by the caller of [`flushSync`](https://ko.reactjs.org/docs/react-dom.html#flushsync).

> Note
>
> This only affects the timing of when the function passed to `useEffect` is called - updates scheduled inside these effects are still deferred. This is different than [`useLayoutEffect`](https://ko.reactjs.org/docs/hooks-reference.html#uselayouteffect), which fires the function and processes the updates inside of it immediately.

Even in cases where `useEffect` is deferred until after the browser has painted, it’s guaranteed to fire before any new renders. React will always flush a previous render’s effects before starting a new update.

#### 조건부 effect 발생

effect의 기본 동작은 모든 렌더링을 완료한 후 effect를 발생하는 것입니다. 이와 같은 방법으로 의존성 중 하나가 변경된다면 effect는 항상 재생성됩니다.

그러나 이것은 이전 섹션의 구독 예시와 같이 일부 경우에는 과도한 작업일 수 있습니다. `source` props가 변경될 때에만 필요한 것이라면 매번 갱신할 때마다 새로운 구독을 생성할 필요는 없습니다.

이것을 수행하기 위해서는 `useEffect`에 두 번째 인자를 전달하세요. 이 인자는 effect가 종속되어 있는 값의 배열입니다. 이를 적용한 예는 아래와 같습니다.

```
useEffect(
  () => {
    const subscription = props.source.subscribe();
    return () => {
      subscription.unsubscribe();
    };
  },
  [props.source],
);
```

자 이제, `props.source`가 변경될 때에만 구독이 재생성될 것입니다.

> 주의
>
> 이 최적화를 사용하는 경우, 값의 배열이 **시간이 지남에 따라 변경되고 effect에 사용되는 컴포넌트 범위의 모든 값들(예를 들어, props와 state와 같은 값들)을** 포함하고 있는지 확인하세요. 그렇지 않다면 여러분의 코드는 이전 렌더링에서 설정된 오래된 값을 참조하게 될 것입니다. [how to deal with functions](https://ko.reactjs.org/docs/hooks-faq.html#is-it-safe-to-omit-functions-from-the-list-of-dependencies)와 [array values change too often](https://ko.reactjs.org/docs/hooks-faq.html#what-can-i-do-if-my-effect-dependencies-change-too-often) 할 때 무엇을 할 것인지에 대해서 조금 더 알아보세요.
>
> effect를 수행하고 (mount를 하거나 unmount 할 때) 그것을 한 번만 실행하고 싶다면 두 번째 인자로 빈 배열(`[]`)을 전달할 수 있습니다. 이를 통해 effect는 React에게 props나 state에서 가져온 *어떤* 값에도 의존하지 않으므로, 다시 실행할 필요가 전혀 없다는 것을 알려주게 됩니다. 이것을 특별한 경우로 간주하지는 않고, 의존성 값의 배열이 항상 어떻게 동작하는지 직접적으로 보여주는 것뿐입니다.
>
> 빈 배열(`[]`)을 전달한다면 effect 안에 있는 props와 state는 항상 초깃값을 가지게 될 것입니다. 두 번째 인자로써 `[]`을 전달하는 것이 친숙한 `componentDidMount`와 `componentWillUnmount`에 의한 개념과 비슷하게 느껴지겠지만, effect가 너무 자주 리렌더링 되는 것을 피하기 위한 보통 [더 나은](https://ko.reactjs.org/docs/hooks-faq.html#is-it-safe-to-omit-functions-from-the-list-of-dependencies) [해결책](https://ko.reactjs.org/docs/hooks-faq.html#what-can-i-do-if-my-effect-dependencies-change-too-often)이 있습니다. 또한 브라우저가 모두 그려질 때까지 React는 `useEffect`의 수행을 지연하기 때문에 다른 작업의 수행이 문제가 되지는 않는다는 것을 잊지 마세요.
>
> [`eslint-plugin-react-hooks`](https://www.npmjs.com/package/eslint-plugin-react-hooks#installation) 패키지의 [`exhaustive-deps`](https://github.com/facebook/react/issues/14920) 규칙을 사용하기를 권장합니다. 그것은 의존성이 바르지 않게 정의되었다면 그에 대해 경고하고 수정하도록 알려줍니다.

의존성 값의 배열은 effect 함수의 인자로 전달되지는 않습니다. 그렇지만 개념적으로는, 이 기법은 effect 함수가 무엇일지를 표현하는 방법입니다. effect 함수 안에서 참조되는 모든 값은 의존성 값의 배열에 드러나야 합니다. 나중에는 충분히 발전된 컴파일러가 이 배열을 자동적으로 생성할 수 있을 것입니다.

### 



참고링크: [Hooks API Reference – React (reactjs.org)](https://ko.reactjs.org/docs/hooks-reference.html)