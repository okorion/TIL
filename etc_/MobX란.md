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