220425_basicJavascript TIL~



#### 1. JavaScript에서 표준(standard)가 중요한 이유를 서술하시오.

> 제1차 브라우저 전쟁 이후 수많은 브라우저에서 자체 자바스크립트 언어를 사용하게 됨. 결국 서로 다른 자바스크립트가 만들어지면서 크로스 브라우징 이슈가 발생하여 웹 표준의 필요성이 제기

* 크로스 브라우징(Cross Browsing)
  * W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론 (동일성이 아닌 동등성)
  * 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문

#### 2. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- DOM에서 최상위 객체는 document다.

  => F, DOM에서 최상위 객체는 window이다.

- getElementByld 메서드보다 querySelector 메서드가 좋은 이유는 선택자를 더 유연하게 사용할 수 있기 때문이다.

  => T

- querySelectorAll 메서드를 통해 선택한 NodeList는 forEach 메서드를 사용할 수 있다.

  => T

- document.createElement 메서드를 통해 HTML 요소를 생성할 수 있다.

  => T

- 부모 노드에서 자식 노드를 추가하는 유일한 방법은 append 메서드 뿐이다.

  => F, appendChild 메서드도 존재한다.



