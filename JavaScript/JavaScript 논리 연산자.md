## 🧱 JavaScript 논리 연산자

### X || Y

`X || Y` 논리 연산자는 수학에서 OR(또는)과 같습니다. `X`와 `Y`의 값 중에서 하나만 `True`이면, 전체도 `True`입니다.

```
<script>
  var a = 3;
  var b = 5;
  var c = (a<b) || (a>b);
  document.write(c);
</script>
```

[예제 ▷](https://jsfiddle.net/yukimura009/zc5bp6Lq/4/)

<br>

### X && Y

`X && Y` 논리 연산자는 수학에서 AND(그리고)와 같습니다. `X`와 `Y`값이 모두 `true`를 만족해야 전체도 `true`를 반환합니다.

```
<script>
  var a = 3;
  var b = 5;
  var c = (a<b) && (a>b);
  document.write(c);
</script>
```

[예제 ▷](https://jsfiddle.net/yukimura009/610v5j87/1/)

<br>

### ! X

`! X` 연산자는 수학의 ~(NOT)과 같습니다. `X`값이 `true`이면 `false`를 반환하고, `X`값이 `false`이면 `true`를 반환합니다.

```
<script>
  var a = 3;
  var b = 5;
  var c = !(a>b);
  document.write(c);
</script>
```

[예제 ▷](https://jsfiddle.net/yukimura009/01aqxj3g/2/)

논리 연산자는 비교 연산자와 함께 조건문 등에서 자주 사용됩니다.

<br>

<br>

#### 참고링크: [자바스크립트 논리 연산자 OR, AND, NOT 예제 - dasima](https://dasima.xyz/javascript-logical-operators/)

<br>