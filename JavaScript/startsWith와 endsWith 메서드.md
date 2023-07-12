# 🛫 String.prototype.startsWith()

**`startsWith()`** 메서드는 어떤 문자열이 특정 문자로 시작하는지 확인하여 결과를 `true` 혹은 `false`로 반환합니다.

<br>

## [시도해보기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#시도해보기)

<iframe class="interactive is-js-height" height="200" src="https://interactive-examples.mdn.mozilla.net/pages/js/string-startswith.html" title="MDN Web Docs Interactive Example" loading="lazy" data-readystate="complete" style="box-sizing: border-box; border: 0px; max-width: 100%; width: 765.719px; background-color: var(--background-secondary); border-radius: var(--elem-radius); color: var(--text-primary); height: 444px; margin: 1rem 0px; padding: 0px;"></iframe>

<br>

## [구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#구문)

JSCopy to Clipboard

```
startsWith(searchString)
startsWith(searchString, position)
```

<br>

### [매개변수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#매개변수)

- `searchString`

  문자열의 시작 지점에서 탐색할 문자열. 정규표현식이 올 수 없습니다.

- `position` Optional

  `searchString`을 탐색할 위치. 기본값은 `0`.

<br>

### [반환 값](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#반환_값)

대상 문자열이 주어진 문자로 시작하면 `true`, 아니면 `false`.

<br>

### [예외](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#예외)

- [`TypeError`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

  `searchString`이 [정규식일 경우](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/RegExp#special_handling_for_regexes).

<br>

## [설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#설명)

`startsWith` 메소드로 어떤 문자열이 다른 문자열로 시작하는지 확인 할 수 있습니다. 대소문자를 구분합니다.

<br>

## [예제](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#예제)

### [`startsWith()` 사용하기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#startswith_사용하기)

JSCopy to Clipboard

```
const str = "To be, or not to be, that is the question.";

console.log(str.startsWith("To be")); // true
console.log(str.startsWith("not to be")); // false
console.log(str.startsWith("not to be", 10)); // true
```



<br>

<br>

------------



# 🛬 String.prototype.endsWith()

The **`endsWith()`** 메서드를 사용하여 어떤 문자열에서 특정 문자열로 끝나는지를 확인할 수 있으며, 그 결과를 `true` 혹은 `false`로 반환한다.

<br>

## [문법](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith#문법)

```
str.endsWith(searchString[, length])
```

<br>

### [파라미터들](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith#파라미터들)

- `searchString`

  이 문자열의 끝이 특정 문자열로 끝나는지를 찾기 원하는 문자열입니다.

- `length`

  옵션입니다. 찾고자 하는 문자열의 길이값이며, 기본값은 문자열 전체 길이입니다. 문자열의 길이값은 문자열 전체 길이 안에서만 존재하여야 합니다.

<br>

### [반환 값](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith#반환_값)

문자열의 끝이 주어진 문자열로 끝나면 **`true`**, 그렇지 않다면 **`false`**

<br>

## [설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith#설명)

여러분은 이 메서드를 사용하여 어떤 문자열이 특정 문자열로 끝나는지를 확인할 수 있습니다.

<br>

## [예제](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith#예제)

### [`endsWith()` 사용하기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith#endswith_사용하기)

```
var str = 'To be, or not to be, that is the question.';

console.log(str.endsWith('question.')); // true
console.log(str.endsWith('to be'));     // false
console.log(str.endsWith('to be', 19)); // true
```

<br>

## [Polyfill](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith#polyfill)

이 메서드는 ECMAScript 6 규격에 포함되었습니다만 아직까지는 모든 JavaScrpt가 이 기능을 지원하고 있지는 않습니다. 하지만 여러분은 `String.prototype.endsWith()` 메서드를 다음과 같이 쉽게 [polyfill](https://en.wikipedia.org/wiki/Polyfill) 할 수 있습니다:

```
if (!String.prototype.endsWith) {
  String.prototype.endsWith = function(searchString, position) {
      var subjectString = this.toString();
      if (typeof position !== 'number' || !isFinite(position) || Math.floor(position) !== position || position > subjectString.length) {
        position = subjectString.length;
      }
      position -= searchString.length;
      var lastIndex = subjectString.indexOf(searchString, position);
      return lastIndex !== -1 && lastIndex === position;
  };
}
```

<br>

<br>

#### 참고링크: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith, https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith

<br>