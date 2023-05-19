# 🔬 MobX란?

### 소개

 애플리케이션 상태에서 파생되는 모든 것은 자동으로 되어야 합니다.

 MobX는 functional reactive programming을 투명하게 적용함으로써 상태 관리를 쉽고 확장성 있게 만들어주는 검증된 라이브러리입니다. (TFRP, Transparent Functional Reactive Programming). MobX의 철학은 간단합니다.

<br>

##### 😙 쉽다.

 미니멀하고 보일러 플레이트로부터 자유로운 코드를 통해 당신의 의도를 잘 담아내 보세요. 데이터를 변경하고 싶습니까? 자바스크립트 할당문을 사용하면 됩니다. 비동기 과정에서 데이터를 변경하고 싶습니까? 새로운 도구는 필요 없으며 MobX 시스템이 변경사항을 찾아내고 사용 중인 곳에 전달합니다.

<br>

##### 🚅 렌더링 최적화를 쉽게 할 수 있다.

 데이터의 모든 변경과 사용은 런타임에 추적되고 상태와 출력 사이의 모든 관계를 나타내는 의존 트리(dependency tree)를 만듭니다. 따라서 리액트 컴포넌트들처럼 상태에 따라 필요한 경우에만 연산이 실행됩니다. 그래서 memoization, selectors 등을 사용하여 컴포넌트 최적화 작업을 할 필요가 없습니다.

<br>

##### 🤹🏻‍♂️ 구조가 자유롭다

 UI 프레임워크 밖에서 애플리케이션 상태를 관리 할 수 있습니다. 따라서 코드 분리가 쉽고 다른 곳에서 사용하기 유용하며 무엇보다 쉽게 테스트 할 수 있습니다.

<br>

<br>

## 간단한 예제

MobX를 사용하는 코드

```javascript
import React from "react"
import ReactDOM from "react-dom"
import { makeAutoObservable } from "mobx"
import { observer } from "mobx-react"

// 애플리케이션 상태를 모델링합니다.
class Timer {
    secondsPassed = 0

    constructor() {
        makeAutoObservable(this)
    }

    increase() {
        this.secondsPassed += 1
    }

    reset() {
        this.secondsPassed = 0
    }
}

const myTimer = new Timer()

// observable state를 사용하는 사용자 인터페이스를 구축합니다.
const TimerView = observer(({ timer }) => (
    <button onClick={() => timer.reset()}>Seconds passed: {timer.secondsPassed}</button>
))

ReactDOM.render(<TimerView timer={myTimer} />, document.body)

// 매초마다 Seconds passed: X를 업데이트 합니다.
setInterval(() => {
    myTimer.increase()
}, 1000)
```

 리액트 컴포넌트인 `TimerView`를 감싸고 있는 `observer`는 observable인 `timer.secondsPassed`에 의존하여 자동으로 렌더링 됩니다. reactivity 시스템은 나중에 해당 필드가 *정확하게* 수정될 때 컴포넌트를 다시 렌더링 합니다.

<br>

 모든 이벤트(`onClick`, `setInterval`)는 observable state(`myTimer.secondsPassed`)를 변경시키는 *action*(`myTimer.increase`, `myTimer.reset`)을 호출합니다. observable state의 변경 사항은 모든 연산과 변경사항에 따라 달라지는 부수 효과(`TimerView`)에 전파됩니다.

<br>

![MobX unidirectional flow](https://mobx.js.org/assets/flow2.png)

 위 그림은 위의 예시 또는 MobX를 사용하는 다른 애플리케이션에 적용할 수 있습니다.

<br>

 더 복잡한 예시를 이용한 [MobX의 요지](https://ko.mobx.js.org/the-gist-of-mobx.html), [10분만에 알아보는 MobX와 React](https://ko.mobx.js.org/getting-started.html)를 통해 MobX의 핵심 개념에 대해 알아볼 수 있습니다. MobX 모델의 철학과 장점은 [UI as an afterthought](https://michel.codes/blogs/ui-as-an-afterthought) 와 [How to decouple state and UI (a.k.a. you don’t need componentWillMount)](https://hackernoon.com/how-to-decouple-state-and-ui-a-k-a-you-dont-need-componentwillmount-cc90b787aa37) 에서 자세하게 확인할 수 있습니다.

<br>

<br>

#### 참고링크: [MobX에 대하여 · MobX](https://ko.mobx.js.org/README.html)

<br>

<br>

<br>

# MobX의 요지

## 개념

MobX는 어플리케이션에서 다음 세 가지 개념을 구분합니다.

1. 상태(state)
2. 동작(action)
3. 파생(derivation)

세 가지 개념에 대해 아래의 내용을 자세히 살펴보거나, [10분만에 알아보는 MobX와 React](https://ko.mobx.js.org/getting-started.html)에서 단계별로 심층적으로 살펴보고 간단한 Todo list 앱을 만들어보세요.

<br>

### 1. 상태(state)를 정의하고 관찰 가능하게(observable) 만들기

*State*는 애플리케이션을 구동하는 데이터입니다. 일반적으로 todo 아이템과 같은 *도메인 별 state*가 있고 현재 선택된 요소와 같은 *view state*가 있습니다. State는 값을 보유하고 있는 스프레드시트 셀과 같습니다.

원하는 데이터 구조(일반 객체, 배열, 클래스, 순환 데이터 구조 또는 참조)에 state를 저장합니다. 어떤 데이터 구조를 사용하든 MobX의 작동에는 문제가 되지 않습니다. 단지 시간이 지남에 따라 변경하려는 모든 속성을 MobX가 추적할 수 있도록 `observable`로 표시하면 됩니다.

여기 간단한 예제가 있습니다.

```javascript
import { makeObservable, observable, action } from "mobx"

class Todo {
    id = Math.random()
    title = ""
    finished = false

    constructor(title) {
        makeObservable(this, {
            title: observable,
            finished: observable,
            toggle: action
        })
        this.title = title
    }

    toggle() {
        this.finished = !this.finished
    }
}
```

**Hint**: [`makeAutoObservable`](https://ko.mobx.js.org/observable-state.html)을 사용하면 위 예제를 더 단순화 할 수 있지만, 이처럼 명시적으로 표시함으로써 다른 개념을 더 자세히 보여드리고 있습니다.

`observable`을 사용하는 것은 객체의 속성을 스프레드시트 셀로 바꾸는 것과 같습니다. 스프레드시트와 다른 점은 들어갈 수 있는 값이 원시 값(primitive values)뿐만 아니라 참조(reference), 객체 및 배열일 수도 있습니다.

`action`으로 표시된 `toggle`은 어떨까요?

<br>

### 2. action을 이용한 state 업데이트

*action*은 사용자 이벤트, 백엔드 데이터 푸시, 예약된 이벤트 등과 같이 *state*를 변경하는 코드 조각입니다. action은 스프레드시트 셀에 새 값을 입력하는 사용자와 같습니다.

위의 `Todo` 예제에서 `finished` 값을 바꾸는 `toggle`을 확인할 수 있으며, `finished`는 `observable`로 표시되어 있습니다. 위의 예시처럼 `observable`을 변경하는 코드는 [`action`](https://ko.mobx.js.org/actions.html)으로 표시하는 것이 좋습니다. 이렇게 하면 MobX가 트랜잭션을 자동으로 적용하여 성능을 쉽게 최적화할 수 있습니다.

action을 사용하면 코드를 구조화하는 데 도움을 줄 수 있으며 의도하지 않은 state 변경도 방지할 수 있습니다. state를 변경하는 메서드는 MobX 용어로 *action*이라고 합니다. 현재의 state를 기반으로 새로운 정보를 계산하는 *view*와는 대조적입니다. 모든 메서드는 이 두 가지 목표 중 하나에 기여해야 합니다.

<br>

### 3. 상태(state) 변화에 자동으로 응답하는 파생(derivation) 만들기

state에서 더 이상의 상호작용 없이 파생될 수 있는 *모든 것*이 derivation 입니다. derivation은 다음과 같이 다양한 형태로 존재할 수 있습니다.

- *사용자 인터페이스*
- 남은 `todos`의 수와 같은 *파생 데이터*
- *백엔드 통합* (예시: 서버에 변경사항 전송)

MobX는 다음과 같이 두 종류로 derivation을 구분합니다.

- *computed 값* : 현재의 observable state 에서 순수 함수를 사용하여 파생될 수 있는 값
- *reaction* : state가 변경될 때 자동으로 발생해야 하는 부수효과 (명령형 프로그래밍과 반응형 프로그래밍 사이를 연결해주는 다리 역할)

MobX를 시작할 때 reaction을 과도하게 사용하는 경향이 있습니다. 가장 좋은 방식은 현재 state를 기반으로 값을 생성하려는 경우에 항상 `computed`를 사용하는 것입니다.

<br>

#### 3.1. computed를 사용하여 파생된 값 모델링하기

*computed* 값을 생성하려면 JS getter 함수 `get`을 사용하여 속성을 정의하고 `makeObservable`을 사용하여 `computed`로 표시합니다.

```javascript
import { makeObservable, observable, computed } from "mobx"

class TodoList {
    todos = []
    get unfinishedTodoCount() {
        return this.todos.filter(todo => !todo.finished).length
    }
    constructor(todos) {
        makeObservable(this, {
            todos: observable,
            unfinishedTodoCount: computed
        })
        this.todos = todos
    }
}
```

MobX는 todo가 추가되거나 `finished` 속성 중 하나가 수정될 때 `unfinishedTodoCount`를 자동으로 업데이트합니다.

이러한 계산은 MS Excel과 같은 스프레드시트 프로그램의 공식과 유사합니다. 자동으로 업데이트되지만 필요할 때(무언가 결과에 영향을 미칠 수 있을 때)만 업데이트됩니다.

<br>

#### 3.2. reaction을 사용하여 부수효과(side effect) 모델링하기

사용자가 화면에서 state의 변화나 computed 값의 변화를 볼 수 있으려면 GUI의 일부를 다시 그리는 *reaction*이 필요합니다.

reaction은 computed 값과 유사하지만, 정보를 생성하는 대신 콘솔 출력, 네트워크 요청, DOM 패치 적용을 위해 React 컴포넌트 트리를 점진적으로 업데이트하는 등의 부수효과를 생성합니다.

간단히 말해, reaction은 [반응형](https://en.wikipedia.org/wiki/Reactive_programming) 프로그래밍과 [명령형](https://ko.wikipedia.org/wiki/명령형_프로그래밍) 프로그래밍의 세계를 연결합니다.

지금까지 가장 많이 사용되는 reaction 형태는 UI 컴포넌트입니다. action과 reaction 모두 부수효과를 일으킬 수 있습니다. form을 제출할 때 네트워크 요청을 하는 것처럼, 트리거 될 수 있는 명확하고 명시적인 출처가 있는 부수효과는 관련 이벤트 핸들러에서 명시적으로 트리거 되어야 합니다.

<br>

#### 3.3. 반응형 리액트 컴포넌트

React를 사용하는 경우 [설치 중에 선택한](https://ko.mobx.js.org/installation.html#installation) 바인딩 패키지에서 [`observer`](https://ko.mobx.js.org/react-integration.html) 함수를 이용하여 컴포넌트를 감싸서 반응형으로 만들 수 있습니다. 해당 예제에서는 더 가벼운 `mobx-react-lite` 패키지를 사용합니다.

```javascript
import * as React from "react"
import { render } from "react-dom"
import { observer } from "mobx-react-lite"

const TodoListView = observer(({ todoList }) => (
    <div>
        <ul>
            {todoList.todos.map(todo => (
                <TodoView todo={todo} key={todo.id} />
            ))}
        </ul>
        Tasks left: {todoList.unfinishedTodoCount}
    </div>
))

const TodoView = observer(({ todo }) => (
    <li>
        <input type="checkbox" checked={todo.finished} onClick={() => todo.toggle()} />
        {todo.title}
    </li>
))

const store = new TodoList([new Todo("Get Coffee"), new Todo("Write simpler code")])
render(<TodoListView todoList={store} />, document.getElementById("root"))
```

`observer`는 리액트 컴포넌트를 렌더링하는 데이터의 derivation으로 변환합니다. MobX를 사용하면 smart 컴포넌트나 dump 컴포넌트의 구분이 없습니다. 모든 컴포넌트는 smart하게 렌더링 되지만, dumb하게 정의됩니다. MobX에서는 필요할 때마다 컴포넌트가 다시 렌더링 되며, 그 이상은 렌더링 되지 않습니다.

따라서 위 예제의 `onClick` 핸들러는 `toggle` action을 사용할 때 적절한 `TodoView` 컴포넌트를 강제로 다시 렌더링하지만, `TodoListView` 컴포넌트는 완료되지 않은 작업의 수(unfinishedTodoCount)가 변경된 경우에만 다시 렌더링 됩니다. `Tasks left`줄을 지우거나 별도의 컴포넌트에 넣으면 Todo를 체크할 때 `TodoListView` 컴포넌트는 더 이상 다시 렌더링 되지 않습니다.

React가 MobX와 어떻게 작동하는지 자세히 알아보려면 [React 통합](https://ko.mobx.js.org/react-integration.html) 섹션을 확인해보세요.

<br>

#### 3.4. 커스텀 reaction

거의 필요하지는 않지만 [`autorun`](https://ko.mobx.js.org/reactions.html#autorun), [`reaction`](https://ko.mobx.js.org/reactions.html#reaction), [`when`](https://ko.mobx.js.org/reactions.html#when) 함수를 사용하여 상황에 맞게 만들 수 있습니다. 예를 들어, `autorun`은 `unfinishedTodoCount`의 수가 변경될 때마다 로그 메시지를 출력합니다.

```javascript
// state를 자동으로 관찰하는 함수입니다.
autorun(() => {
    console.log("Tasks left: " + todos.unfinishedTodoCount)
})
```

`unfinishedTodoCount`가 변경될 때마다 새 메시지를 출력하는 이유는 무엇일까요? 답은 아래의 원칙에 있습니다.

*MobX는 추적된 함수를 실행하는 동안 읽은 기존의 observable 속성에 반응합니다.*

MobX가 반응해야 하는 observable 항목을 결정하는 방법에 대해 자세히 알아보려면 [반응성 이해하기](https://ko.mobx.js.org/understanding-reactivity.html) 섹션을 확인해보세요.

<br>

## 원칙

MobX는 *action*이 *state*를 변경하는 단방향 데이터 흐름을 사용하여 영향을 받는 모든 *view*를 업데이트합니다.

![Action, State, View](https://ko.mobx.js.org/assets/action-state-view.png)

1. *state*가 변경되면 모든 *derivation*이 **자동으로** 그리고 **원자 단위로** 업데이트됩니다. 결과적으로 중간 값을 관찰할 수는 없습니다.
2. 기본적으로 모든 *derivation*은 **동기식**으로 업데이트 됩니다. 이는 *action*이 *state*를 변경한 직후에 computed 값을 안전하게 검사할 수 있음을 의미합니다.
3. *computed 값*은 **느리게** 업데이트됩니다. 활발히 사용되지 않는 계산된 값은 부수효과(I/O)에 필요할 때까지 업데이트되지 않습니다. 만약 view가 계산된 값을 사용하지 않으면 가비지가 자동으로 수집됩니다.
4. 모든 *computed 값*은 **순수**해야 하며 *state*를 바꾸면 안 됩니다.

이러한 배경이 생기게 된 맥락에 대해 더 알고 싶다면 [MobX의 기본 원칙](https://hackernoon.com/the-fundamental-principles-behind-mobx-7a725f71f3e8)을 확인하세요.
<br>

<br>

#### 참고링크: [MobX의 요지 · MobX](https://ko.mobx.js.org/the-gist-of-mobx.html)

<br>