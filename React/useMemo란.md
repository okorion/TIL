# 📋 useMemo란?

`useMemo`는 리액트에서 컴포넌트의 성능을 최적화 하는데 사용되는 훅이다.

`useMemo`에서 memo는 **memoization**을 뜻하는데 이는 그대로 해석하면 **‘메모리에 넣기’**라는 의미이며 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술이다.

쉽게 말해 동일한 값을 반환하는 함수를 반복적으로 호출해야한다면 처음 값을 계산할 때 해당 값을 메모리에 저장해 필요할 때마다 다시 계산하지 않고 메모리에서 꺼내서 재사용하는 것이다.

리액트에서 함수형 컴포넌트는 렌더링 => 컴포넌트 함수 호출 => 모든 내부 변수 초기화의 순서를 거친다.

예시와 함께 살펴보자.

```jsx
function Component() {
    const value = calculate();
    return <div>{value}</div> 
}

function calculate() {
    return 10;
}
```

컴포넌트가 렌더링 될 때마다 value라는 변수가 초기화된다.
즉, 렌더링 될 때마다 calculate 함수가 불필요하게 재호출된다는 것인데 만약 calculate가 무겁고 복잡한 함수라면 매우 비효율적일 것이다.

때문에 우리는 `useMemo` 훅을 사용하는 것인데 `useMemo`를 사용하면 렌더링 => 컴포넌트 함수 호출 => memoize된 함수 재사용하는 순서를 거친다.

이렇게 되면 calculate 함수를 반복적으로 실행할 필요가 없게 된다.
`useMemo`는 위에 말했듯이 처음에 계산된 값을 메모리에 저장해 컴포넌트가 계속 렌더링되어도 calculate를 다시 호출하지 않고 메모리에 저장되어있는 계산된 값을 가져와 재사용할 수 있게 해준다.

------

## 📌 1. useMemo의 구조

```jsx
const value = useMemo(() => {
    return calculate();
},[item])
```

`useMemo`는 `useEffect`처럼 첫 번째 인자로 콜백 함수, 두 번째 인자로 의존성 배열(dependancyArray)을 받는다.

의존성 배열 안에있는 값이 업데이트 될 때에만 콜백 함수를 다시 호출하여 메모리에 저장된 값을 업데이트 해준다.

만약 빈 배열을 넣는다면 `useEffect`와 마찬가지로 마운트 될 때에만 값을 계산하고 그 이후론 계속 memoization된 값을 꺼내와 사용한다.

------

## 📌 2. useMemo 예제 1

```jsx
import { useState } from "react";
 
const hardCalculate = (number) => {
  console.log("어려운 계산!");
  for (let i = 0; i < 99999999; i++) {} // 생각하는 시간
  return number + 10000;
};

const easyCalculate = (number) => {
  console.log("쉬운 계산!");
  return number + 1;
};

function App() {
  const [hardNumber, setHardNumber] = useState(1);
  const [easyNumber, setEasyNumber] = useState(1);

  const hardSum = hardCalculate(hardNumber);
  const easySum = easyCalculate(easyNumber);

  return (
    <div>
      <h3>어려운 계산기</h3>
      <input
        type="number"
        value={hardNumber}
        onChange={(e) => setHardNumber(parseInt(e.target.value))}
      />
      <span> + 10000 = {hardSum}</span>
      
      
      <h3>쉬운 계산기</h3>
      <input
        type="number"
        value={easyNumber}
        onChange={(e) => setEasyNumber(parseInt(e.target.value))}
      />
      <span> + 1 = {easySum}</span>
    </div>
  );
}

export default App;
```

위 예제엔 어려운 계산기와 쉬운 계산기가 있다.

어려운 계산기는 반복문을 99999999번 돌리고 값을 반환하기 때문에 숫자를 변경하면 누르면 1초 정도의 딜레이를 거친 후 값이 변경된다.

심지어 **쉬운 계산기의 값을 변경해도 1초 정도의 딜레이를 거친 후 값이 변경**된다.

그 이유는 쉬운 계산기의 input값을 변경하면 함수형 컴포넌트인 App이 리렌더링되는데 이 때, 위에서 말했듯 내부의 변수들이 초기화되기 때문에 hardCalculate가 다시 실행되기 때문이다.

그렇다면 이제 `useMemo`를 통해 이를 방지해보자.

```jsx
 const hardSum = useMemo(() => {
    return hardCalculate(hardNumber);
  }, [hardNumber]);
  const easySum = easyCalculate(easyNumber);
```

이처럼 `useMemo`의 첫 번째 인자로 콜백 함수를 넣고, 의존성 배열 안에 hardNumber를 넣어 hardNumber 값이 변경될 때에만 콜백함수가 실행되게 하면 된다.

하지만 리액트에서 `useMemo`가 정말 빛을 발하는 상황은 따로있다.
다음 예제를 통해 함께 살펴보자.

------

## 📌 3. useMemo 예제 2


(좌측 바를 땡겨 코드를 확인할 수 있습니다.)

`useEffect`의 의존성 배열에 location을 넣었는데 number state를 변경해도 useEffect가 실행된다.

그 이유는 자바스크립트에서 객체는 원시 타입과는 다르게 값이 저장될 때 주소 값으로 저장되기 때문이다.

그렇기 때문에 리액트에선 number state가 바뀌면 App 컴포넌트가 재호출되면서 location의 주소값이 변경이 되었기 때문에 location이 변경이 되었다고 인식을 한다.

여기서도 `useMemo` 훅을 통해 이를 방지할 수 있다.

위 식에서 주석을 통해 1번 location과 2번 location을 구분해놨으니 두개를 번갈아가며 사용해보면 어떤 차이가 있는지 확인할 수 있다.



<br>

<br>

#### 참고링크: [[React\] useMemo란? (velog.io)](https://velog.io/@jinyoung985/React-useMemo란)

<br>