## 🍬 웹 워커(Web Worker)란?

웹워커는 Background Thread에서 스크립트를 실행하는 방법이다. UI Thread와는 별개의 Thread를 실행시켜 사용자 인터페이스(UI)를 방해하지 않고 작업을 수행할 수 있다.

– Thread란 어떠한 프로그램 내에서, 특히 [프로세스](https://ko.wikipedia.org/wiki/프로세스) 내에서 실행되는 흐름의 단위를 말한다. 일반적으로 한 프로그램은 하나의 스레드를 가지고 있지만, 프로그램 환경에 따라 둘 이상의 스레드를 동시에 실행할 수 있다. 이러한 실행 방식을 [멀티스레드](https://ko.wikipedia.org/wiki/멀티스레딩)(multithread)라고 한다. ( 출처 : [위키백과](https://ko.wikipedia.org/wiki/스레드) )

##### 웹 워커 활용

– 매우 복잡한 수학적 계산 작업
– 원격지에 있는 리소스에 대한 액세스 작업(또는 로컬 스토로지를 액세스 하는 경우)
– 백그라운드에서 오랜시간 작업해야 하는 경우
– UI 쓰레드에 방해 없이 지속적으로 수행해야 하는 작업 등

##### 웹 워커 지원 브라우저 확인

http://caniuse.com/#search=webworker

```
if ( !!window.Worker ) {
    alert('웹 워커를 지원하는 브라우저입니다.');
} else {
    alert( '웹 워커를 지원하지 않는 브라우저입니다.' );
}
```

## 웹 워커 사용하기

#### 1 ) Worker 실행 파일 ( worker.js ) 작성

워커가 실행할 스크립트는 별도의 자바스크립트 파일( worker.js )을 만들고 작성해야 한다. self는 워커 내부의 worker 전역 스코프에 대한 참조이다.

```
// worker 메시지 수신 listener
self.onmessage = function( e ) {
    console.log( 'Worker가 받은 메시지 ', e.data );

    // 1초 후에 호출한 페이지에 데이터를 보낸다.
    setTimeout( function() {
        postMessage( 'Worker Value' );
    }, 1000 );
};
```

#### 2 ) Worker 호출

Worker객체를 만든 후 생성한 worker 파일의 이름을 매개변수로  넘겨주어야 한다.

```
var worker = new Worker( 'worker.js' );
worker.postMessage( '워커 실행' );  // 워커에 메시지를 보낸다.

// 메시지는 JSON구조로 직렬화 할 수 있는 값이면 사용할 수 있다. Object등 
// worker.postMessage( { name : '302chanwoo' } );

// 워커로 부터 메시지를 수신한다.
worker.onmessage = function( e ) {
    console.log('호출 페이지 - ', e.data );
};
```

#### 3 ) 워커 종료하기

```
worker.terminate();
```

### 예제

1초마다 워커로부터 데이터를 전달받는 sample

<iframe width="100%" "="" height="150" src="http://302chanwoo.com/lab/worker" frameborder="0" style="box-sizing: border-box; margin: 0px; padding: 0px; border: 0px rgb(242, 242, 242); font: inherit; vertical-align: baseline; max-width: 100%;"></iframe>

#### worker.js

```
var i = 0; // 1씩 증가시켜서 전달할 변수

// 메시지 수신
self.onmessage = function( e ) {
    loop();
};

// 호출한 페이지에 1씩 증가시킨 i를 1초마다 전달한다.
function loop() {

    // 1씩 증가시켜서 전달
    postMessage( ++i ); 

    // 1초뒤에 다시 실행
    setTimeout( function() {
        loop();
    }, 1000 );

}
```

#### HTML

```
 <button id="btnStartWorker" class="btn">워커 시작</button>
<button id="btnStopWorker" class="btn">워커 중지</button>
<div id="output"></div> 
```

#### Javascript

```
    var btnStartWorker = document.getElementById( 'btnStartWorker' );     // worker 실행 버튼
    var btnStopWorker = document.getElementById( 'btnStopWorker' );       // worker 중지 버튼
    var output = document.getElementById( 'output' );                     // 받은 메시지 출력
    var worker;                                                           // worker

    btnStartWorker.addEventListener( 'click', startWorker );
    btnStopWorker.addEventListener( 'click',stopWorker );

    // worker 실행
    function startWorker() {

      // Worker 지원 유무 확인
      if ( !!window.Worker ) {

        // 실행하고 있는 워커 있으면 중지시키기
        if ( worker ) {
          stopWorker();
        }

        worker = new Worker( 'worker.js' );
        worker.postMessage( '워커 실행' );    // 워커에 메시지를 보낸다.

        // 메시지는 JSON구조로 직렬화 할 수 있는 값이면 사용할 수 있다. Object등
        // worker.postMessage( { name : '302chanwoo' } );

        // 워커로 부터 메시지를 수신한다.
        worker.onmessage = function( e ) {
          console.log('호출 페이지 - ', e.data );
          output.innerHTML += e.data;
        };
      }

    }

    // worker 중지
    function stopWorker() {

      if ( worker ) {
        worker.terminate();
        worker = null;
      }

    }
```

### 참고 자료

[www.slideshare.net/jidolstar/html5-web-worker](http://www.slideshare.net/jidolstar/html5-web-worker)
[www.html5rocks.com/en/tutorials/workers/basics/](http://www.html5rocks.com/en/tutorials/workers/basics/)
[developer.mozilla.org/ko/docs/Web/API/Web_Workers_API/basic_usage](http://developer.mozilla.org/ko/docs/Web/API/Web_Workers_API/basic_usage)
[프론트엔드 개발자를 위한 자바스크립트 프로그래밍](http://www.insightbook.co.kr/books/programming-insight/professional-javascript-for-web-developers)





<br>

<br>

#### 참고링크: [Web Worker 사용하기 - 302chanwoo blog](http://blog.302chanwoo.com/2016/08/webworker/)

<br>