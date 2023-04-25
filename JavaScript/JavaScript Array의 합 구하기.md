# 🧮 JavaScript Array의 합 구하기

이 게시물은 JavaScript에서 어레이의 모든 값의 합을 찾는 방법에 대해 설명합니다.

## 1. 사용 `Array.prototype.reduce()` 기능

그만큼 [reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce) 메서드를 사용하여 각 어레이 요소에서 감속기 기능을 실행할 수 있습니다. 어레이의 모든 값의 합을 계산하려면 리듀서 함수가 현재 요소 값을 이전 값의 이미 계산된 합에 더해야 합니다.

요약하자면, 어레이에 포함된 값은 기본값을 제공해야 합니다. `reduce()` 메소드, 그렇지 않으면 코드가 던질 것입니다 `TypeError` 빈 어레이에. 이것은 익명 함수를 사용하여 아래에 설명되어 있습니다.

```javascript
add = function(arr) {
    return arr.reduce((a, b) => a + b, 0);
};
 
var arr = [3, 6, 1, 5, 8];
 
var sum = add(arr);
console.log(sum)
 
/*
    결과: 23
*/
```

<br>


ES6에는 위의 구문을 단순화하는 화살표 함수가 있습니다.

```javascript
const add = arr => arr.reduce((a, b) => a + b, 0);
 
var arr = [3, 6, 1, 5, 8];
var sum = add(arr);
 
console.log(sum)
 
/*
    결과: 23
*/
```

<br>

<br>

## 2. Lodash 라이브러리 사용하기

Lodash 도서관에는 [_.sum](https://lodash.com/docs/#sum) 어레이에 있는 값의 합을 계산할 수 있는 메서드입니다.


```javascript
var _ = require('lodash');
 
var arr = [3, 6, 1, 5, 8];
var sum = _.sum(arr);
 
console.log(sum)
 
/*
    결과: 23
*/
```

<br>

<br>

#### 참고링크: [JavaScript에서 배열의 모든 값의 합 찾기 (techiedelight.com)](https://www.techiedelight.com/ko/find-sum-values-array-javascript/)

<br>
