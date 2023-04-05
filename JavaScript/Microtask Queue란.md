## 🎼 Task Queue말고 다른 큐가 더 있다고? (MicroTask Queue, Animation Frames)

자바스크립트에서 비동기 함수가 동작하는 원리에 대해서 공부했다면, Task Queue에 대해 들어보았을 것이다. Task Queue는 Web API가 수행한 비동기 함수를 넘겨받아 Event Loop가 해당 함수를 Call Stack에 넘겨줄 때까지 비동기 함수들을 쌓아놓는 곳이다.

<br>

> **Task Queue말고 다른 큐가 더 있다고?**

그런데, JavaScript의 Promise를 공부하던 중 놀랍게도 Task Queue가 유일한 Queue가 아니라는 것을 알게 되었다. Event Loop는 **브라우저에 존재하는 여러 Queue들에 우선순위를 부여해 어떤 task를 먼저 수행할지 결정**한다.

<br>

## Task Queue(Macrotask Queue)

우리가 기존에 알고 있던 Task Queue는 뒤에서 설명한 Microtask Queue와 구별하기 위해 Macrotask Queue라고도 부른다.

- 이 큐는 setTimeout(), setInterval(), setImmediate()와 같은 task를 넘겨받는다.

그렇다면 Microtask Queue는 어떤 비동기 작업들을 넘겨받는 것일까?

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--05Fi8vBq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/42eatw03fcha0e1qcrf0.gif)



<br>

## Microtask Queue

- Microtask Queue는 Promise나 async/await, process.nextTick, Object.observe, MutationObserver과 같은 비동기 호출을 넘겨받는다.
- 그리고 Microtask의 우선순위는 일반 task(또는 macrotask)보다 더 높다.

<br>

코드로도 이를 확인해보자. 아래 예시처럼, Promise로 비동기 호출을 하면 해당 작업은 Microtask Queue에 쌓이게 되는데, Microtask는 setTimeout과 같은 일반 Task보다 높은 우선순위를 가지고 있어서, Promise함수의 내용이 setTimeout함수의 내용보다 더 먼저 출력되는 것을 확인할 수 있다.

```js
// 1. 실행
console.log('script start')

// 2. task queue로 전달
setTimeout(function() {
  // 8. task 실행
  console.log('setTimeout')
}, 0)

// 3. microtask queue로 전달
Promise.resolve()
  .then(function() {
    // 5. microtask 실행
    console.log('promise1')
    // 6. microtask queue로 전달
  })
  .then(function() {
    // 7. microtask 실행
    console.log('promise2')
  })

// 4. 실행
console.log('script end')
```

[해당페이지](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)를 클릭하면 애니메이션으로 동작과정을 확인할 수 있다.

<br>

(브라우저 환경에 따라 아래와 같은 결과가 나오지 않을 수도 있다. 이는 브라우저마다 비동기 작업을 처리하는 세부적인 구조가 다르기 때문인데, 이 글은 V8 엔진을 사용하는 Chrome 브라우저를 바탕으로 한 설명 글이다.)

```shell
script start
script end
promise1
promise2
setTimeout
```

<br>

<br>

### Promise

아래는 Promise가 Microtask Queue로 전달되는 과정을 나타낸 애니메이션이다.

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s---Bt6DKsn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/6cbjuexvy6z9ltk0bi18.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--6NSYq-nO--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/yqoemb6f32lvovge8yrp.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--us8FF30N--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/6wxjxduh62fqt531e2rc.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--oOS_-CiG--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/a6jk0exl137yka3oq9k4.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--5iH5BNWm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/lczn4fca41is4vpicr6w.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--hPFPTZp2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/p54casaaz9oq0g8ztpi5.gif)

<br>

<br>

### Async/Await

ES7에서는 Promise를 대체할 수 있는 async/await 문법이 등장했다. Async/Await이 Microtask Queue로 전달되는 과정을 확인해보자.

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--bfscMU3t--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/d27d7xxiekczftjyic4b.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--wN7yFTnt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/9wqej2269vmntfcuxs9t.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--lX9JfreE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/lch6lutxnl88j0durpyh.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--UC78HoCO--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/b6l3psgewvtrtmrr60tg.gif)

<br>

![img](https://res.cloudinary.com/practicaldev/image/fetch/s--V8u36kEG--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/hlhrtuspjyrstifubdhs.gif)

<br>



Async/Await을 쓸 경우, Promise와는 다른 모습을 보이는 것을 확인할 수 있다.

1. myFunc 함수 안의 두번째 줄이 실행되었을 때, one 함수는 콜 스택에서 pop되어 promise를 반환한다.
2. promise가 반환되었을 때 마주하는 것은 await 키워드인데, 이 경우 async 함수의 실행은 미뤄진다.
3. 그리고 async 함수의 나머지 부분들을 실행하는 것은 microtask Queue로 넘겨진다.

<br>

## Animation Frames

- Animation Frames는 requestAnimationFrame과 같이 브라우저 렌더링과 관련된 task를 넘겨받는 Queue이다.
- 우선순위는 Microtask보다는 낮고, (Macro)Task보다는 높다.

<br>

코드로 확인해보자.

```js
// 1. 실행
console.log("script start");

// 2. task queue로 전달
setTimeout(function () {
  // 10. task 실행
  console.log("setTimeout");
}, 0);

//3. microtask queue로 전달
Promise.resolve()
  .then(function () {
    // 6. microtask 실행
    console.log("promise1");
  }) // 7. microtask queue로 전달
  .then(function () {
    // 8. microtask 실행
    console.log("promise2");
  });

//4. AnimationFrame으로 전달
requestAnimationFrame(function () {
  //9. animation frame 실행
  console.log("animation");
});

//5. 실행
console.log("script end");
script start
script end
promise1
promise2
animation
setTimeout
```

<br>

## 정리

- 이벤트 루프가 비동기 작업을 처리하는 우선순위는 **Microtask Queue -> Animation Frames -> Task Queue** 순이다.
- 또한, 이벤트 루프는 Microtask Queue나 Animation Frames를 방문할 때는, 큐 안에 있는 **모든 작업들을 수행**하지만, Task Queue를 방문할 때는 **한 번에 하나의 작업**만 call stack으로 전달하고 다른 Queue를 순회한다.

<br>

![img](https://velog.velcdn.com/images%2Ftitu%2Fpost%2F0eeea3c2-986e-408d-ae56-52dad1143811%2Fimage.png)

------

<br>

<br>

<br>

참조:
https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/
https://dev.to/lydiahallie/javascript-visualized-promises-async-await-5gke#syntax
https://iamsjy17.github.io/javascript/2019/07/20/how-to-works-js.html

<br>

<br>

<br>

#### 참고링크: [[JavaScript\] Task Queue말고 다른 큐가 더 있다고? (MicroTask Queue, Animation Frames) (velog.io)](https://velog.io/@titu/JavaScript-Task-Queue말고-다른-큐가-더-있다고-MicroTask-Queue-Animation-Frames-Render-Queue)

<br>