# 🤙 Promise

**`Promise`** 객체는 비동기 작업이 맞이할 미래의 완료 또는 실패와 그 결과 값을 나타냅니다.

**주의:** 이 기능은 [Web Worker](https://developer.mozilla.org/ko/docs/Web/API/Web_Workers_API)에서 사용할 수 있습니다

프로미스의 작동 방식과 프로미스 사용 방법에 대해 알아보려면 먼저 [프로미스 사용하기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Using_promises)을 읽어보세요.

## [설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#설명)

`Promise`는 프로미스가 생성된 시점에는 알려지지 않았을 수도 있는 값을 위한 대리자로, 비동기 연산이 종료된 이후에 결과 값과 실패 사유를 처리하기 위한 처리기를 연결할 수 있습니다. 프로미스를 사용하면 비동기 메서드에서 마치 동기 메서드처럼 값을 반환할 수 있습니다. 다만 최종 결과를 반환하는 것이 아니고, 미래의 어떤 시점에 결과를 제공하겠다는 '약속'(프로미스)을 반환합니다.

`Promise`는 다음 중 하나의 상태를 가집니다.

- 대기(*pending)*: 이행하지도, 거부하지도 않은 초기 상태.
- 이행(*fulfilled)*: 연산이 성공적으로 완료됨.
- 거부(*rejected)*: 연산이 실패함.

대기 중인 프로미스는 값과 함께 이행할 수도, 어떤 이유(오류)로 인해 거부될 수도 있습니다. 이행이나 거부될 때, 프로미스의 `then` 메서드에 의해 대기열(큐)에 추가된 처리기들이 호출됩니다. 이미 이행했거나 거부된 프로미스에 처리기를 연결해도 호출되므로, 비동기 연산과 처리기 연결 사이에 경합 조건은 없습니다.

[`Promise.prototype.then()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) 및 [`Promise.prototype.catch()` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) 메서드의 반환 값은 새로운 프로미스이므로 서로 연결할 수 있습니다.

![img](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/promises.png)

**참고:** 느긋한 평가와 연산 연기를 위한 방법을 프로미스라고 부르는 언어도 여럿 존재합니다(Scheme 등). JavaScript에서의 프로미스는 콜백 함수를 연결할 수 있는, 이미 진행 중인 프로세스를 나타냅니다. 표현식을 느긋하게 평가하려면 `f = () => expression`처럼 매개변수 없는 함수를 사용해 느긋한 표현식을 생성하고, `f()`를 호출해 평가하세요.

**참고:** 프로미스가 대기에서 벗어나 이행 또는 거부된다면 프로미스가 처리(*settled*)됐다고 말합니다. 프로미스와 함께 쓰이는 다른 단어인 '리졸브'(*resolved*)는 프로미스가 처리됐거나, 다른 프로미스의 상태에 맞춰 상태가 '잠김'됐다는 의미입니다. [States and fates](https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md)에서 프로미스 용어에 대한 보다 자세한 설명을 읽을 수 있습니다.

## [생성자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#생성자)

- [`Promise()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)

  새로운 `Promise` 객체를 생성합니다. 주로 프로미스를 지원하지 않는 함수를 감쌀 때 사용합니다.

## [정적 메서드](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#정적_메서드)

- [`Promise.all(iterable)`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

  주어진 모든 프로미스가 이행하거나, 한 프로미스가 거부될 때까지 대기하는 새로운 프로미스를 반환합니다.반환하는 프로미스가 이행한다면, 매개변수로 제공한 프로미스 각각의 이행 값을 모두 모아놓은 배열로 이행합니다. 배열 요소의 순서는 매개변수에 지정한 프로미스의 순서를 유지합니다.반환하는 프로미스가 거부된다면, 매개변수의 프로미스 중 거부된 첫 프로미스의 사유를 그대로 사용합니다.

- [`Promise.allSettled(iterable)`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)

  주어진 모든 프로미스가 처리(이행 또는 거부)될 때까지 대기하는 새로운 프로미스를 반환합니다.`Promise.allSettled()`가 반환하는 프로미스는 매개변수로 제공한 모든 프로미스 각각의 상태와 값(또는 거부 사유)을 모아놓은 배열로 이행합니다.

- [`Promise.any(iterable)` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any)

  주어진 모든 프로미스 중 하나라도 이행하는 순간, 즉시 그 프로미스의 값으로 이행하는 새로운 프로미스를 반환합니다.

- [`Promise.race(iterable)`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)

  주어진 모든 프로미스 중 하나라도 처리될 때까지 대기하는 프로미스를 반환합니다.반환하는 프로미스가 이행한다면, 매개변수의 프로미스 중 첫 번째로 이행한 프로미스의 값으로 이행합니다.반환하는 프로미스가 거부된다면, 매개변수의 프로미스 중 거부된 첫 프로미스의 사유를 그대로 사용합니다.

- [`Promise.reject(reason)`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject)

  주어진 사유로 거부하는 `Promise` 객체를 반환합니다.

- [`Promise.resolve()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)

  주어진 값으로 이행하는 `Promise` 객체를 반환합니다. 이때 지정한 값이 `then` 가능한(`then` 메서드를 가지는) 값인 경우, `Promise.resolve()`가 반환하는 프로미스는 `then` 메서드를 "따라가서" 자신의 최종 상태를 결정합니다. 그 외의 경우, 반환된 프로미스는 주어진 값으로 이행합니다.어떤 값이 프로미스인지 아닌지 알 수 없는 경우, 보통 일일히 두 경우를 나눠서 처리하는 대신 `Promise.resolve()`로 값을 감싸서 항상 프로미스가 되도록 만든 후 작업하는 것이 좋습니다.

## [인스턴스 메서드](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#인스턴스_메서드)

[마이크로태스크 안내서](https://developer.mozilla.org/ko/docs/Web/API/HTML_DOM_API/Microtask_guide)를 방문해 프로미스 인스턴스 메서드가 마이크로태스크 큐와 서비스를 이용하는 방법을 알아보세요.

- [`Promise.prototype.catch()` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)

  프로미스에 거부 처리기 콜백을 추가하고, 콜백이 호출될 경우 그 반환값으로 이행하며 호출되지 않을 경우, 즉 이전 프로미스가 이행하는 경우 이행한 값을 그대로 사용해 이행하는 새로운 프로미스를 반환합니다.

- [`Promise.prototype.then()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)

  프로미스에 이행과 거부 처리기 콜백을 추가하고, 콜백이 호출될 경우 그 반환값으로 이행하며 호출되지 않을 경우(`onFulfilled`, `onRejected` 중 상태에 맞는 콜백이 함수가 아닐 경우) 처리된 값과 상태 그대로 처리되는 새로운 프로미스를 반환합니다.

- [`Promise.prototype.finally()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)

  프로미스의 이행과 거부 여부에 상관없이 처리될 경우 항상 호출되는 처리기 콜백을 추가하고, 이행한 값 그대로 이행하는 새로운 프로미스를 반환합니다.

## [예제](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#예제)

### [기본 예제](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#기본_예제)

```
let myFirstPromise = new Promise((resolve, reject) => {
  // 우리가 수행한 비동기 작업이 성공한 경우 resolve(...)를 호출하고, 실패한 경우 reject(...)를 호출합니다.
  // 이 예제에서는 setTimeout()을 사용해 비동기 코드를 흉내냅니다.
  // 실제로는 여기서 XHR이나 HTML5 API를 사용할 것입니다.
  setTimeout( function() {
    resolve("성공!")  // 와! 문제 없음!
  }, 250)
})

myFirstPromise.then((successMessage) => {
  // successMessage는 위에서 resolve(...) 호출에 제공한 값입니다.
  // 문자열이어야 하는 법은 없지만, 위에서 문자열을 줬으니 아마 문자열일 것입니다.
  console.log("와! " + successMessage)
});
```

Copy to Clipboard

### [고급 예제](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#고급_예제)

다음의 작은 예제는 `Promise`의 동작 방식을 보여줍니다. `testPromise()` 함수는 [``](https://developer.mozilla.org/ko/docs/Web/HTML/Element/button)을 클릭할 때마다 호출되며, [`window.setTimeout()` (en-US)](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)을 사용해 1~3초의 무작위 간격 이후 프로미스 횟수(1부터 시작하는 숫자)로 이행하는 프로미스를 생성합니다. `Promise()` 생성자는 프로미스를 만드는 데 쓰입니다.

프로미스 이행은 [`p1.then()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)을 사용하는 이행 콜백 세트를 통해 단순히 로그에 남습니다. 약간의 로그를 통해, 함수의 동기 부분이 비동기적 프로미스의 완료와 어떻게 분리되어 있는지 확인할 수 있습니다.

#### HTML

```
<button id="btn">프로미스 만들기!</button>
<div id="log"></div>
```

Copy to Clipboard

#### JavaScript

```
'use strict';
var promiseCount = 0;

function testPromise() {
    var thisPromiseCount = ++promiseCount;

    var log = document.getElementById('log');
    log.insertAdjacentHTML('beforeend', thisPromiseCount +
        ') 시작 (<small>동기적 코드 시작</small>)<br/>');

    // 새 프로미스 생성 - 프로미스의 생성 순서를 전달하겠다는 약속을 함 (3초 기다린 후)
    var p1 = new Promise(
        // 실행 함수는 프로미스를 이행(resolve)하거나
        // 거부(reject)할 수 있음
        function(resolve, reject) {
            log.insertAdjacentHTML('beforeend', thisPromiseCount +
                ') 프로미스 시작 (<small>비동기적 코드 시작</small>)<br/>');
            // setTimeout은 비동기적 코드를 만드는 예제에 불과
            window.setTimeout(
                function() {
                    // 프로미스 이행 !
                    resolve(thisPromiseCount);
                }, Math.random() * 2000 + 1000);
        }
    );

    // 프로미스를 이행했을 때 할 일은 then() 호출로 정의하고,
    // 거부됐을 때 할 일은 catch() 호출로 정의
    p1.then(
        // 이행 값 기록
        function(val) {
            log.insertAdjacentHTML('beforeend', val +
                ') 프로미스 이행 (<small>비동기적 코드 종료</small>)<br/>');
        })
    .catch(
        // 거부 이유 기록
        function(reason) {
            console.log('여기서 거부된 프로미스(' + reason + ')를 처리하세요.');
        });

    log.insertAdjacentHTML('beforeend', thisPromiseCount +
        ') 프로미스 생성 (<small>동기적 코드 종료</small>)<br/>');
}

if ("Promise" in window) {
  var btn = document.getElementById("btn");
  btn.addEventListener("click", testPromise);
} else {
  log = document.getElementById('log');
  log.innerHTML = "Live example not available as your browser doesn't support the <code>Promise<code> interface.";
}
```



출처: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise



자바스크립트는 웹페이지를 동적으로 변화시키기 위해 태어났고, 이러한 태생 덕분에 필연적으로 비동기처리 형태를 갖게됐습니다.

dom 조작을 위해 javascript 코드가 동작하는 와중에도 웹 페이지가 멈추지 않도록 해야했기 때문이죠.

 

이번 글에서는 자바스크립트에서 비동기를 처리하는 방식인 callback과 callback의 문제점, ES6에 포함된 promise가 이를 어떻게 해결하는지에 대해서 알아보겠습니다.

 

(비동기가 어떻게 동작하는지에 대한 내용은 추후에 따로 다루겠습니다. 이번 글에서는 callback과 promise에 대한 부분만 살펴보겠습니다.)

 

 

**1. 비동기와 callback**

 

자바스크립트는 싱글 스레드로 동작합니다. 그럼에도 javascript가 병렬적으로 비동기 코드를 실행하는 것처럼 보이는 것은 비동기 처리를 외부 api에 위임하고, 완료된 작업을 event loop를 통해서 반환받고, 다시 javascript의 실행 영역에서 callback을 실행하기 때문입니다.

 

javascript에서 흔히 볼 수 있는 비동기와 callback으로 setTimeout을 들 수 있습니다.

```
setTimeout(function () {   
    console.log('hi'); 
}, 1000);
```

 

setTimeout을 통해 비동기처리가 외부 api(timer)에 위임되고, 1000ms가 지나면 callback 함수가 실행되어 콘솔창에 'hi'를 출력하게 됩니다.

 

또한 흔히 볼 수 있는 비동기와 callback으로 ajax 요청도 들 수 있습니다.

```
$.ajax({   
    type: 'POST',   
    url: 'http://something.com/members',   
    data: data,   
    error: function (error) {     
        console.log(error);   
    },   
    success: function (data) {     
        console.log(data);   
    }, 
});
```

 

위 코드도 마찬가지로 api를 요청하고 실행이 완료되면 그 결과에 따라 success 혹은 error callback을 실행하게 됩니다.

 

예전 작은 규모의 웹에서는 비동기 요청이 많지 않았고 각 비동기 요청간 의존성이 크지 않았지만, 웹이 발전하고 javascript가 서버를 비롯한 다양한 플랫폼으로 진출하면서 단순히 callback만으로 모든 상태를 통제하기 어렵게 됐습니다.

 

 

**2. 비동기 요청(과 callback)으로 발생하는 안티패턴**

 

요즘 교육과정에서는 어떻게 배우고 있을지 모르겠지만 제가 학교에서 수업을 들을때만해도 callback의 문제가 뭐냐 라고 물으면 주변 사람들은 '콜백 지옥'만을 이야기 했습니다.

 

또한 Promise를 사용하면 단순히 '콜백 지옥'을 해결하여 가독성을 높인다고 대답하는데, 참 모순적이게도 promise를 사용할 때도 우리는 then에 callback 함수를 넣어서 사용하고있습니다.

 

지금부터 callback에서 발생할 수 있는 문제, 정확히 말하자면 비동기 요청을 사용하므로써 발생할 수 있는 안티 패턴에 대해 알아보고 콜백 지옥이 아니라 promise가 이 문제들을 어떻게 해결할 수 있는지 알아보겠습니다.

 

 

**2-1. 비동기 응답 의존 관계에 따른 callback 중첩**

 

이 경우가 흔히 말하는 콜백 지옥의 예 입니다.

게시판에 글을쓰고 파일을 업로드하는 요청을 처리하는 서버 코드를 생각해볼 수 있습니다.

```
postRequest('/upload', function(req, res){
    var file = req.files[0];
    
    saveFile(file, function(originFileName){
        saveData(req.body, function(){       
            res.send("ok");     
        });   
    }); 
});
```

 

각 비동기 요청이 순차적으로 일어나는 것을 보장해야 하는 경우에 위와 같은 문제가 발생할 수 있습니다.

 

------

 

**2-2. 비동기 대 비동기(혹은 비동기 대 동기) 간 경쟁관계 발생**

 

이 경우는 위의 콜백 중첩패턴을 우회하기 위한 또다른 안티패턴으로 볼 수 있습니다.

```
var a = null; 
var b = null;  

function A(res) {   
    a = res;   
    if(a !== null && b !== null){     
        console.log(a + b);   
    } 
}); 

function B(res) {   
    b = res;   
    if(a !== null && b !== null){     
        console.log(a + b);   
    } 
});
```

 

여러 개의 비동기를 호출한 경우 A가 먼저 도착할수도, B가 먼저 도착할지 아무도 알 수 없습니다.

 

이를 방지하기위해 a 혹은 b 변수 값이 세팅되었는지 확인하는 작업을 각 콜백에 삽입해야하는 문제로, 관련 비동기 호출이 증가할수록 건드려야 하는 코드의 양이 기하급수적으로 증가합니다.

 

출처: https://yuddomack.tistory.com/entry/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%BD%9C%EB%B0%B1%EC%9D%98-%EB%AC%B8%EC%A0%9C%EC%A0%90%EA%B3%BC-%ED%94%84%EB%A1%9C%EB%AF%B8%EC%8A%A4-%EC%93%B0%EB%8A%94-%EC%9D%B4%EC%9C%A0