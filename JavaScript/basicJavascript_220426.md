220426 basicJavascript TIL ~



#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- JavaScript에서 함수는 변수에 할당, 인자로 전달할 수 있으나 함수의 결과값으로 반환할 수는 없다.

  => F, **함수는 함수의** 리턴**값**으로 리턴이 가능하다.

- 함수의 매개변수의 개수와 인자의 개수는 반드시 일치하지 않아도 동작한다.

  => T

- 배열에 새로운 요소를 추가하는 메서드는 append다.

  => F, javaScript에서 배열에 새로운 요소를 추가하는 것은 push() 메서드이다.

- JSON 데이터는 바로 객체처럼 key 접근이 가능하다.

  => T

- 화살표 함수와 function 키워드로 선언한 함수는 차이가 없다.

  => F, **일반 함수**는 **함수가 어떻게 호출되었는지에 따라 this에 바인딩할 객체가 동적으로 결정**되고, **화살표 함수**는 **언제나 상위 스코프의 this를 가리킨다.**



#### 2. 다음의 Array Helper Method의 동작을 간략히 서술하시오.

> forEach, map, filter, find, every, some, reduce

* forEach: 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
* map: 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
* filter: 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
* find: 콜백 함수의 반환 값이 참이면 해당 요소를 반환
* every: 배열의 모든 요소가 판별 함수를 통과하면 참을 반환
* some: 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환
* reduce: 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

