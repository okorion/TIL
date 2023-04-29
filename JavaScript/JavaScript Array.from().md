# 🚋 JavaScript Array.from()

**`Array.from()`** 메서드는 유사 배열 객체(array-like object)나 반복 가능한 객체(iterable object)를 얕게 복사해 새로운`Array` 객체를 만듭니다.

<br>

## [시도해보기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#시도해보기)

<iframe class="interactive is-js-height" height="200" src="https://interactive-examples.mdn.mozilla.net/pages/js/array-from.html" title="MDN Web Docs Interactive Example" loading="lazy" data-readystate="complete" style="box-sizing: border-box; border: 0px; max-width: 100%; width: 765.719px; background-color: var(--background-secondary); border-radius: var(--elem-radius); color: var(--text-primary); height: 444px; margin: 1rem 0px; padding: 0px;"></iframe>

<br>

## [구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#구문)

```
    Array.from(arrayLike[, mapFn[, thisArg]])
```

<br>

### [매개변수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#매개변수)

- `arrayLike`

  배열로 변환하고자 하는유사 배열 객체나 반복 가능한 객체.

- `mapFn` Optional

  배열의 모든 요소에 대해 호출할 맵핑 함수.

- `thisArg` Optional

  `mapFn` 실행 시에 `this`로 사용할 값.

  <br>

### [반환 값](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#반환_값)

새로운 [`Array`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array) 인스턴스.

<br>

## [설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#설명)

다음과 같은 경우에 `Array.from()`으로새`Array`를 만들 수 있습니다.

- 유사 배열 객체 (`length` 속성과 인덱싱 된 요소를 가진 객체)
- [순회 가능한 객체 (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) ([`Map`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Map), [`Set`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set) 등객체의 요소를 얻을 수 있는 객체)

`Array.from()`은 선택 매개변수인 `mapFn`를 가지는데, 배열(혹은 배열 서브클래스)의 각 요소를[맵핑](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map)할 때 사용할 수 있습니다. 즉,`Array.from(obj, mapFn, thisArg)`는 중간에 다른 배열을 생성하지 않는다는 점을 제외하면`Array.from(obj).map(mapFn, thisArg)`와 같습니다. 이 특징은 [typed arrays](https://developer.mozilla.org/ko/docs/Web/JavaScript/Typed_arrays)와 같은 특정 배열 서브클래스에서 중간 배열 값이 적절한 유형에 맞게 생략되기 때문에 특히 중요합니다.

`from()` 메서드의 `length` 속성은 1입니다.

ES2015 이후, 클래스 구문은 내장 및 새 클래스의 상속을 가능케 했습니다. 그 결과로 `Array.from`과 같은 정적 메서드는 `Array`의 서브클래스에 의해 상속되며, `Array` 대신 자신의 인스턴스를 만듭니다.

<br>

## [예제](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#예제)

### [`String`에서 배열 만들기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#string에서_배열_만들기)

```javascript
Array.from('foo');
// ["f", "o", "o"]
```

<br>

### [`Set`에서 배열 만들기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#set에서_배열_만들기)

```javascript
const s = new Set(['foo', window]);
Array.from(s);
// ["foo", window]
```

<br>

### [`Map`에서 배열 만들기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#map에서_배열_만들기)

```javascript
const m = new Map([[1, 2], [2, 4], [4, 8]]);
Array.from(m);
// [[1, 2], [2, 4], [4, 8]]

const mapper = new Map([['1', 'a'], ['2', 'b']]);
Array.from(mapper.values());
// ['a', 'b'];

Array.from(mapper.keys());
// ['1', '2'];
```

<br>

### [배열 형태를 가진 객체(`arguments`)에서 배열 만들기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#배열_형태를_가진_객체arguments에서_배열_만들기)

```javascript
function f() {
  return Array.from(arguments);
}

f(1, 2, 3);

// [1, 2, 3]
```

<br>

### [`Array.from`과 화살표 함수 사용하기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#array.from과_화살표_함수_사용하기)

```javascript
// Using an arrow function as the map function to
// manipulate the elements
Array.from([1, 2, 3], x => x + x);
// [2, 4, 6]

// Generate a sequence of numbers
// Since the array is initialized with `undefined` on each position,
// the value of `v` below will be `undefined`
Array.from({length: 5}, (v, i) => i);
// [0, 1, 2, 3, 4]
```

<br>

### [시퀀스 생성기(range)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from#시퀀스_생성기range)

```javascript
// Sequence generator function (commonly referred to as "range", e.g. Clojure, PHP etc)
const range = (start, stop, step) => Array.from({ length: (stop - start) / step + 1}, (_, i) => start + (i * step));

// Generate numbers range 0..4
range(0, 4, 1);
// [0, 1, 2, 3, 4]

// Generate numbers range 1..10 with step of 2
range(1, 10, 2);
// [1, 3, 5, 7, 9]

// Generate the alphabet using Array.from making use of it being ordered as a sequence
range('A'.charCodeAt(0), 'Z'.charCodeAt(0), 1).map(x => String.fromCharCode(x));
// ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
```

<br>

<br>

#### 참고링크: [Array.from() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from)

<br>