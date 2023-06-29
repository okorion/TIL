## 🧬 every(), some() 함수란?

자바스크립트에서 Array의 [every()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/every)는 배열의 모든 요소가 어떤 조건을 충족하는지 확인하고, [some()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/some) 함수는 배열의 1개 요소라도 특정 조건을 충족하는지 확인하는데 사용합니다.

<br>

아래 코드는 some과 every를 사용하는 예제입니다. some과 every의 인자로 어떤 조건을 체크하는 callback 함수를 전달합니다. `some()`의 경우 1개 요소라도 callback에 대해서 true가 리턴되면 true를 리턴합니다. 반면에 `every()`는, 배열의 모든 요소가 callback에 대해서 true가 리턴되어야 true를 리턴합니다.

```js
var arr1 = [10, 20, 30, 40];

let result = arr1.some(num => num > 30);
console.log(result); // true

result = arr1.every(num => num > 30);
console.log(result); // false
```

- [1. every(), some() Syntax](https://codechacha.com/ko/javascript-array-every-some/#1-every-some-syntax)
- [2. every(), some()의 차이점](https://codechacha.com/ko/javascript-array-every-some/#2-every-some의-차이점)
- [3. Arrow function을 이용한 every(), some() 예제](https://codechacha.com/ko/javascript-array-every-some/#3-arrow-function을-이용한-every-some-예제)



<br>

## 1. every(), some() Syntax

every와 some 모두 callback 함수를 인자로 받습니다.

```txt
arr.every(callback)
arr.some(callback)
```

callback 함수는 아래와 같이 3개의 인자를 받습니다. index와 array가 필요하지 않다면 생략할 수 있습니다.

- element : 현재 함수로 전달된 요소
- index : 현재 요소의 index
- array : 배열 객체

```txt
function isEven(element, index, array)
```



<br>

## 2. every(), some()의 차이점

- every()는 모든 요소에 대해서 조건을 충족해야 true 리턴
- some()은 1개 요소만 충족해도 true를 리턴
- some의 경우, 어떤 요소가 조건을 충족하면 남아있는 요소들을 체크하지 않고 true 리턴 및 함수 종료. 남은 요소와 관계 없이 true를 리턴하기 때문에 남은 요소들을 확인할 필요 없음.
- every의 경우, 어떤 요소가 조건을 충족하지 못하면 남은 요소들을 체크하지 않고 false를 리턴. 남은 요소들이 조건을 충족해도 false가 리턴되기 때문에 체크할 필요 없음.

아래 예제를 보면, 위의 내용들을 확인할 수 있습니다.

```js
function isEven(element, index, array) {
  let even = (element % 2 === 0);
  console.log("element: " + element + ", index: "
    + index + ", array: " + array + ", even: " + even);
  return even;
}

console.log("# every test1");
let result = [10, 20, 30, 40].every(isEven);
console.log(result);

console.log("# every test2");
result = [10, 21, 30, 40].every(isEven);
console.log(result);

console.log("# some test1");
result = [10, 20, 30, 40].some(isEven);
console.log(result);

console.log("# some test2");
result = [11, 21, 31, 41].some(isEven);
console.log(result);
```

Output:

```txt
# every test1
element: 10, index: 0, array: 10,20,30,40, even: true
element: 20, index: 1, array: 10,20,30,40, even: true
element: 30, index: 2, array: 10,20,30,40, even: true
element: 40, index: 3, array: 10,20,30,40, even: true
true
# every test2
element: 10, index: 0, array: 10,21,30,40, even: true
element: 21, index: 1, array: 10,21,30,40, even: false
false
# some test1
element: 10, index: 0, array: 10,20,30,40, even: true
true
# some test2
element: 11, index: 0, array: 11,21,31,41, even: false
element: 21, index: 1, array: 11,21,31,41, even: false
element: 31, index: 2, array: 11,21,31,41, even: false
element: 41, index: 3, array: 11,21,31,41, even: false
false
```



<br>

## 3. Arrow function을 이용한 every(), some() 예제

다음과 같이 Arrow function을 사용하여 간단히 구현할 수 있습니다.

```js
let result = [10, 20, 30, 40].every(element => element % 2 === 0);
console.log(result);

result = [10, 20, 30, 40].some((element, index) => element % 2 === 0);
console.log(result);

result = [10, 20, 30, 40].some((element, index, arrow) => element % 2 === 0);
console.log(result);
```

Output:

```txt
true
true
true
```

<br>

<br>

#### 참고링크: [JavaScript - Array every(), some() 알아보기 (codechacha.com)](https://codechacha.com/ko/javascript-array-every-some/)

<br>