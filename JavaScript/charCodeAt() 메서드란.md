## 🍭 charCodeAt() 메서드란?

## **아스키코드 및 유니코드 변환 방법**

아스키코드와 유니코드는 다른 개념이지만 처음 128개(0~127)의 코드는 동일합니다. 이번 포스팅은 JavaScript에서 아스키코드 및 유니코드로 변환하는 방법을 소개합니다.

<br>

------

### **charCodeAt() - 문자를 코드로 변환**

문자를 아스키코드로 변환하려면 charCodeAt() 메서드를 사용합니다. charCodeAt() 메서드는 문자열에서 호출할 수 있으며 특정 위치의 UTF-16 코드를 나타내는 0부터 65535 사이의 정수를 반환합니다.

```javascript
str.charCodeAt(index);
```

**매개변수**

index: 문자열의 특정 위치(인덱스)이며 생략하는 경우 0을 기본값으로 사용합니다.

 <br>

**반환 결과**

주어진 위치(인덱스)의 UTF-16 코드를 반환하며 0부터 65535 사이의 정수가 아닌 경우 NaN을 반환합니다.

```javascript
console.log('A'.charCodeAt());  // 65
console.log('A'.charCodeAt(0)); // 65

// 문자 'A'의 두 번째 인덱스는 undefined이므로 charCodeAt() 메서드는 NaN을 반환한다.
console.log('A'.charCodeAt(2)); // NaN
```

<br>

<br>

------

### **fromCharCode() - 코드를 문자로 변환**

fromCharCode() 메서드는 UTF-16 코드를 문자로 변환합니다.

```javascript
String.fromCharCode(code1, code2, ..., codeN);
```

**매개변수**

code1, code2, ..., codeN: 문자열로 변환하려는 코드를 매개변수로 전달할 수 있습니다. 매개변수의 갯수는 0에서 N개이며, 매개변수로 올바른 코드가 전달되었는지 유효성 검사는 수행하지 않습니다.

 <br>

**반환 결과**

변환된 문자열을 반환하며, 유효한 코드가 아닌 경우 빈 문자열("")을 반환합니다.

```javascript
console.log(String.fromCharCode(65, 66, 67)); // ABC
```

<br>

<br>

------

### **codePointAt() - 문자를 코드로 변환**

codePointAt() 메서드는 위에서 소개한 charCodeAt() 메서드와 유사하게 동작하는 것처럼 보이지만, codePointAt() 메서드가 표현할 수 있는 정수의 범위가 더 큽니다.

```javascript
str.codePointAt(index);
```

<br>

**매개변수**

index: 문자열의 특정 위치(인덱스)이며 생략하는 경우 0을 기본값으로 사용합니다.

 <br>

**반환 결과**

주어진 위치(인덱스)의 유니코드를 반환하며 주어진 위치에 문자가 없는 경우 undefined를 반환합니다.

```js
console.log('𐩕'.codePointAt()); // 68181
console.log('𐩕'.charCodeAt());  // 55298

console.log('⌥'.codePointAt()); // 8997
console.log('⌥'.charCodeAt());  // 8997

console.log('A'.codePointAt()); // 65
console.log('A'.charCodeAt());  // 65
```

위 예제에서 알 수 있듯이 codePointAt() 메서드와 charCodeAt() 메서드는 동일한 값을 반환하는 것처럼 보이지만, 일부 특수 기호는 다른 값을 반환합니다.

<br>

<br>

------

### **fromCodePoint() - 코드를 문자로 변환**

fromCodePoint() 메서드는 지정된 코드 포인트 시퀀스를 문자열로 반환합니다.

```js
String.fromCodePoint(code1, code2, ..., codeN);
```

**매개변수**

code1, code2, ..., codeN: 문자열로 변환하려는 코드를 매개변수로 전달할 수 있습니다. 매개변수의 갯수는 0에서 N개이며, fromCharCode() 메서드와 달리 유효성 검사를 수행합니다.

 <br>

**반환 결과**

변환된 문자열을 반환하며, 매개변수를 전달하지 않으면 빈 문자열("")을 반환합니다.

 <br>

**예외 및 에러**

잘못된 유니코드를 전달하거나 숫자 타입이 아닌 경우 RangeError 예외가 발생합니다.

```js
console.log(String.fromCodePoint(65, 66, 67)); // ABC
```

<br>

<br>

------

### **정리**

- 아스키코드와 유니코드는 다른 개념이지만, 0부터 127까지 128개의 코드는 동일합니다.
- JavaScript에서 문자를 코드로 변환하려면 charCodeAt(), codePointAt() 메서드를 사용합니다.
- JavaScript에서 코드를 문자로 변환하려면 fromCharCode(), fromCodePoint() 메서드를 사용합니다.

<br>

<br>

#### 참고링크: [[JavaScript\]아스키코드 및 유니코드 변환 방법 (tistory.com)](https://developer-talk.tistory.com/880)

<br>