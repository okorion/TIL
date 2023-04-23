# 🔢 Math.max()

**Math.max()** 함수는 입력값으로 받은 0개 이상의 숫자 중 가장 큰 숫자를 반환합니다.

<br>

## [시도해보기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max#시도해보기)

<iframe class="interactive is-js-height" height="200" src="https://interactive-examples.mdn.mozilla.net/pages/js/math-max.html" title="MDN Web Docs Interactive Example" loading="lazy" data-readystate="complete" style="box-sizing: border-box; border: 0px; max-width: 100%; width: 635.438px; background-color: var(--background-secondary); border-radius: var(--elem-radius); color: var(--text-primary); height: 444px; margin: 1rem 0px; padding: 0px;"></iframe>



<br>

## [문법](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max#문법)

```
  Math.max()
  Math.max(값0)
  Math.max(값0, 값1)
  Math.max(값0, 값1, ... , 값N)
```

Copy to Clipboard

<br>

### [매개변수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max#매개변수)

- `값1, 값2, ...`

  가장 큰 값을 선택하고 반환할 0개 이상의 숫자입니다.

  <br>

### [반환 값](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max#반환_값)

입력된 숫자 중 가장 큰 숫자를 반환합니다. 만약 인수 중 하나라도 숫자로 변환하지 못한다면 [`NaN`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/NaN)로 반환합니다. 매개변수를 제공하지 않은 경우 결과는 -[`Infinity`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Infinity)입니다.

<br>

## [설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max#설명)

max ()는 Math의 정적 메서드이기 때문에 만든 Math 개체의 메서드가 아닌 항상 Math.max ()로 사용해야합니다. (Math는 생성자가 아닙니다).

만약 아무 요소도 주어지지 않았다면 -[`Infinity`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Infinity)로 반환합니다.

만약 한 개 이상의 요소가 숫자로 변환되지 않는다면 [`NaN`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/NaN)로 반환됩니다.

<br>

## [예제](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max#예제)

### [`Math.max()함수 사용하기`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max#math.max함수_사용하기)

```
Math.max(10, 20);   //  20
Math.max(-10, -20); // -10
Math.max(-10, 20);  //  20
```



<br>

<br>

#### 참고링크: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max

<br>