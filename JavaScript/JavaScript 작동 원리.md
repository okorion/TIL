### **그렇다면 자바스크립트는?**

 

 지금까지 설명으로 HTML 문서를 파싱 하여 HTML과 CSS를 **렌더링 엔진**에서 처리하는 과정을 알아봤습니다.

위 과정까지 만으로 웹 페이지를 화면에 나타내는 것은 충분합니다. 하지만 Javascript는 어떻게 처리가 될까요? 

 

 Javascript 또한 렌더링 엔진에서 처리가 될까요? **아닙니다.**

 

 자바스크립트는 **자바스크립트 엔진**이 처리합니다. HTML 파서는 `<script>` 태그를 만나면 Javascript 코드를 실행하기 위해 DOM 생성 프로세스를 중지하고 자바스크립트 엔진으로 권한을 넘깁니다. 제어 권한을 넘겨받은 자바스크립트 엔진은 `<script>` 태그 내의 Javascript 코드 또는 `src` 속성에 정의된 Javascript 파일을 로드하고 파싱 하여 실행합니다. Javascript의 실행이 완료되면 다시 HTML 파서로 제어 권한을 넘겨서 중지했던 시점으로 돌아가 DOM 생성을 재개합니다. 

 

![img](https://blog.kakaocdn.net/dn/Ax7cR/btrb1qH7RCh/5P6KFuOtPDeS41cLbalPLk/img.png)브라우저 동작 원리, 출처 =&nbsp;https://poiemaweb.com/js-browser

 

 이처럼 브라우저는 **동기적으로** HTML, CSS, Javascript를 처리합니다. 하지만 자바스크립트 엔진에 제어 권한이 있을 때 Javascript 코드가 완성되지 않은 DOM을 조작하게 된다면 어떻게 될까요? 당연히 에러가 발생할 것입니다. 

이것이 HTML 파일에서 **Javascript 코드를 `<body>`\**태그\** 하단에 위치시키는 이유**입니다.



참고링크: [[CS\] 웹 브라우저는 어떻게 작동하는가? (tistory.com)](https://bbangson.tistory.com/87)