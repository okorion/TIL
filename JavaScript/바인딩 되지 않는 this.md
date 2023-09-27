### 🛞 바인딩 되지 않은 this

화살표 함수가 나오기 전까지는, 모든 새로운 함수는, 어떻게 그 함수가 호출되는지에 따라 자신의 [`this`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this) 값을 정의했습니다:

- 이 함수가 생성자인 경우는 새로운 객체
- [엄격 모드](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Strict_mode) 함수 호출에서는 `undefined`
- 함수가 "객체 메서드"로서 호출된 경우 문맥 객체
- 등등

이는 객체 지향 스타일로 프로그래밍할 때 별로 좋지않습니다.

```js
function Person() {
  // Person() 생성자는 `this`를 자신의 인스턴스로 정의.
  this.age = 0;

  setInterval(function growUp() {
    // 비엄격 모드에서, growUp() 함수는 `this`를
    // 전역 객체로 정의하고, 이는 Person() 생성자에
    // 정의된 `this`와 다름.
    this.age++;
  }, 1000);
}

var p = new Person();
```

ECMAScript 3/5 에서는, 이 문제를 `this` 값을 폐쇄될 수 있는 (비전역) 변수에 할당하여 해결했습니다.



```js
function Person() {
  var that = this;
  that.age = 0;

  setInterval(function growUp() {
    // 콜백은  `that` 변수를 참조하고 이것은 값이 기대한 객체이다.
    that.age++;
  }, 1000);
}
```

이렇게 하는 대신에, [바인딩한 함수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)는 적절한 `this` 값이 `growUp()` 함수에 전달될 수 있도록 생성될 수 있습니다.

화살표 함수는 자신의 `this`가 없습니다. 대신 화살표 함수를 둘러싸는 렉시컬 범위(lexical scope)의 `this`가 사용됩니다; 화살표 함수는 일반 변수 조회 규칙(normal variable lookup rules)을 따릅니다. 때문에 현재 범위에서 존재하지 않는 `this`를 찾을 때, 화살표 함수는 바로 바깥 범위에서 `this`를 찾는것으로 검색을 끝내게 됩니다.

따라서 다음 코드에서 `setInterval`에 전달 된 함수 내부의 `this`는 `setInterval`을 포함한 function의 `this`와 동일한 값을 갖습니다.

```js
function Person() {
  this.age = 0;

  setInterval(() => {
    this.age++; // |this|는 Person 객체를 참조
  }, 1000);
}

var p = new Person();
```

#### 엄격 모드와의 관계

`this`가 렉시컬(lexical, 정적)임을 감안하면, `this`에 관한 [엄격 모드](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Strict_mode) 규칙은 그냥 무시됩니다.

```js
var f = () => {
  "use strict";
  return this;
};
f() === window; // 혹은 전역객체
```

엄격 모드의 나머지 규칙은 평소대로 적용합니다.



<br>

<br>

#### 참고링크: [화살표 함수 - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

<br>