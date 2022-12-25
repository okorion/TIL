### SPA와 MPA란?
- SPA(Single Page Application)는 한 개(Single)의 Page로 구성된 Application이다.
  MPA(Multiple Page Application)는 여러 개(Single)의 Page로 구성된 Application이다.
- MPA는 새로운 페이지를 요청할 때마다 정적 리소스가 다운로드된다. 매번 전체 페이지가 다시 렌더링 된다.
  반면 SPA는 웹 에플리케이션에 필요한 모든 정적 리소스를 최초 한 번에 다운로드한다.
  그 이후 새로운 페이지 요청이 있을 때, 페이지 갱신에 필요한 데이터만 전달 받아서 페이지를 갱신한다.
- 그래서 SPA를 CSR(Client Side Rendering) 방식으로 렌더링한다고 말한다.
  그래서 MPA를 SSR(Server Side Rendering) 방식으로 렌더링한다고 말한다.

#### **MPA(Multiple Page Application)**

- 여러 개(Single)의 Page로 구성된 Application이다.
- MPA는 SSR(Server Side Application) 방식으로 렌더링한다.
  새로운 페이지를 요청할 때마다 서버에서 렌더링된 정적 리소스(HTML, CSS, JavaScript)가 다운로드된다.
  페이지 이동하거나 새로고침하면 전체 페이지를 다시 렌더링한다.

[![MPA](https://i0.wp.com/hanamon.kr/wp-content/uploads/2021/03/MPA.png?resize=601%2C324&ssl=1)](https://hanamon.kr/spa-vs-mpa와-ssr-vs-csr-정리/mpa/)

##### 👍 **MPA 장점**

1. SEO 관점에서 유리하다.
   - MPA는 완성된 형태의 HTML 파일을 서버로부터 전달받는다.
     따라서 검색엔진이 페이지를 크롤링하기에 적합하다.

1. 첫 로딩 매우 짧다.

- - 서버에서 이미 렌더링해 가져오기 때문이다.
  - 그러나 클라이언트가 JS 파일을 모두 다운로드하고 적용하기전 까지는 각각의 기능은 동작하지않는다.

##### 👎 **MPA 단점**

1. 새로운 페이지를 이동하면 ‘깜빡’인다. (UX)
   - 매 페이지 요청마다 리로딩(새로고침) 발생.
     새로운 페이지를 요청할 때마다 전체 페이지를 다시 렌더링하기 때문이다.
2. 페이지 이동시 불필요한 템플릿도 중복해서 로딩 (성능)
3. 서버 렌더링에 따른 부하
4. 모바일 앱 개발시 추가적인 백엔드 작업 필요 (생산성)개발이 복잡해질 수 있다.

#### **SPA(Single Page Application)**

- 한 개(Single)의 Page로 구성된 Application이다.
- SPA는 CSR(Client Side Rendering) 방식으로 렌더링한다.
- 단 한 번만 리소스(HTML, CSS, JavaScript)를 로딩한다.
  그 후에는 데이터를 받아올 때만 서버와 통신한다.
- 즉, 첫 요청시 딱 한 페이지만 불러오고 페이지 이동 시 기존 페이지의 내부를 수정해서 보여주는 방식이다.
- 이를 클라이언트 관점에서 말하자면 최초 페이지를 로딩한 시점부터는 페이지 리로딩 없이 필요한 부분만 서버로 부터 받아서 화면을 갱신하는 것이다.
  필요한 부분만 갱신하기 때문에 네이티브 앱에 가까운 자연스러운 페이지 이동과 사용자 경험(UX)을 제공할 수 있다.
- Angular, React, Vue 등 프론트엔드 기술들이 나오면서 크게 유행하고 있다.

[![SPA](https://i0.wp.com/hanamon.kr/wp-content/uploads/2021/03/SPA.png?resize=600%2C324&ssl=1)](https://hanamon.kr/spa-vs-mpa와-ssr-vs-csr-정리/spa/)

- 그런데 CSR 방식으로 만든 SPA 앱은 검색엔진최적화(SEO)가 어렵다.
  일반적인 SPA 앱을 검색로봇 입장에서 보면 모든 페이지의 소스가 아래와 같이 보이다.
  검색엔진이 색인을 할 만한 컨텐츠가 존재하지 않는 것이다.

```
<html>
<head>
  <title>Single Page Application</title>
  <link rel="stylesheet" href="app.css" type="text/css">
</head>
<body>
  <div id="app"></div>
  <script src="app.js"></script>
</body>
</html>
```



##### 👍 **SPA 장점**

1. 자연스러운 사용자 경험 (UX)
   - 전체 페이지를 업데이트 할 필요가 없기 때문에 빠르고 ‘깜빡’ 거림이 없다.
2. 필요한 리소스만 부분적으로 로딩 (성능)
   - SPA의 Application은 서버에게 정적리소스를 한 번만 요청한다.그리고 받은 데이터는 전부 저장해놓는다. (캐시=Cache)
3. 서버의 템플릿 연산을 클라이언트로 분산 (성능)
4. 컴포넌트별 개발 용이 (생산성)
5. 모바일 앱 개발을 염두에 둔다면 동일한 API를 사용하도록 설계 가능 (생산성)

##### 👎 **SPA 단점**

1. JavaScript 파일을 번들링해서 한 번에 받기 때문에 초기 구동 속도가 느리다. (Webpack의 code splitting으로 해결 가능)
2. 검색엔진최적화(SEO)가 어려움 (SSR로 해결 가능)
3. 보안 이슈 (프론트엔드에 비즈니스 로직 최소화)
   - SSR에서는 사용자에 대한 정보를 서버측에서 세션으로 관리를 하지만 CSR 방식에서는 클라이언트측의 쿠키말고는 사용자에 대한 정보를 저장할 공간이 마땅치 않다.

##### ⚠️ **주의점**

- SPA 방식이 모두 CSR인 것은 아니다. => SPA를 SSR 방식으로 렌더링 할 수도 있다

예: React의 Next.js, Vue의 Nuxt.js



출처: [SPA vs MPA와 SSR vs CSR 장단점 뜻정리 - 하나몬 (hanamon.kr)](https://hanamon.kr/spa-mpa-ssr-csr-장단점-뜻정리/)



### CSR과 SSR의 차이, SSR이 검색엔진최적화(SEO)에 좋은 이유

 React나 Vue, Angular 같이 SPA 방식으로 개발하는 경우 여러가지 장점이 많지만, SEO(검색엔진최적화)가 잘 되지 않는다는 단점이 있습니다. 그렇기때문에 사용자들에게 정보제공을 하고 유입을 증가시켜야 할 경우 SPA방식이 불리할 수가 있는데요. 하지만 SSR(Server Side Rendering)방식으로 개발을 할 경우 SEO와 SPA 두마리 토끼를 다 잡을 수 있습니다!

 React의 경우를 예로 CSR과 SSR의 차이를 비교해보겠습니다. React를 서버사이드에서 렌더링 하고 싶은 경우 사용해야 하는 프레임워크로 대표적으로는 Next.js가 있습니다. (Vue의 경우 Nuxt.js가 있습니다.) 
우선 Next.js를 사용하지 않고 그냥 React로 클라이언트 사이드에서 렌더링(CSR)을 했을 경우에 어떤 방식으로 브라우저가 작동하는지 보겠습니다.



![img](https://blog.kakaocdn.net/dn/cIveuZ/btrwpuX65n1/3Ic7cHfjKWILfI0Sm57LqK/img.png)react(CSR)



 사용자가 www.react로 만들어진app.com에 접속을 했습니다. 그러면 해당 서버에서 그에 맞는 소스코드를 클라이언트에게 주어야겠죠. 그런데 서버는 <div id="root"></div>라는 빈 html코드와 <script>소스만을 줍니다. 그럼 해당 소스코드를 받은 클라이언트에서는 <script>를 읽으면서 react.js를 다운받고, 다운받아진 react.js가 reactDOM.render()을 통해 html을 렌더링 하게 됩니다. 그게 리액트를 사용해보신 분들은 아는 index.js의 이 부분입니다.



![img](https://blog.kakaocdn.net/dn/yitvD/btrwA5BYmXb/u6k4xT69vPNnxVbMwiLviK/img.png)React의 index.js



 id="root"에 html을 렌더링하고 있죠. 그리고 만들어진 js 부분을 만들어진 <html>에 연결시키면, 우리가 아는 React앱이 완성이 됩니다.
그럼 Next.js를 이용해 서버사이드 렌더링을 했을 경우엔 어떻게 동작될까요?



![img](https://blog.kakaocdn.net/dn/bBcyU2/btrwAYW83FY/r5gpIfH37v20Ilcbx7RsC0/img.png)next.js(SSR)



 사용자가 www.next로 만들어진app.com에 접속을 했습니다. 그러면 서버에서 react가 동작해서 서버에서 html코드를 만들어서 이미 완성된 <html>과 <script>를 클라이언트로 보내줍니다. 그럼 클라이언트쪽에서는 완성된 <html>에 <script>를 연결시켜주기만 하면 우리가 아는 Next.js앱이 완성이 됩니다. 이러한 방식을 사용하면 검색엔진들이 이미 서버쪽에서 만들어진 html을 크롤링 할 수 있기 때문에 좀 더 검색에 유리해지게됩니다.



출처: [CSR과 SSR의 차이, SSR이 검색엔진최적화(SEO)에 좋은 이유 (tistory.com)](https://imagineu.tistory.com/57)





### 💯 추가 계층구조, SPA, MPA 설명

![img](https://blog.kakaocdn.net/dn/cwDgWz/btqKSXeznWm/Ili8uo7W4mNdDZ1tICjOY1/img.png)SPA vs MPA



당신이 웹 퍼블리셔, 프론트엔드 개발자가 아니더라도 웹 개발 분야에 있다면 **SPA (Single Page Application)** 혹은 **MPA (Multi Page Application)**에 대해서 들어본 적이 있을 거다. 처음 들어본다고? 괜찮다. SPA, MPA가 무엇인지 소개할 예정이다. 들어가기 전에 앞서 선행학습으로, 지겨운 방법론 두 가지를 짚고 넘어가고자 한다.

 

### **2계층 구조 (2 Tier Architecture Structure)**



![img](https://blog.kakaocdn.net/dn/Ta71B/btqKXiPwF1R/mdqK4LTNPRcaukhENgqwc0/img.png)2계층 구조



과거 대부분의 웹사이트는 2계층 구조로 개발되어있다. 2계층 구조란, 화면이 보여지는 클라이언트(Client)와 데이터베이스(DB)가 물리적으로 분리되어 있는 것을 뜻하며, 클라이언트에는 UI (User Interface)와 비즈니스 로직Business Logic이 함께 있는 구조다.

 

비교적 쉽고 빠르게 개발할 수 있고, 애플리케이션 구조가 단순하여 초기 서비스나 웹사이트들이 많이 사용하는 구조다. 다만 클라이언트 속도 문제, 비즈니스가 복잡해지거나 비대해지면 관리하기가 어려워져서 차후에 3계층, 혹은 N계층 구조로 재설계하여 리뉴얼하기도 한다.

 

### **3계층 구조 (3 Tier Architecture Structure)**



![img](https://blog.kakaocdn.net/dn/cTBrmF/btqKYlE2ZSD/jK9zyDHkFILBIydjo7X001/img.png)3계층 구조



2계층 구조와 3계층 구조의 가장 큰 차이점은 클라이언트 안에 있는 비즈니스 로직이 분리된다는 점이다. 클라이언트는 프레젠테이션, 비즈니스는 애플리케이션이라고 부르기도 한다. 3계층 구조로 설계하게 되면서 클라이언트는 프론트엔드 개발자가, 비즈니스 로직은 백엔드 개발자가 담당하게 되어 역할 분담이 이루어진다.

 

가장 큰 장점으로 UI와 비즈니스 로직이 분리되어 있어 애플리케이션을 배포할 때 UI와 비즈니스 로직을 각각 배포할 수 있다는 점이다.

 

위 구조에 대한 이해를 어느정도 하고 있어야 SPA와 MPA에 대한 이해를 하기 쉬울 것이니, 뭔 말이야 하면서 스크롤을 내렸다면 한 번 읽어볼 것을 권한다.

 

 

### **MPA, Multi Page Application 다중 페이지 응용프로그램**



![img](https://blog.kakaocdn.net/dn/ce63Ro/btqKSWfFgqC/TqXpra61Jk8Kkn5g2kwRPK/img.jpg)MPA 작동 방식



MPA는 전통적인 웹 애플리케이션 개발 방식이다. 이러한 구조는 jsp, 혹은 php 등과 같은 웹 서버 언어로 구축된 웹사이트에서 많이 보인다. 웹 브라우저에서 특정 페이지에 대한 요청을 서버에 보내면, 서버는 데이터를 HTML 문서로 웹 브라우저에 응답해준다. 이 때 전체 페이지가 다시 불러와지면서 화면이 깜빡거리게 된다.

 

이는 웹사이트를 사용하는 유저에게 좋은 사용자 경험을 제공할 수 없다. 페이지 이동 시 잠깐 깜빡이고 페이지가 나온다면 좋겠지만, 데이터가 많을 경우 화면에 다시 그려지는 동안 사용자는 그저 기다려야 하기 때문이다. 한번쯤은 다른 페이지로 넘어갔는데 흰 화면이 계속 나와서 스트레스를 받았던 경험이 있을 거다.

 

AJAX를 이용한 비동기 통신을 통해 상당 부분 해소할 수 있었지만, 근본적으로 페이지가 새로고침 된다는 문제를 해결할 수는 없었다.

 

MPA의 가장 큰 단점은 프론트엔드와 백엔드가 결합되어 있다는 점이다. 이 문제는 2계층 구조에서 비즈니스가 복잡해지거나 비대해지면 관리하기가 어려워진다라는 말과 동일하다는 것을 알 수 있다.

 

단점이 많이 부각되고 있지만 MPA의 가장 큰 장점은 SEO 친화적이다. 네이버나 구글 같은 검색 사이트에 노출되는 것이 중요한 웹사이트라면, MPA 구조로 개발하는 것이 좋다.

 

### **SPA, Single Page Application 단일 페이지 응용 프로그램**



![img](https://blog.kakaocdn.net/dn/zR9q4/btqKZmRfmnr/fef0KBkj2Z3N6rySkLwpjk/img.jpg)SPA 작동 방식



MPA의 단점을 개선해줄 수 있는 것이 바로 SPA다. SPA는 하나의 HTML 파일을 가지고 나머지는 javascript를 이용해서 동적으로 화면을 구성할 수 있다. 서버는 최초 실행 시 HTML 파일을 비롯한 정적 자원을 클라이언트에 보내주며, 이후에는 데이터가 변경되는 부분만 JSON으로 보내 변경될 수 있게 한다.

 

즉, 최초 로딩 때 실행한 HTML 파일에서 변경되지 않는 부분은 그대로 두고 변경되는 부분만 다시 렌더링하여 효율적인 변경이 가능하다는 것인데, 가장 큰 장점이라고 할 수 있다. 특히 새로고침이 되지 않고 변경된다는 점에서 사용자에게 좋은 경험을 제공해줄 수 있다.

 

위 내용만 보면 MPA의 단점을 개선해주고 장점만 있는 것 같지만, 단점도 존재한다. 최초 실행 시 모든 정적 자원을 가져오기 때문에 초기 렌더링 속도가 느리고, SEO에 굉장히 취약하다.





출처: [웹 개발자가 알아두면 좋은 SPA, MPA (tistory.com)](https://seunghyun90.tistory.com/92)
