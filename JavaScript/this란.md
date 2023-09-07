# this

JavaScript에서 **함수의 `this` 키워드**는 다른 언어와 조금 다르게 동작합니다. 또한 [엄격 모드](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Strict_mode)와 비엄격 모드에서도 일부 차이가 있습니다.

대부분의 경우 `this`의 값은 함수를 호출한 방법에 의해 결정됩니다. 실행중에는 할당으로 설정할 수 없고 함수를 호출할 때 마다 다를 수 있습니다. ES5는 [`함수를 어떻게 호출했는지 상관하지 않고 this 값을 설정할 수 있는`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this) [`bind`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) 메서드를 도입했고, ES2015는 스스로의 `this` 바인딩을 제공하지 않는 [화살표 함수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Arrow_functions)를 추가했습니다(이는 렉시컬 컨텍스트안의 `this`값을 유지합니다).





출처: [this - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this)

참고링크: [개발자 면접 단골질문 자바스크립트 this - YouTube](https://www.youtube.com/watch?v=tDZROpAdJ9w&list=WL&index=30&t=2s)

[JavaScript] this의 모든 것 : 예제로 살펴보기 - https://paperblock.tistory.com/44
