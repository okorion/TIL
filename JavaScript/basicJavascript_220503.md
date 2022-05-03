220503_basicJavascript TIL~



#### 1. 아래 설명을 읽고 T/F 여부를 작성하시오.

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다.

  => T

- XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다.

  => T

- XHR 객체를 활용하여 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다.

  => T

- axios는 XHR(XMLHTTPRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.

  => T

  

#### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

```js
console.log('Hello SAFY!')

setTimeout(function () {
    console.log('I am from setTimeout')
}, 1000)

console.log('Bye SAFY!')
```



1. Call Stack에 `console.log('Hello SAFY')`
   1. Output으로 `Hello SAFY`
   2. Call Stack 비워짐.

2. Call Stack에 `setTimeout(function () {console.log('I am from setTimeout')}, 1000)`
   1. Web API에 `function () {console.log('I am from setTimeout')}` 코드 Timer() 1초

3. Call Stack에 `console.log('Bye SAFY!')`
   1. Output으로 Bye SAFY!

4. 2-1의  `function () {console.log('I am from setTimeout')}` 가 Task Queue에 들어감.
   1. function(`console.log('I am from setTimeout')`)이 Call Stack에 들어감.
   2. Output으로 `I am from setTimeout`
