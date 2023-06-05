# 👔 createPortal이란?

Portal은 부모 컴포넌트의 DOM 계층 구조 바깥에 있는 DOM 노드로 자식을 렌더링하는 최고의 방법을 제공합니다.

```
ReactDOM.createPortal(child, container)
```

첫 번째 인자(`child`)는 엘리먼트, 문자열, 혹은 fragment와 같은 어떤 종류이든 [렌더링할 수 있는 React 자식](https://ko.legacy.reactjs.org/docs/react-component.html#render)입니다. 두 번째 인자(`container`)는 DOM 엘리먼트입니다.

<br>

## 사용법

보통 컴포넌트 렌더링 메서드에서 엘리먼트를 반환할 때 그 엘리먼트는 부모 노드에서 가장 가까운 자식으로 DOM에 마운트됩니다.

```
render() {
  // React는 새로운 div를 마운트하고 그 안에 자식을 렌더링합니다.
  return (
    <div>      {this.props.children}
    </div>  );
}
```

그런데 가끔 DOM의 다른 위치에 자식을 삽입하는 것이 유용할 수 있습니다.

```
render() {
  // React는 새로운 div를 생성하지 *않고* `domNode` 안에 자식을 렌더링합니다.
  // `domNode`는 DOM 노드라면 어떠한 것이든 유효하고, 그것은 DOM 내부의 어디에 있든지 상관없습니다.
  return ReactDOM.createPortal(
    this.props.children,
    domNode  );
}
```

portal의 전형적인 유스케이스는 부모 컴포넌트에 `overflow: hidden`이나 `z-index`가 있는 경우이지만, 시각적으로 자식을 “튀어나오도록” 보여야 하는 경우도 있습니다. 예를 들어, 다이얼로그, 호버카드나 툴팁과 같은 것입니다.

<br>

> 주의
>
> portal을 이용하여 작업할 때 [키보드 포커스 관리](https://ko.legacy.reactjs.org/docs/accessibility.html#programmatically-managing-focus)가 매우 중요하다는 것을 염두에 두세요.
>
> For modal dialogs, ensure that everyone can interact with them by following the [WAI-ARIA Modal Authoring Practices](https://www.w3.org/WAI/ARIA/apg/patterns/dialogmodal/).



<br>

<br>

#### 참고링크: [Portals – React (reactjs.org)](https://ko.legacy.reactjs.org/docs/portals.html)

<br>

