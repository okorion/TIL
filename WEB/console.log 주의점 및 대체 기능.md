## 🥮 console.log 주의점 및 대체 기능

### **콘솔 로그의 함정 & 주의점**

브라우저의 console.log 를 사용할때 주의해야할 점이 있다. 예를들어 다음 예제가 콘솔에 어떻게 표시될지 예상해보자.

<br>

```javascript
var obj = {};

console.log(obj);

obj.a = 1;Copy
```

콘솔이 출력되는 라인은 아직 obj 에 값을 넣기 전이니 당연히 결과값이 {} 빈값이 출력이 될 것이다.

<br>

[![console.log](https://blog.kakaocdn.net/dn/I2Blc/btr5gwNUrYc/J6pe2tyAlVRTELLuTCRkWK/img.png)](https://blog.kakaocdn.net/dn/I2Blc/btr5gwNUrYc/J6pe2tyAlVRTELLuTCRkWK/img.png)

<br>

그런데 아래 화살표를 눌러보면, 아래와 같이 값이 a: 1 이 들어가 있음을 볼 수 있다. 즉, 결과값이 무언가 이상하게 짬뽕이 되어버린 것이다.

<br>

[![console.log](https://blog.kakaocdn.net/dn/b3np1l/btr5guJnvjH/W93WnKUXg0iVEjRacWVQ7K/img.png)](https://blog.kakaocdn.net/dn/b3np1l/btr5guJnvjH/W93WnKUXg0iVEjRacWVQ7K/img.png)

<br>

이러한 현상이 일어나는 이유는, console.log는 참조를 로깅하기 때문에 객체와 같이 내용물이 변할 수 있는 것들은 내용이 실시간으로 바뀌기 때문이다.

객체 뿐만 아니라 배열도 마찬가지이다.

<br>

```javascript
var arr = [];

console.log(arr, arr.length);

// 복잡한 코드가 있다고 가정

setTimeout(function() { // 비동기 가정
  arr.push(5);
}, 0);Copy
```

<br>

[![console.log](https://blog.kakaocdn.net/dn/clskx7/btr5pzbtaDF/qzrXfYmrjXhUK7paMkg6UK/img.png)](https://blog.kakaocdn.net/dn/clskx7/btr5pzbtaDF/qzrXfYmrjXhUK7paMkg6UK/img.png)

<br>

비동기를 통해 배열값 push를 후처리 하였기 때문에 당장 콘솔 결과값은 빈배열에 배열 length는 0이지만, 화살표를 눌러 안의 내용을 살펴보면 첫번째 인덱스 값이 들어가 있고 length 역시 1로 찍혀져 있는 걸 볼 수 있다.

<br>

[![console.log](https://blog.kakaocdn.net/dn/bglqZc/btr5gwf8Xse/0kLItMe3KPnEqVi44cguT1/img.png)](https://blog.kakaocdn.net/dn/bglqZc/btr5gwf8Xse/0kLItMe3KPnEqVi44cguT1/img.png)

<br>

<br>

------

### **이밖의 콘솔 자매들**

직접 스타일링 해주는 것도 좋지만 아래 미리 제공하는 콘솔 API 들도 이용하면 유용하다.

- console.log : 아이콘이 없는 검은색 텍스트
- console.info : 진한 텍스트
- console.debug : 파란색 텍스트
- console.warn : 아이콘이 있는 노란색 텍스트
- console.error : 아이콘이 있는 빨간색 텍스트

> Tip
>
> 단, 브라우저 종류마다 출력되는 스타일은 약간 다르다는 점은 유의하자

<br>

```JAVASCRIPT
var playerOne = 120;
var playerTwo = 130;
var playerThree = 140;
var playerFour = 150;
var playerFive = 160;

console.log("Console.log" + " " +  playerOne);
console.debug("Console.debug" + " " +playerTwo);
console.info("Console.info" + " " + playerFour);
console.warn("Console.warn" + " " + playerThree);
console.error("Console.error" + " " + playerFive);Copy
```

<br>

[![console.warn](https://blog.kakaocdn.net/dn/bCRDBp/btr5ep2FyXD/LF5RFaGSXA7Kss9uVA07dk/img.png)](https://blog.kakaocdn.net/dn/bCRDBp/btr5ep2FyXD/LF5RFaGSXA7Kss9uVA07dk/img.png)크롬 콘솔 출력 화면

<br>

이때 console.error 와 console.warn 은 단순한 값 출력 뿐만 아니라 문제가 발생하는 코드 라인 스택을 표시한다는 점에서 기능상 차이를 보인다.

보통 catch 문과 같이 오류 메세지를 콘솔 화면에 출력하기 위해 에러 내용을 습관적으로 console.log 로 처리하는 사람들이 있는데, 그릇된 방법은 아니지만 이보다 console.error 메서드를 사용하는 것이 훨씬 현명하다. 왜냐하면 console.warn과 같이 붉은색 배경에 기호 출력 뿐만 아니라 누적된 함수 호출 스택을 콘솔 화면에 표시해 주기 때문이다.

<br>

```JAVASCRIPT
const a = () => {
  console.error("error");
}
const b = () => {
  a()
}
const c = () => {
  b()
}

c()Copy
```

<br>

[![console.error](https://blog.kakaocdn.net/dn/F5Z81/btr5cEe59Uf/aCjmROhuhs8KDaHtkS14Y0/img.png)](https://blog.kakaocdn.net/dn/F5Z81/btr5cEe59Uf/aCjmROhuhs8KDaHtkS14Y0/img.png)

<br>

<br>

#### 참고자료: [📚 console.log는 이제 그만 ❗ - 다양한 콘솔 API 모음 (tistory.com)](https://inpa.tistory.com/entry/📚-다양한-콘솔-API#콘솔_로그의_함정__주의점)

<br>