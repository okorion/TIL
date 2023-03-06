### **1. Origin의 의미**

먼저, CORS에서의 **Origin**이 무엇을 의미하는 건지 짚고 넘어가자. 한국말로는 **'출처'**라고 부르는 것인데, 이는 URL, 도메인 등과 비슷해 보이지만 엄연히 의미가 다르기 때문에 확실히 알고 넘어가야 한다.

 

**Origin은 URL에서 프로토콜, 도메인, 포트 번호를 합친 부분**을 의미한다. 예를 들어, 다음과 같은 URL이 있다고 해보자.

> URL : `https://it-eldorado.com:80/posts/123456?data=789#abc`

 

여기서 프로토콜(Scheme이라고도 함)에 해당하는 부분은 `https://`이고, 도메인에 해당하는 부분은 `it-eldorado.com`이며, 포트 번호에 해당하는 부분은 `:80`이다. 따라서 Origin은 `https://it-eldorado.com:80`이다. 참고로, `window.location.origin` 명령어를 실행하면 현재 접속 중인 웹사이트의 Origin을 알아낼 수 있다.

> Origin : `https://it-eldorado.com:80`

##  

### **2. SOP와 CORS의 관계**

Origin의 의미를 이해했으니, 이제 브라우저의 보안 관련 정책인 **SOP(Same Origin Policy)와 CORS(Cross Origin Resource Sharing)의 관계**를 알아보자. SOP는 한국말로 **'동일 출처 정책'**이라고 부르며, CORS는 **'교차 출처 자원 공유'**라고 부른다. 갑자기 SOP를 소개하는 이유는, SOP가 CORS와 아주 긴밀한 관계를 가지고 있기 때문이다. 둘 간의 관계에 주목하여 설명을 따라가 보자.

 

**SOP(Same Origin Policy)는 다른 Origin으로 요청을 보낼 수 없도록 금지하는 브라우저의 기본적인 보안 정책**이다. 즉, 동일한 Origin으로만 요청을 보낼 수 있게 하는 것이다. 실제로 아주 옛날에는 이것이 절대적인 규칙이었기 때문에, 다른 Origin으로 요청을 보내는 건 애초에 불가능하였다. 그러나 기술이 발달하면서 서로 다른 Origin끼리 데이터를 주고받아야 하는 일이 많아졌고, 이로 인해 SOP는 별도의 예외 사항을 두게 되었다. **즉, 몇 가지 예외 상황에 대해서는 다른 Origin으로도 요청을 보낼 수 있게 하는 것이다.**

 

[**RFC 6454**](https://tools.ietf.org/html/rfc6454#section-3.4.2)에서는 그러한 예외 상황을 다음과 같이 정의하고 있다. (아래에서 설명해줄 것이므로 굳이 읽지 않아도 된다.)

> Generally, reading information from another origin is forbidden. However, an origin is permitted to use some kinds of resources retrieved from other origins. For example, an origin is permitted to **execute script**, **render images**, and **apply style sheets** from any origin. Likewise, an origin can **display content from another origin, such as an HTML document in an HTML frame**. Network resources can also opt into letting other origins read their information, for example, using **Cross-Origin Resource Sharing**.

 

해석해보면, `<script>` 태그로 JavaScript를 실행하는 경우, 이미지를 렌더링 하는 경우, `<link>` 태그로 스타일 시트 파일을 불러오는 경우, HTML 문서를 화면에 보여주는 경우에는 다른 Origin으로의 요청을 허용한다는 내용이다. 그리고 CORS 정책을 지키는 요청의 경우에도 다른 Origin으로의 요청을 허용한다는 내용이 적혀 있는데, 이것이 바로 우리가 주목해야 하는 예외 상황이다.

 

즉, **CORS(Cross Origin Resource Sharing)는 다른 Origin으로 요청을 보내기 위해 지켜야 하는 정책으로, 원래대로라면 SOP에 의해 막히게 될 요청을 풀어주는 정책**이라고 볼 수 있다. 하도 우리를 짜증 나게 해서 요청을 막는 정책인 줄 알았더니, 오히려 요청을 보낼 수 있도록 돕는 정책이었던 것이다.

 

여기서 주목할 만한 점은, **CORS는 '브라우저'의 정책**이라는 것이다. 즉, 서버는 평소처럼 요청이 오면 응답을 해줄 뿐이고, **브라우저가 자신이 보낸 요청 및 서버로부터 받은 응답의 데이터가 CORS 정책을 지키는지 검사하여 안전한 요청을 보낸 건지 검사**하는 것이다. 따라서 서버가 정상적으로 응답을 해줬더라도, 알고 보니 안전한 요청이 아니라고 판단되면 해당 응답을 버린다. 그렇기 때문에 서버 간 통신에서는 이러한 정책이 전혀 적용되지 않는다는 것을 알 수 있다.

> ※ 참고로, 위에서 언급한 예외 상황 중 CORS 요청을 제외한 나머지 경우는 요청 시 `Sec-Fetch-Mode` 헤더의 값을 `no-cors`로 설정한다. 이는 서버가 보내준 응답에 대해 CORS 정책을 검사하지 않게 하는 대신, 해당 응답을 JavaScript 단에서 읽을 수 없도록 한다.

##  

### **3. 자유롭게 다른 Origin으로 요청을 보낼 수 있다면?**

**만약 SOP가 없어서 자유롭게 다른 Origin으로 요청을 보낼 수 있다면 어떻게 될까?** 즉, SOP의 필요성에 대한 본질적인 물음이다. 이 물음에 답하기 위해서는, 다음과 같은 상황을 상상해보면 된다.

> 악의적인 마음을 품은 해커가 자신의 웹사이트를 구축해놓고, 이 웹사이트를 가리키는 링크를 담은 메일을 사용자에게 보내는 것이다. 그리고 이 사용자는 A라는 웹사이트에 로그인이 되어 있어서 브라우저 단에 인증 정보가 존재한다고 해보자. 만약 그 사용자가 실수로 해당 링크를 클릭하여 해커의 웹사이트에 접속하면, 해커가 심어둔 JavaScript 코드가 실행되어 자기도 모르게 A 웹사이트로 개인 정보를 조회하는 API 요청을 보낼 것이다. 이 사용자의 브라우저 단에는 인증 정보가 존재하기 때문에, 이것이 해당 요청에 함께 실어서 전송되면 서버는 인증된 요청이라 생각하여 개인 정보를 응답해줄 것이다. 그러고 나면 그 개인 정보를 해커가 빼돌릴 수 있게 된다. (이것이 바로 [CSRF](https://it-eldorado.tistory.com/10) 공격이다.)

 

그런데 만약 다른 Origin으로의 요청을 막는 정책, 즉 SOP가 존재한다면 이러한 문제를 어느 정도 예방할 수 있다. 해커가 구축한 웹사이트와 A 웹사이트는 당연히 Origin이 다르기 때문에, 해커의 웹사이트에서 A 웹사이트로 API 요청을 보낼 수 없기 때문이다. 따라서 SOP는 브라우저의 아주 기본적인 보안 정책으로서 기능한다.

##  

### **4. CORS 동작 원리 ★★★**

CORS의 기본적인 동작 원리는 단순하다. **브라우저는 다른 Origin으로 요청을 보낼 때 `Origin` 헤더에 자신의 Origin을 설정하고, 서버로부터 응답을 받으면 응답의 `Access-Control-Allow-Origin` 헤더에 설정된 Origin의 목록에 요청의 `Origin` 헤더 값이 포함되는지 검사**하는 것뿐이다. 즉, CORS 요청을 위해서는 서버에서 응답의 `Access-Control-Allow-Origin` 헤더에 허용되는 Origin의 목록 혹은 와일드카드(`*`)를 설정해주면 된다. 이것이 기본적인 CORS 정책이다.

> ※ 와일드카드(*)는 모든 Origin을 허용한다는 것을 의미하는 특수 기호이다.

 

하지만 동작 원리를 조금 더 깊게 들어가면 CORS 요청은 다음과 같이 세 가지 유형으로 나눠서 생각해볼 수 있다.

 

**4-1. 단순 요청 (Simple Request)**

**단순 요청(Simple Request)**은 공식 용어가 아닌, MDN에서 사용한 용어를 가져온 것이다. 그런데 이름이 의미하는 것과 달리, 단순 요청은 흔한 유형의 요청이 아니다. 단순 요청이 되기 위한 조건이 매우 까다롭기 때문이다. [그 조건](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS#단순_요청simple_requests)은 대략 다음과 같다.

> - 메소드가 GET, HEAD, POST 중 하나여야 한다.
> - User Agent가 자동으로 설정한 헤더를 제외하면, 아래와 같은 헤더들만 사용할 수 있다.
>   - Accept
>   - Accept-Language
>   - Content-Language
>   - Content-Type
>   - DPR
>   - Downlink (en-US)
>   - Save-Data
>   - Viewport-Width
>   - Width
> - Content-Type 헤더에는 아래와 같은 값들만 설정할 수 있다.
>   - application/x-www-form-urlencode
>   - multipart/form-data
>   - text/plain
> - . . .

 

위와 같은 조건을 만족하는 단순 요청은 **안전한 요청**으로 취급되어, (뒤에서 설명할) **프리플라이트 요청이 필요 없이 단 한 번의 요청**만을 전송한다. 즉, 위에서 언급한 CORS의 기본적인 동작 원리를 그대로 따른다. 다른 Origin으로 요청을 보낼 때 `Origin` 헤더에 자신의 Origin을 설정하고, 서버로부터 응답을 받으면 응답의 `Access-Control-Allow-Origin` 헤더에 설정된 Origin의 목록에 요청의 `Origin` 헤더 값이 포함되는지 검사하는 것이다. 이를 그림으로 나타내면 다음과 같다.

 



![img](https://blog.kakaocdn.net/dn/qJIWX/btq9uAkfvPp/NP5Zvzmvr7MNdNxmRRkHC0/img.png)[Figure 1] 단순 요청 (Simple Request)



 

**4-2. 프리플라이트 요청 (Preflight Request)**

위에서 소개한 단순 요청의 조건에 벗어나는(= 안전하지 않은) 요청의 경우, 서버에 실제 요청을 보내기 전에 예비 요청에 해당하는 **프리플라이트 요청(Preflight Request)**을 먼저 보내서 실제 요청이 전송하기에 안전한지 확인한다. 만약 안전한 요청이라고 확인이 된다면, 그때서야 실제 요청을 서버에게 보낸다. 따라서 총 두 번의 요청을 전송한다.

 

프리플라이트 요청의 특징은 다음과 같다.

> - 메소드로 OPTIONS를 사용한다.
> - `Origin` 헤더에 자신의 Origin을 설정한다.
> - `Access-Control-Request-Method` 헤더에 실제 요청에 사용할 메소드를 설정한다.
> - `Access-Control-Request-Headers` 헤더에 실제 요청에 사용할 헤더들을 설정한다.

 

서버는 이러한 프리플라이트 요청에 대해 다음과 같은 특징을 가진 응답을 제공해야 한다.

> - `Access-Control-Allow-Origin` 헤더에 허용되는 Origin들의 목록 혹은 와일드카드(`*`)를 설정한다.
> - `Access-Control-Allow-Methods` 헤더에 허용되는 메소드들의 목록 혹은 와일드카드(`*`)를 설정한다.
> - `Access-Control-Allow-Headers` 헤더에 허용되는 헤더들의 목록 혹은 와일드카드(`*`)를 설정한다.
> - `Access-Control-Max-Age` 헤더에 해당 프리플라이트 요청이 브라우저에 캐시 될 수 있는 시간을 초 단위로 설정한다.

 

이러한 응답을 받고 나면 브라우저는 **이 응답의 정보를 자신이 전송한 요청의 정보와 비교하여 실제 요청의 안전성을 검사**한다. 만약 이 안전성 검사에 통과하게 된다면, 그때서야 실제 요청을 서버에게 보낸다. 단, 이때는 `Access-Control-Request-XXX` 형태의 헤더는 보내지 않는다.

 

예를 들어, `Content-Type` 헤더의 값이 `application/json`이고 사용자 정의 헤더로 `Custom-Header`를 사용하는 POST 요청을 서버에게 보내려 한다고 해보자. 그러면 이는 단순 요청의 조건에 벗어나기 때문에 프리플라이트 요청이 필요하다. 따라서 총 두 번의 요청이 서버에게 전송되며, 이를 그림으로 나타내면 다음과 같다.

 



![img](https://blog.kakaocdn.net/dn/pP42w/btq9kPRyADK/xNqcGxeMH1BYv9IWX1WqY1/img.png)[Figure 2] 프리플라이트 요청 (Preflight Request)



 

**4-3. 인증 정보를 포함한 요청 (Credentialed Request)**

위에서 소개한 두 유형의 요청은 인증 정보가 없는 경우였다. 여기서 말하는 인증 정보(Credential)란 쿠키(Cookie) 혹은 Authorization 헤더에 설정하는 토큰 값 등을 일컫는다. 만약 이러한 **인증 정보를 함께 보내야 하는 요청(Credentialed Request)**이라면, 별도로 따라줘야 하는 CORS 정책이 존재한다. 이에 대해 한 번 알아보자.

 

우선, **쿠키 등의 인증 정보를 보내기 위해서는 클라이언트 단에서 요청 시 별도의 설정이 필요**하다. 이는 Ajax 요청을 위해 어떠한 도구를 사용하느냐에 따라 달라진다. 만약 `XMLHttpRequest`, jQuery의 ajax, 또는 `axios`를 사용한다면 `withCredentials` 옵션을 `true`로 설정해줘야 한다. 반면, `fetch` API를 사용한다면 `credentials` 옵션을 `include`로 설정해줘야 한다. 이러한 별도의 설정을 해주지 않으면 쿠키 등의 인증 정보는 절대로 자동으로 서버에게 전송되지 않는다.

 

위와 같은 설정을 통해 인증 정보를 요청에 포함시켰다면, 이 요청은 이제 인증 정보를 포함한 요청이 된다. 그리고 서버는 이러한 요청에 대해 일반적인 CORS 요청과는 다르게 대응해줘야 한다. **응답의 `Access-Control-Allow-Origin` 헤더가 와일드카드(`\*`)가 아닌 분명한 Origin으로 설정되어야 하고, `Access-Control-Allow-Credentials` 헤더는 `true`로 설정되어야 한다.** 그렇지 않으면 브라우저에 의해 응답이 거부된다. 이를 그림으로 나타내면 다음과 같다.

 



![img](https://blog.kakaocdn.net/dn/dc3FOn/btq9pCp5eBt/B1LImhUewiWv9tCiuR2UU1/img.png)[Figure 3] 인증 정보를 포함한 요청 (Credentialed Request)



출처: [[Web\] CORS (Cross Origin Resource Sharing) 이해하기 (tistory.com)](https://it-eldorado.tistory.com/163)