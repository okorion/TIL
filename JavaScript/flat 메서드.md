# 🍣 Array.prototype.flat()

**`flat()`** 메서드는 모든 하위 배열 요소를 지정한 깊이까지 재귀적으로 이어붙인 새로운 배열을 생성합니다.

<br>

## [구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/flat#구문)

```javascript
    const newArr = arr.flat([depth])
```

<br>

### [매개변수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/flat#매개변수)

- `depth` Optional

  중첩 배열 구조를 평탄화할 때 사용할 깊이 값. 기본값은 1입니다.

<br>

### [반환 값](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/flat#반환_값)

하위 배열을 이어붙인 새로운 배열.

<br>

## [예제](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/flat#예제)

### [중첩 배열 평탄화](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/flat#중첩_배열_평탄화)

```javascript
const arr1 = [1, 2, [3, 4]];
arr1.flat();
// [1, 2, 3, 4]

const arr2 = [1, 2, [3, 4, [5, 6]]];
arr2.flat();
// [1, 2, 3, 4, [5, 6]]

const arr3 = [1, 2, [3, 4, [5, 6]]];
arr3.flat(2);
// [1, 2, 3, 4, 5, 6]

const arr4 = [1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]];
arr4.flat(Infinity);
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

<br>

### [배열 구멍 제거](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/flat#배열_구멍_제거)

`flat` 메서드는 배열의 구멍도 제거합니다.

```javascript
const arr5 = [1, 2, , 4, 5];
arr5.flat();
// [1, 2, 4, 5]
```

<br>

<br>

#### 참고링크: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/flat

<br>