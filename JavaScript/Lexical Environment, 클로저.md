### Lexical Environment의 개념

`Lexical Environment`는 코드 `block`, `function`, `script`를 실행하기 앞서 생성되는 특별한 객체로, 실행할 스코프 범위 안에 있는 **변수와 함수를 프로퍼티로 저장하는 객체**다.

즉 우리가 소스 코드를 실행하면서 참조가 필요한 변수의 값을 이 Lexical Environment 라는 객체에서 식별자 이름을 키로 찾는다고 보면 된다.





### 클로저

이제 렉시컬 환경이 어떻게 클로저를 가능하게 하는지 살펴보자.

```javascript
function makeCounter() {
  let count = 0;
 
  return function() {
    return count++;
  };
}
 
let counter = makeCounter();
```

**makeCounter라는 함수의 호출이 시작될 때, 새로운 렉시컬 환경이 만들어진다.** 그리고 makeCounter 함수 실행에 필요한 변수를 저장할 것이다. 거기에는 count 라는 로컬 변수가 저장될 것이다.

그리고 여기서 특이한 점은 함수를 리턴하고 있는데, 그 함수가 리턴하는 것이 `count++` 라는 것이다. 어쨌거나 makeCounter 함수가 실행하면서 저 리턴 함수는 **만들어져서** counter 변수에 저장될 것이다. 포인트는 counter 함수가 만들어지기만 했다는 것이다. 이 함수를 실행하지는 않았다.

이제 counter 변수에는 함수가 만들어진 함수가 저장돼 있고, counter를 호출하면, 0이라는 값이 리턴된다.

즉 makeCounter에 있었던 count 변수를 참조할 수 있다는 뜻이다.

이것이 어떻게 가능하냐면, **모든 함수는 `[[Environment]]` 라는 내부 프로퍼티를 갖고 있다.** **이 프로퍼티는 함수가 만들어질 때 그 함수를 둘러싼 외부 렉시컬 환경에 대한 참조를 저장한다.** 다시 한번 언급하지만 실행될 때가 아니고 함수가 만들어질 때다. 위 예시로 들자면 makeCounter가 실행되면 counter 함수는 만들어지기만 한 상태이다. 이 때 이미 외부 렉시컬 환경 즉 makeCounter의 렉시컬 환경에 대한 참조를 `counter.[[Enviroment]]` 프로퍼티에 저장한 것이다. 그리고 counter 함수가 나중에 호출될 때, 이 때 비로소 counter 함수의 렉시컬 환경 객체가 생성되고, 이 객체가 외부 렉시컬 환경에 대한 참조를 `counter.[[Enviroment]]` 프로퍼티로부터 가져온다. 그렇게 해서 이 counter함수가 언제 어디서 실행되든 이미 만들어질 때 makeCounter의 렉시컬 환경에 대한 참조를 저장했으므로 count 변수를 참조할 수 있다. 그리고 이런 것을 `클로저`라고 한다.

정리해서 말하자면 **클로저란 외부 변수를 기억하고 접근할 수 있는 함수를 말한다.** 그리고 자바스크립트에서는 사실 모든 함수가 클로저인 셈이다.





참고링크: [[JavaScript\] 렉시컬 환경 (tistory.com)](https://developer-alle.tistory.com/407)