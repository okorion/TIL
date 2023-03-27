# [REST API] LogIn GET vs POST



로그인을 하게 되면 아이디와 비밀번호를 입력하고 요청을 보내면 사용자를 식별할 수 있는 응답을 받아 메인페이지에 진입하게 된다.

여기에서 log in 요청 시 URL에 아이디와 비밀번호를 담아 GET요청을 해야하는지 request body에 아이디와 비밀번호를 담아 POST요청을 해야하는지에 대해 의문이 생겼다.
Database에 정보를 생성하지 않고 사용자 식별 정보를 가져오기 때문에 GET인 것 같기도 하지만 request body에 정보를 담을 수 없기 때문에 URL에 아이디와 비밀번호를 담아서 요청을 보내야하는데 이는 보안상 취약하게 느껴져 POST로 처리를 해야하는지 정확하게 판단하기가 어려움을 느꼈다.

<br>

그렇다면 구글링을 통해 참고문서를 찾아 공부를 해보도록 하자.

찾은 참고문서
https://stackoverflow.com/questions/43965316/for-login-get-or-post

참고문서에 따라 결론부터 말하면 GET과 POST 중에서는 POST가 나음. 하지만 바람직한 건 SSL(HTTPS)이다.
우선 둘 중 POST가 나은 이유를 말하자면 GET 요청은 서버 데이터의 상태를 변경하지 않기 때문에 쿼리를 적극적으로 캐싱할 수 있어 아이디와 비밀번호와 같은 정보를 쿼리에 담아 보내게 되면 보안에 취약할 수 있기 때문이다.(다음페이지가 로딩되거나 다른페이지로 이동할때까지 로그파일이나 사용자 브라우저에 일반텍스트로 표시됨)
반면, POST는 서버의 상태를 변경시키고 동일한 응답을 주며 서버를 동일한 상태로 유지하기위해 캐싱을 하지 않기 때문에 GET보다는 보안에 용이할 수 있다.

<br>예를 들면 5번의 로그인에 실패했을 때 6번째 요청은 "당신의 IP는 30분동안 차단되었습니다." 라고 응답할 수 있다.
하지만 가장 좋은 방법은 SSL(https)로 처리하는 방법이다.

https://stackoverflow.com/questions/5868786/what-method-should-i-use-for-a-login-authentication-request
여기에서 비슷한 이유로 logout을 할 때 GET 요청과 POST 또는 DELETE 요청을 하는 것 중 어떤 것을 사용해야하느지에 대한 논쟁을 보았다. session을 삭제할 뿐 정보의 변경은 없다는 주장의 GET 사용 RESTful한 요청은 DELETE요청(session을 삭제하므로)라는 주장들이 보였다.
내가 생각하는 점은 REST API에 꼭 맞는 API설계도 중요하지만 보안의 용이함과 사용자의 편의성 등 여러가지를 고려해 결정하는 것이 맞지않을까라는 생각을 했다.

<br>

### 참고링크: [[REST API\] LogIn GET vs POST (velog.io)](https://velog.io/@jch9537/REST-API-LogIn-GET-vs-POST)

<br>

<br>

<br>

# 로그인, 로그아웃에는 무슨 HTTP 메소드를 써야할까?

2022. 4. 6. 15:06

일단 먼저 HTTP에 대해 간단하게 보자.

<br>

## [HTTP 메소드 종류](https://ssdragon.tistory.com/92#HTTP%--%EB%A-%--%EC%--%-C%EB%--%-C%--%EC%A-%--%EB%A-%--)

1. GET : 리소스 조회

- 서버에 전달하고 싶은 데이터는 query(쿼리 파라미터, 쿼리 스트링)으로 전달
- 메시지 바디를 사용할 순 있지만, 지원하지 않는 곳도 많아서 권장X
- POST : 요청 데이터 처리, 주로 등록에 사용

- 메시지 바디를 통해 서버로 요청 데이터 전달
- 메시지 바디를 통해 들어온 데이터를 처리하는 모든 기능 수행 (만능)
- 주로 전달된 데이터로 신규 리소스 등록, 프로세스 처리에 사용됨
- PUT : 리소스를 전부 교체할 때

- 리소스를 대체하고, 없으면 생성 (새로운 것으로 덮는다)
- 클라이언트가 리소스를 식별하여, 리소스 위치를 알고 URI 지정 (POST와 차이점)
- PATCH : 리소스 부분 변경 (리소스가 존재해야함.)
- DELETE : 리소스 삭제

 

<br>

![img](https://blog.kakaocdn.net/dn/Pm6pB/btryyfLxRfh/SywriVtyng4vGzvSbTenpk/img.png)https://ko.wikipedia.org/wiki/HTTP

<br>

 

 

 

## [클라이언트에서 서버로 데이터 전송 방법](https://ssdragon.tistory.com/92#%ED%--%B-%EB%-D%BC%EC%-D%B-%EC%--%B-%ED%-A%B-%EC%--%--%EC%--%-C%--%EC%--%-C%EB%B-%--%EB%A-%-C%--%EB%-D%B-%EC%-D%B-%ED%--%B-%--%EC%A-%--%EC%--%A-%--%EB%B-%A-%EB%B-%--)

1. 쿼리 파라미터를 통한 데이터 전송 (GET)
2. 메시지 바디를 통한 데이터 전송 (POST, PUT, PATCH)

 <br>

 

 

## [HTTP API 설계 예시](https://ssdragon.tistory.com/92#HTTP%--API%--%EC%--%A-%EA%B-%--%--%EC%--%--%EC%-B%-C)

- 회원 목록 /members → **GET**
- 회원 등록 /members → **POST**
- 회원 조회 /members/{id} → **GET**
- 회원 수정 /members/{id} → **PATCH**, **PUT**, **POST**
- 회원 삭제 /members/{id} → **DELETE**

 <br>

 

 

## [🧐 로그인과 로그아웃 때는 HTTP 메소드 중 무엇을 써서 요청을 보내야 할까?](https://ssdragon.tistory.com/92#%F-%-F%A-%--%--%EB%A-%-C%EA%B-%B-%EC%-D%B-%EA%B-%BC%--%EB%A-%-C%EA%B-%B-%EC%--%--%EC%-B%--%--%EB%--%-C%EB%-A%--%--HTTP%--%EB%A-%--%EC%--%-C%EB%--%-C%--%EC%A-%--%--%EB%AC%B-%EC%--%--%EC%-D%--%--%EC%-D%A-%EC%--%-C%--%EC%-A%--%EC%B-%AD%EC%-D%--%--%EB%B-%B-%EB%--%B-%EC%--%BC%--%ED%--%A-%EA%B-%-C%-F)

메서드의 의도와 달리 실제로 그 요청을 받고 동작하는 서버에서는 구현을 다르게 할 수 있다.

하지만 이는 HTTP 메소드의 의도(관례)를 깨트리는 것이라고 볼 수 있다.

결국 HTTP는 클라이언트와 서버 사이의 인터페이스 역할을 하는 것이고, 실제로 구현을 어떻게 할지는 개발자에게 달려있다.

 <br>

HTML FORM 전송은 GET과 POST만 지원한다.

이 때는 메서드의 정의와 꼭 맞게 사용하고 있지 않게 된다.

GET이든 POST이든 HTTP 프로토콜을 사용하면 내부 데이터는 패킷으로 전송되기에 다 노출된다.

결국 HTTPS나 전송 구간간에 암호화를 하는 것이 중요하다.

일부 웹서버나 방화벽에서 PUT, DELETE, HEAD 등 메서드를 허용하지 않을 수 있다.

API 서버를 제작할 때도 그렇고, 보통 GET과 POST만 허용하도록 만드는 경우가 있다.

 <br>

[Spring Security문서](https://docs.spring.io/spring-security/reference/)에서는 GET이 CSRF 공격에 취약하기에 POST 요청이 선호된다고 명시되어 있다.

따라서 로그인 시에는 POST를 써서 ID와 PW가 body에 담겨서 보내지는데 이것을 HTTPS를 적용하면 암호화가 된다.

GET은 모든 사람에게 표시되는 쿼리 스트링으로 URL 요청이 보내지기에 **로그인은 POST를 쓴다.**

Spring Securty는 로그인, 로그아웃 요청이 POST유형이지만, CSRF 보호를 비활성화하면 GET으로 로그아웃 요청을 사용할 수 있다.

 <br>

현재 프로젝트에서는 로그인을 Access Token과 Refresh Token이라는 토큰 인증 방식을 사용한다.

Refresh Token을 쿠키에 저장하여 로그인을 유지하는데 **httpOnly를 사용하여 서버에서만 쿠키를 재설정**할 수 있다.

이 때는 사용자가 직접 수동으로 지우는 것 외에는 서버에서 삭제하여 로그아웃을 할 수 밖에 없다.

즉, **로그아웃을 하려면 서버에 HTTP 요청을 보내야 한다.**

 <br>

StackOverFlow 등에서 여러 글들을 찾아보았는데 GET일 때는 prefetch로 인한 GET단점도 존재한다고 한다.

사용자를 위해 Web Acceleration 또는prefetch로 사용자가 클릭할 가능성이 있는 링크를 가정하여 미리 가져와 페이지 로딩 시간을 줄이는 기술이다. 이런 프로세스는 GET 링크가 콘텐츠를 반환하기 위해서지 상태를 변경하기 위한 것이 아니기 때문에 한 것이라고 한다.

이 때 GET으로 로그아웃을 만들어 놓는다면 강제 로그아웃이 될 지도 모른다.

[HTTP/1.1 RFC](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)에서는 **GET메서드는 콘텐츠 반환하는데만 사용**해야하며 사용자는 GET 요청의 부작용에 대해 책임을 질 수 없다고 분명히 명시하고 있다. 그러므로 가능하면 이 권장 사항을 따라야한다.

 <br>

이를 통해 GET 요청 시 상태 저장 부작용은 없어야하고,

브라우저에서 prefetch를 포함하는 프로세스를 실행할 수도 있다.

GET을 통해 로그아웃을 할 때 prefetch 프로세스가 강제로 로그아웃시킬 수 있다.

토큰, 세션 등 StateLess 상태에서도 서버에서 BlackList라든지 사용할 때 서버에 요청해야하므로 **POST를 사용하는 것이 낫다고 본다.**

 <br>

 

## [결론](https://ssdragon.tistory.com/92#%EA%B-%B-%EB%A-%A-)

쿠키 또는 세션을 삭제하기에 정보의 변경이 없다는 GET 사용! (비추천)

쿠키 또는 세션을 삭제하는 의미이기에 RESTful한 요청으로 DELETE 사용!

진정한 의미의 RESTful 요청은 POST 사용!

<br>

### 참고링크: [로그인, 로그아웃에는 무슨 HTTP 메소드를 써야할까? — 꾸준히 성장하는 개발자스토리 (tistory.com)](https://ssdragon.tistory.com/92)

<br>

<br>

<br>

# [Project] login/logout 에는 어떤 HTTP method를 사용해야할까?

<br>

인증을 구현하다가 문득 로그아웃은 어떤 http 메서드를 사용해야하는지에 대해 의문이 들었다.

로그인의 경우 지금까지 자연스럽게 POST 메서드로 요청을 받도록 구현해왔지만, 로그아웃의 경우 GET으로 작성하면서도 맞는건지 확신이 들지 않아서 찾아봤다.

<br>

### 📗 로그인 (Login)

> 결론부터 말하자면, 로그인의 경우 `POST`가 더 나은 방법이라고 할 수 있다.

<br>

*로그인의 경우 비밀번호라는 민감한 정보가 들어있기 때문에, 쿼리 스트링으로 노출되는 GET 방식보다는 POST 방식으로 요청을 보내는 것이 안전하다*

라는 것 정도는 알고 있었다.

더 구체적인 이유를 찾아본 결과,

우선 `GET 요청`은 서버 데이터의 상태를 변경하지 않기 때문에 쿼리를 적극적으로 캐싱할 수 있어 비밀번호와 같은 정보를 쿼리에 담아 보내면 보안에 취약할 수 있다.

반면 `POST 요청`은 서버의 상태를 변경시키고 동일한 응답을 주며, 서버를 동일한 상태로 유지하기위해 캐싱을 하지 않기 때문에 GET보다는 안전하다고 볼 수 있다.

하지만, GET, POST 모두 HTTP protocol을 사용하면 내부 데이터는 패킷으로 전송되기에 다 노출된다.

결국 **`HTTPS`**나 전송 구간에 **암호화를 하는 것이 중요**하다. 로그인 시 POST를 사용하면 body에 담겨서 보내지는데 이것을 HTTPS를 적용하면 암호화가 된다.

<br>

### 📕 로그아웃

로그아웃의 경우 POST, GET, DELETE 등 여러가지 의견이 있었지만, 여러 의견을 종합해본 결과 POST를 사용하기로 결정했다.

<br>

#### GET 요청을 사용해도 된다는 입장

GET 요청을 사용해도 된다는 사람들의 입장은 서버 측에 요청할 때 특별한 데이터를 담지 않기 때문에 GET을 사용해도 무방하다는 것이다.

하지만, 아래 자료는 이에 반대하는 입장, 즉 GET을 사용했을 때 나타날 수 있는 부작용에 대해 설명하고 있다.
![img](https://velog.velcdn.com/images/bagt/post/cdbc65e0-8360-41f9-8d06-1aad3b84a56d/image.png)![img](https://velog.velcdn.com/images/bagt/post/8933c11b-2b7a-40cb-926c-d18fc42c6f9b/image.png)

위 글은 서버쪽으로 요청을 보낼 때 특별한 데이터를 담지도 않고, 단순하기 때문에 GET 메서드를 사용할 수도 있고 GET 메서드로 동작할 수도 있지만, **부작용**이 있을 수 있으며, 해당 부작용은 `prefetch`라는 기술과 관련이 있다는 내용이다.

<br>

#### prefetch란?

> 여기서 **`prefetch`**란, 사용자를 위해 GET 링크를 미리 가져와, 사용자가 해당 링크를 클릭했을 때 즉시 제공함으로써 페이지 로딩 시간을 줄이는 프로세스이다.

이때 로그아웃을 GET 요청으로 구현하게 되면, 페이지에서 링크를 미리 가져오려고 시도하는 동안 **실수로 사용자를 로그아웃 시킬 수 있다.**

prefetch와 같은 기술은 `GET 링크가 콘텐츠를 반환하기 위해서 존재한다고 가정하기 때문`이다.

`HTTP/1.1 RFC` 또한 GET 메서드는 **컨텐츠를 반환하는 용도로만 사용**해야 하며 사용자는 GET 요청의 부작용에 대해 책임을 질 수 없다고 분명히 명시하고 있기 때문에, 가능하면 이 권장 사항을 따라야 한다는 것이다.

<br>

### 📚 결론

결론적으로 로그아웃 요청도 서버에 세션/토큰을 처리하는 로그아웃 프로세스를 요청하는 것이므로 **POST** 요청을 사용해야 하며,

<br>

**GET 요청을 사용하면 안되는 이유**는 prefetch와 같은 기술에 영향을 받아 비정상적으로 동작할 수 있으며, GET 요청은 본질적으로 컨텐츠 반환에 사용되어야 하기 때문이다.

> +참고로, `Spring Security`는 **기본적으로** 로그아웃 요청이 POST 메서드여야 하지만, **CSRF 보호를 비활성화하는 경우** GET 메서드로 로그아웃 요청을 사용하도록 할 수 있다.

<br>

### 📃 Reference

- https://stackoverflow.com/questions/3521290/logout-get-or-post
- https://www.baeldung.com/logout-get-vs-post



### 참고링크: [[Project\] login/logout 에는 어떤 HTTP method를 사용해야할까? (velog.io)](https://velog.io/@bagt/HTTP-method-for-loginlogout)

<br>

<br>

<br>

### 🎃 CSRF 공격이란?

CSRF 공격(Cross Site Request Forgery)은 웹 어플리케이션 취약점 중 하나로 인터넷 사용자(희생자)가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격입니다.

<br>

CSRF를 통해 해커는 희생자의 권한을 도용하여 중요 기능을 실행하는 것이 가능합니다. 예를들어, 페이스북에 희생자의 계정으로 광고성 글을 올리는 것이 가능해 집니다. (물론 페이스북은 CSRF 공격에 대해 잘 대응을 하였겠지만, 이번 글에서 피해 서비스 = 페이스북으로 설명하겠습니다.)

조금 더 설명하자면, CSRF는 해커가 사용자의 컴퓨터를 감염시키거나 페이스북 서버를 해킹을 해서 이뤄지는 공격은 아닙니다. 그래서 CSRF 공격이 이뤄지려면 다음 조건이 만족되어야 합니다.

- 위조 요청을 전송하는 서비스(페이스북)에 희생자가 로그인 상태
- 희생자가 해커가 만든 피싱 사이트에 접속

언뜻 보면 이 두 조건을 다 만족하기가 어려울 것 같지만 생각처럼 드문 일은 아닙니다. 예를들어 페이스북, 네이버, 구글 등의 유명 사이트는 보통 PC에서 자동 로그인을 해놓은 경우가 많고 피싱 사이트는 피싱 메일, 음란 사이트(?) 등을 통해 접속될 수 있습니다. 또한 희생자가 해커가 만든 피싱 사이트를 하지 않더라도 해커가 XSS 공격을 성공한 정상 사이트를 통해 CSRF 공격이 수행될 수 도 있습니다.

CSRF가 행해지는 시나리오를 그림으로 그려보면 다음과 같습니다. 이미지는 직접 만들기 귀찮은 관계로 OWASP에 리더로 근무하시는 분의 블로그에서 발췌 하였습니다. (친절하진 않지만 그나마 제일 이해하기 쉬운 이미지인 것 같네요.)

<br>

![img](https://t1.daumcdn.net/cfile/tistory/99FF9D4B5ABE0C4933)

[이미지 출처 : [http://www.bluekaizen.org\]](http://www.bluekaizen.org]/)

<br>

좀 더 이해하기 쉽게 예제 CSRF 공격코드를 살펴보겠습니다. 물론 말도 안되는 이야기지만, 페이스북에 글을 쓸 때 아래 코드와 같은 폼이 전송된다고 예를 듭시다. 피싱 사이트에 똑같이 페이스북에 글쓰기를 요청하는 폼이 숨겨져 있고, 그 내용으로 가입하면 10만원을 준다는 사기성 광고를 본문으로 적혀져 있습니다. 희생자는 피싱 사이트에 접속함으로써 본인의 페이스북 계정으로 해당 글이 등록되게 됩니다.

<br>
<br>

*피싱 사이트에 포함된 코드*

```html
<form action="http://facebook.com/api/content" method="post">
    <input type="hidden" name="body" value="여기 가입하면 돈 10만원 드립니다." />
    <input type="submit" value="Click Me"/>
</form>
```

<br>

위의 공격을 통해 희생자의 페친들은 친구가 올린 글이니 의심없이 속아 넘어갈 수도 있겠죠. 

<br>

<br>

### 참고링크: [CSRF 공격이란? 그리고 CSRF 방어 방법 (itstory.tk)](https://itstory.tk/entry/CSRF-공격이란-그리고-CSRF-방어-방법)