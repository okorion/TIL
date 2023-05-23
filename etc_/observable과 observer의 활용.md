> MobX에서 observable로 둘러 쌓인 객체는 상태만 있는게 낫지 않을까? observable로 둘러쌓인 객체에 함수가 있으면 코드 가독성이 떨어지는 거 아닌가?

=> `observable 객체`는 변화 상태를 감지하는 것뿐만 아니라 `observable 객체`에 종속되어 있는 함수를 자동으로 실행하는 역할도 한다!
<br>
## 🔗 observable 객체에 종속된 함수
 observable로 둘러싸인 객체에 함수가 포함되는 것은 MobX에서 자주 사용되는 패턴 중 하나입니다. 이 패턴은 MobX의 핵심 기능 중 하나인 자동 반응(automatic reaction)을 통해 상태 변화를 감지하고 관련된 코드를 자동으로 실행할 수 있게 해줍니다.
 <br>

 함수가 observable 객체에 포함되는 것은 코드의 유연성과 효율성을 높일 수 있습니다. 몇 가지 이유로는 다음과 같습니다:

**1. 상태와 관련된 로직을 객체 내부에 캡슐화**: 함수를 observable 객체에 포함시키면 상태와 관련된 로직을 객체 내부에 캡슐화할 수 있습니다. 이로써 상태와 관련된 작업이 한 곳에 집중되어 코드의 구조를 개선하고 유지보수성을 높일 수 있습니다.

**2. 자동 반응**: MobX의 핵심 기능인 자동 반응은 observable 객체의 상태가 변경될 때 자동으로 해당 객체와 관련된 코드를 업데이트합니다. 함수가 observable 객체에 종속되어 있다면, 해당 함수는 상태 변화에 자동으로 반응하여 필요한 작업을 수행할 수 있습니다. 이는 코드를 더 간결하고 의도한 대로 동작하도록 만들어 줍니다.

**3. 코드 가독성**: 함수를 observable 객체에 포함시키면 상태와 관련된 로직이 한 곳에 모여 있어 가독성이 향상될 수 있습니다. 관련된 함수와 상태가 함께 그룹화되어 있으므로 코드를 이해하기 쉬워지고 디버깅이 용이해집니다.
<br>

물론, 모든 상황에서 함수를 observable 객체에 포함시키는 것이 가장 좋은 방법은 아닐 수 있습니다. 함수의 크기가 크거나 다른 객체와의 상호작용이 많은 경우에는 함수를 다른 곳에 분리하는 것이 더 적합할 수 있습니다. 하지만 작고 간단한 함수의 경우, observable 객체에 포함시키는 것이 코드의 구조와 가독성을 향상시킬 수 있습니다.
<br>

### 📃 예문
```
우리는 주문을 처리하는 온라인 상점을 운영한다고 가정합니다.
주문(order) 객체를 옵저버블로 만들고,
해당 객체에는 주문 상태를 처리하는 함수가 포함되어 있습니다.

주문 상태에 변화가 있을 때마다, 예를 들어 주문이 새로 생성되거나
배송이 완료되는 경우, 해당 함수는 자동으로 실행됩니다.
이 함수는 주문 상태에 맞게 알림을 보내는 역할을 할 수 있습니다.
예를 들어, 주문이 새로 생성되면 함수는 관리자에게 알림을 보내거나
고객에게 이메일을 발송할 수 있습니다.

이렇게 옵저버블 객체에 함수를 종속시킴으로써,
상태의 변화에 자동으로 반응할 수 있습니다.
우리는 별도의 코드를 작성하지 않아도 상태의 변화를 감지하고
필요한 작업을 수행할 수 있습니다.
이는 코드를 간결하고 효율적으로 유지할 수 있도록 도와줍니다.
```
<br>

### 🔌 예시 코드
 아래는 MobX를 사용하여 옵저버블 객체에 함수를 종속시키고, 상태 변화에 따라 함수가 자동으로 동작하는 예시 코드입니다. 코드 주석을 통해 설명을 추가하였습니다.

```
import { observable, autorun } from "mobx";

// 옵저버블 객체 생성
const user = observable({
  name: "Alice",
  age: 30,
});

// 함수 종속성 설정
autorun(() => {
  console.log(`${user.name} is ${user.age} years old.`);
  // user 객체의 name과 age에 종속된 함수
  // user의 상태가 변경될 때마다 자동으로 실행되며, 변경된 상태를 활용하여 작업을 수행함
});

// 상태 변경
user.name = "Bob";
user.age = 35;
```
위의 코드에서 user라는 옵저버블 객체를 생성하고, name과 age라는 상태를 갖습니다. 그리고 autorun 함수를 사용하여 함수를 종속성으로 설정합니다.

autorun 함수 내부의 함수는 user 객체의 name과 age에 종속되어 있습니다. 이 함수는 user 객체의 상태가 변경될 때마다 자동으로 실행되며, 변경된 상태를 활용하여 작업을 수행합니다.

예를 들어, user 객체의 name과 age가 변경되면, 콘솔에 ${user.name} is ${user.age} years old.라는 메시지가 출력됩니다. 이때 함수는 user 객체의 상태 변화를 감지하고, 변경된 상태를 바탕으로 메시지를 동적으로 생성합니다.

마지막으로 user 객체의 상태를 변경하면, 함수가 자동으로 실행되고 새로운 상태에 맞춰 메시지가 업데이트됩니다. 이렇게 옵저버블 객체에 함수를 종속시킴으로써, 상태의 변화에 따라 함수가 자동으로 동작하게 됩니다.
<br>

## 🎫 observable과 observer의 코드 구조

> 컴포넌트가 단계별로 중첩이 되어있으면 제일 및 단에 observable 객체를 넣고 그 위에는 단계별로 observer를 적용하면 되나?

=> 옵저버블 객체와 옵저버 패턴을 사용하여 컴포넌트를 중첩시킬 수 있습니다. 각 컴포넌트의 최하위 단계에 옵저버블 객체를 위치시키고, 상위 컴포넌트에는 옵저버를 적용하는 방식으로 구현할 수 있습니다.

예를 들어, 중첩된 컴포넌트 구조에서 최하위 컴포넌트에 있는 상태를 변경하면, 해당 컴포넌트를 감싸고 있는 상위 컴포넌트의 옵저버가 상태 변화를 감지하고 자동으로 업데이트됩니다.

```
import { observer } from "mobx-react";
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
// MiddleComponent에 observer를 적용하지 않아도 코드는 작동하지만
// MiddleComponent가 하위 컴포넌트인 LowestComponent의 상태 변화를 감지하고
// 업데이트해야 하는 경우에는 observer를 적용해야 함.
const MiddleComponent = () => {
  return (
    <div>
      <h2>Middle Component</h2>
      <LowestComponent />
    </div>
  );
};

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

위의 코드에서 LowestComponent는 최하위 컴포넌트로 옵저버블 객체 user를 사용합니다. user 객체의 name과 age를 출력하고, Increase Age 버튼을 클릭하면 age 상태를 증가시킵니다.

MiddleComponent는 LowestComponent를 포함하는 중간 단계 컴포넌트입니다.

TopComponent는 최상위 컴포넌트로, MiddleComponent를 감싸고 있습니다. 이 컴포넌트에서 observer를 사용하여 상위 컴포넌트가 하위 컴포넌트의 상태 변화를 감지하고 자동으로 업데이트되도록 설정합니다.

이렇게 구현하면 최하위 컴포넌트인 LowestComponent에서 상태 변경이 발생하면, 해당 컴포넌트를 감싸고 있는 상위 컴포넌트인 TopComponent의 옵저버가 상태 변화를 감지하고 UI를 업데이트합니다. 이를 통해 중첩된 컴포넌트 간의 상태 관리와 자동 업데이트를 구현할 수 있습니다.
<br>

👨‍🏫 **With ChatGPT** 💻
<br>