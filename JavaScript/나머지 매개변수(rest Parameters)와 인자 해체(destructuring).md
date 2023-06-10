## 🍟 나머지 매개변수(rest Parameters)와 인자 해체(destructuring)

자바스크립트에서 나머지 매개변수(rest parameters)와 인자 해체(destructuring)를 활용한 예시를 보여드리겠습니다.

1. 나머지 매개변수 (Rest Parameters):
나머지 매개변수는 함수 정의에서 `...`을 사용하여 표시하며, 전달된 인자들을 배열로 받습니다. 다음은 나머지 매개변수를 활용하여 전달된 숫자들의 합을 구하는 함수의 예시입니다:

```javascript
function sum(...numbers) {
  let total = 0;
  for (let i = 0; i < numbers.length; i++) {
    total += numbers[i];
  }
  return total;
}

console.log(sum(1, 2, 3, 4)); // 10
console.log(sum(5, 10, 15)); // 30
```

위 예시에서 `...numbers`는 나머지 매개변수로, 전달된 인자들을 `numbers` 배열로 받습니다. 함수 내부에서 배열을 순회하고 합산하여 결과를 반환합니다.

<br>

2. 인자 해체 (Argument Destructuring):
인자 해체를 사용하면 객체나 배열과 같은 구조에서 원하는 값들을 추출하여 변수로 할당할 수 있습니다. 다음은 객체를 인자로 받아 그 안에 있는 속성들을 변수로 추출하는 예시입니다:

```javascript
function printUserInfo({ name, age, city }) {
  console.log(`Name: ${name}`);
  console.log(`Age: ${age}`);
  console.log(`City: ${city}`);
}

const user = { name: 'John Doe', age: 25, city: 'New York' };
printUserInfo(user);
```

위 예시에서 `printUserInfo` 함수는 객체를 인자로 받고, 해당 객체의 `name`, `age`, `city` 속성을 변수로 추출하여 출력합니다. `user` 객체를 생성하고 함수에 전달함으로써 해당 속성들의 값을 출력할 수 있습니다.

<br>

인자 해체와 나머지 매개변수는 함수의 매개변수를 더 유연하게 다룰 수 있게 해주는 기능으로, 코드의 가독성과 유지보수성을 향상시키는 데 도움을 줍니다.

<br>

<br>

**👨‍💻 With ChatGPT 👨‍💻**

<br>