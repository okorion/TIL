## SDK와 API에 대해 알아보자

카카오 지도, 카카오 로그인, 음성 그리고 블로그 검색결과 어떤건 api고 어떤건 sdk이다. 안드로이드 앱 개발에서 나는 어떤걸 써야할까? REST API는 또 뭘까? 여태 대충 되는걸 쓰고 넘어갔던 것을 자세히 알아보자!

## API가 무엇일까?

- Application Programing Interface
- 커뮤니케이션에 관한 정의로 다른 앱, 서비스와의 통신을 위한 정의와 프로토콜이 있다.
- 장점
  - 추상화(Abstraction) : 프로세스를 단순화, 복잠한 논리를 다 생각할 필요 없음
  - 표준화 : 정의하는 업계 표준이 있음 (ex. SOAP, GraphQL, REST)

### REST API

- Representational State Transfer
- HTTP URI로 리소스를 표현하고 리소스에 대한 행위를 HTTP Method로 정의하는 방식
- API의 목적이 무엇인지 쉽게 파악이 가능하다.
- request
  - operation (ex. POST, PUT, GET, DELETE)
  - parameters(선택적임)
  - endpoint (/analyze) 가 URL이 된다.
- response
  - json, xml같은 데이터 객체로 추출

### SDK(Software Development Kit)

- 디버거, 프레임워크 등 특정 플랫폼을 위한 소프트웨어 빌딩툴 또는 특정 OS의 코드 라이브러리그룹 같은 개발도구의 집합이다. ex) 안드로이드, iOS SDK등등
- 실제로 api를 호출해주는 메소드를포함 → api request를 직접 쓸 필요가 없음
- response또한 json같은 형태일 필요가 없음 → analyze response object로 받을 수 있음

### SDK와 API의 차이점

- API : 결과를 받아오기 위해 어떤 작업을 수행해야 하는지 알려줄 뿐 받아온 이후의 처리는 개발자의 몫
- SDK : 소프트웨어 개발을 위한 실제 코드까지 있음
- 결국 sdk가 조금 더 크고 편한 도구라고 할 수 있다. (하지만 API가 더 결과를 내밥대로 가공할 수 있는경우도 있을 것이다.)



출처: [SDK와 API가 뭐가 달라? (velog.io)](https://velog.io/@hacha2011/SDK와-API가-뭐가-달라)