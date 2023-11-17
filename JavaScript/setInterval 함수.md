## 🚉 setInterval 함수

setInterval() 함수는 일정한 시간 간격으로 지속적으로 반복해서 작업을 실행할 때 사용하는 자바스크립트 함수입니다.

 

이 함수를 사용하면 일정한 간격으로 코드를 실행할 수 있습니다.

 

아래는 setInterval() 함수를 사용하여 1초마다 "Hello, World!"라는 메시지를 콘솔에 출력하는 예시입니다.

 

```
setInterval(function() {
  console.log("Hello, World!");
}, 1000);
```

이 예시에서는 setInterval() 함수를 호출하여 콜백 함수를 반복적으로 실행하고 있습니다.

setInterval() 함수의 첫 번째 인수로 전달된 함수는 콜백 함수입니다. 이 콜백 함수는 setInterval() 함수가 호출된 후에 지정된 시간(두 번째 인수)마다 반복적으로 실행됩니다.

이 예시에서는 setInterval() 함수가 호출된 후 1초(1000밀리초)마다 "Hello, World!"라는 메시지가 콘솔에 출력됩니다.

 

 

setInterval() 함수는 주로 웹 애플리케이션에서 주기적으로 데이터를 갱신하거나 애니메이션을 구현하는 등의 작업을 수행할 때 사용됩니다.

예를 들어, 사용자가 입력한 내용을 바탕으로 차트를 그리는 경우, setInterval() 함수를 사용하여 일정한 간격으로 차트를 업데이트할 수 있습니다.

setInterval() 함수는 clearInterval() 함수와 함께 사용하여 반복 작업을 중지할 수 있습니다.

 

clearInterval() 함수는 setInterval() 함수로 설정한 타이머를 중지합니다. 타이머를 중지하려면 setInterval() 함수를 호출할 때 반환되는 타이머 ID를 clearInterval() 함수의 인수로 전달하면 됩니다.

 

아래는 setInterval() 함수를 사용하여 1초마다 콘솔에 출력되는 메시지를 clearInterval() 함수를 사용하여 중지하는 예시입니다.

 

```
// setInterval() 함수로 1초마다 "Hello, World!" 메시지를 출력하는 타이머 설정
var intervalId = setInterval(function() {
  console.log("Hello, World!");
}, 1000);

// 5초 후에 clearInterval() 함수를 사용하여 타이머 중지
setTimeout(function() {
  clearInterval(intervalId);
}, 5000);
```

이 예시에서는 setInterval() 함수를 사용하여 1초마다 "Hello, World!" 메시지를 출력하는 타이머를 설정하고 있습니다.

이후, 5초 후에 clearInterval() 함수를 사용하여 타이머를 중지하고 있습니다. setInterval() 함수는 타이머 ID를 반환하므로, clearInterval() 함수를 호출할 때 이 ID를 인수로 전달하여 타이머를 중지합니다.

 

이렇게 setInterval() 함수와 clearInterval() 함수를 함께 사용하여 일정한 간격으로 실행되는 코드를 원하는 시점에 중지할 수 있습니다.



<br>

<br>

#### 참고링크: [[javascript\] 일정간격으로 반복작업을 하기 위한 setInterval 사용하기 (tistory.com)](https://steady-dev.tistory.com/192)

<br>