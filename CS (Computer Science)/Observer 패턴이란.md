## 🥸 Observer Pattern이란?

 옵저버 패턴이란 객체의 상태 변화를 관찰하는 관찰자들, 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴입니다. 어떤 객체의 변경 사항이 발생하였을때 이와 연관된 객체들에게 알려주는 디자인 패턴이라고 생각하시면 됩니다. 

 <br>

![옵저버 패턴](https://blog.kakaocdn.net/dn/dpoa8U/btqZjvUHSeB/f7deiNNAvQGkeu8CGa4Twk/img.jpg)

<br>

옵저버 패턴에는 주체 객체와 상태의 변경을 알아야 하는 관찰 객체(Observer Object)가 존재하며 이들의 관계는 1:1이 될 수도 있고 1:N이 될 수도 있습니다. 

 <br>

## 옵저버 패턴의 장단점

#### 장점

**1.** 실시간으로 한 객체의 변경사항을 다른 객체에 전파할 수 있습니다.

**2.** 느슨한 결합으로 시스템이 유연하고 객체간의 의존성을 제거할 수 있다.

 <br>

#### 단점

**1.** 너무 많이 사용하게 되면, 상태 관리가 힘들 수 있습니다

**2.** 데이터 배분에 문제가 생기면 자칫 큰 문제로 이어질 수 있습니다.

<br>

<br>

#### 참고링크: [[Design Pattern\] 옵저버 패턴(Observer Pattern)에 대하여 (tistory.com)](https://coding-factory.tistory.com/710)

<br>

<br>

<br>

### # 예시 (With ChatGPT)

옵저버블 객체와 옵저버 패턴을 사용하여 컴포넌트를 중첩시킬 수 있습니다. 각 컴포넌트의 최하위 단계에 옵저버블 객체를 위치시키고, 상위 컴포넌트에는 옵저버를 적용하는 방식으로 구현할 수 있습니다.

<br>

예를 들어, 중첩된 컴포넌트 구조에서 최하위 컴포넌트에 있는 상태를 변경하면, 해당 컴포넌트를 감싸고 있는 상위 컴포넌트의 옵저버가 상태 변화를 감지하고 자동으로 업데이트됩니다.

```
javascriptCopy codeimport { observer } from "mobx-react";
import { observable } from "mobx";

// 최하위 컴포넌트에서 사용할 옵저버블 객체
const user = observable({
  name: "Alice",
  age: 30,
});

// 최하위 컴포넌트
const LowestComponent = observer(() => {
  return (
    <div>
      <p>Name: {user.name}</p>
      <p>Age: {user.age}</p>
      <button onClick={() => user.age++}>Increase Age</button>
    </div>
  );
});

// 중간 단계 컴포넌트 
// #중간 단계에 observer가 적용 안 되어도 Top <-> Lowest <-> user는 상태 변화 감지 및 업데이트 가능!
const MiddleComponent = observer(() => {
  return (
    <div>
      <h2>Middle Component</h2>
      <LowestComponent />
    </div>
  );
});

// 최상위 컴포넌트
const TopComponent = observer(() => {
  return (
    <div>
      <h1>Top Component</h1>
      <MiddleComponent />
    </div>
  );
});

// 최상위 컴포넌트 렌더링
ReactDOM.render(<TopComponent />, document.getElementById("root"));
```

 위의 코드에서 `LowestComponent`는 최하위 컴포넌트로 옵저버블 객체 `user`를 사용합니다. `user` 객체의 `name`과 `age`를 출력하고, `Increase Age` 버튼을 클릭하면 `age` 상태를 증가시킵니다.

<br>

`MiddleComponent`는 `LowestComponent`를 포함하는 중간 단계 컴포넌트입니다.

<br>

`TopComponent`는 최상위 컴포넌트로, `MiddleComponent`를 감싸고 있습니다. 이 컴포넌트에서 `observer`를 사용하여 상위 컴포넌트가 하위 컴포넌트의 상태 변화를 감지하고 자동으로 업데이트되도록 설정합니다.

<br>

이렇게 구현하면 최하위 컴포넌트인 `LowestComponent`에서 상태 변경이 발생하면, 해당 컴포넌트를 감싸고 있는 상위 컴포넌트인 `TopComponent`의 옵저버가 상태 변화를 감지하고 UI를 업데이트합니다. 이를 통해 중첩된 컴포넌트 간의 상태 관리와 자동 업데이트를 구현할 수 있습니다.

<br>

### # Observer 패턴과 MVVM 패턴의 연관성 (With ChatGPT)

 옵저버 패턴은 객체 간의 일대다 의존성을 관리하는 패턴입니다. 한 객체의 상태 변화가 다른 여러 객체에게 자동으로 알림을 보내고, 그 객체들은 이를 수신하여 필요한 작업을 수행할 수 있습니다. 이는 객체 간의 느슨한 결합을 유지하면서 상호 작용을 가능하게 합니다.

<br>

 MVVM 패턴은 Model-View-ViewModel의 약자로, UI 개발을 위한 소프트웨어 아키텍처 패턴입니다. MVVM 패턴은 데이터와 비즈니스 로직을 분리하고, 데이터 바인딩을 통해 View와 ViewModel 사이의 양방향 통신을 지원합니다. ViewModel은 View의 데이터를 관리하고 표현 로직을 처리하며, View는 사용자 인터페이스를 담당합니다. Model은 비즈니스 데이터와 로직을 처리하는 역할을 수행합니다.

<br>

 MVVM 패턴에서 ViewModel은 일종의 옵저버 역할을 수행할 수 있습니다. ViewModel은 Model의 상태 변화를 감지하고, 이를 View에 알리는 역할을 합니다. View는 ViewModel을 옵저빙하여 ViewModel의 상태 변화를 자동으로 감지하고, 변경된 상태에 따라 자동으로 업데이트됩니다. 이를 통해 ViewModel과 View 사이에 느슨한 결합을 유지하며, 상호 작용을 가능하게 합니다.

<br>

 따라서, 옵저버 패턴은 MVVM 패턴의 일부 구성 요소로 사용될 수 있으며, ViewModel과 View 사이의 상태 변화 감지 및 업데이트 메커니즘을 구현하는 데에 활용될 수 있습니다.

<br>

<br>

**🚀 With ChatGPT 🚀**

<br>