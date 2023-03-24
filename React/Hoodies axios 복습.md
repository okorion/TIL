### 👨‍🏫 Hoodies axios Study

> ◆ - ◇ - ◇ - ◇   메인 페이지 살펴보기 

```react
// main.js

  useEffect(() => {
    (async () => {
   
      const response = await fetchPreview()   // API 호출!
      const response1 = await fetchPopularview()
      const responseStaffs = await fetchStaffview()

      if (response){
        setArticles(response)

      }
      if (response1){
        setPopularText(response1)

      }
      setStaffs(responseStaffs)
      
      setJobInfo(tempJobInfo)

      
      setIsLoading(false);
      })()
    }, []);  // Dependency Array: useEffect의 두 번째 인자로 사용되며, 배열 안에 들어있는 값이 변경될 때만 해당 함수를 실행할 수 있도록 제어
```

- response가 없는 경우의 예외 처리가 없어서 **Bad**! 🐛

<br>

<br>

> ◇ - ◆ - ◇ - ◇   메인 페이지 API 살펴보기

```react
//mainAPI.js

import axios1 from "../../common/customAxios/customAxios";  // customAxios 사용
import { API_URL } from "../../common/api/url"
/* 
//url.js
export const API_URL = "https://k7a402.p.ssafy.io/api/";
*/

export const fetchPreview = async () => {
    try {
        const response = await axios1.get(API_URL + 'preview/free', {headers: {
                'accessToken': localStorage.getItem('token')   // 로컬 스토리지에서 토큰
            }})
        return response.data
    } catch (err) {
        console.log(err)
    }
}
// API_URL의 반복 => customAxios(axios1)의 baseURL로 다시 설정하는 방법도 OK.
        const response = await axios1.get(API_URL + 'preview/popular', {headers: {
//
        const response = await axios1.get(API_URL + 'preview/mentor', {headers: {       
//

```

- axios에서 에러가 났을 때 예외 처리를 해주기 위해 customAxios 활용.

<br>

- **HTTP header**는 클라이언트와 서버가 요청 또는 응답으로 부가적인 정보를 전송을 할 수 있게 하는 역할!
  - 참고링크: [[HTTP\] 헤더란? 헤더의 역할과 종류 (tistory.com)](https://kawaii-jordy.tistory.com/113)

<br>

<br>

> ◇ - ◇ - ◆ - ◇   메인 페이지 API 살펴보기

```react
//customAxios.js

const axios1 = axios.create({
  baseUrl: "",   // mainAPI.js에서 API_URL의 반복을 줄이기 위해 baseUrl을 설정해줘도 OK. 🦅
});
let isTokenRefreshing = false;
//

axios1.interceptors.response.use(   // axios 인스턴스가 ‘응답을 받은 직후’에 403 Error 발생 시 처리
  (response) => {
    return response;
  },
//
    if (code === 403) {
      if (!isTokenRefreshing) {
        isTokenRefreshing = true;
//
        const token = localStorage.getItem("token");
        axios
          .get(API_URL + "user/reissue", { withCredentials: true })   // withCredentials 옵션을 통해 CORS 해결

//

export default axios1;
```

- **Interceptor**: HTTP 요청과 응답을 가로채는 Axios 기능
  - **Request Interceptor**: Axios 인스턴스가 ‘요청을 보내기 직전’에 가로챔.
  - **Response Interceptor**: Axios 인스턴스가 ‘응답을 받은 직후’에 가로챔.
  - 참고링크: [우리 Axios에게 다시 한 번 기회를 주세요!. 우리가 만든 애플리케이션을 다양한 통신을 주고 받습니다. 데이터베이스와… | by Jake Han | 직방 기술 블로그 | Medium](https://medium.com/zigbang/우리-axios에게-다시-한-번-기회를-주세요-a7b32f4f2db2)

<br>

- **HTTP 403 Error**: 클라이언트에서 유효한 URL에 액세스하는 것이 금지되었다는 뜻입니다. 즉, 서버에서 요청을 이해하지만 클라이언트 측 문제로 인해 요청을 이행할 수 없음.

<br>

- **withCredentials 옵션**은 단어 그대로, 다른 도메인(Cross Origin)에 요청을 보낼 때 요청에 인증(credential) 정보를 담아서 보낼 지를 결정하는 항목
  - **클라이언트나 서버나 둘다 Credentials 부분을 true로 설정**해줘야 한다
  - 참고링크: [[AXIOS\] 📚 CORS 쿠키 전송하기 (withCredentials 옵션) (tistory.com)](https://inpa.tistory.com/entry/AXIOS-📚-CORS-쿠키-전송withCredentials-옵션)

<br>

<br>

> ◇ - ◇ - ◇ - ◆ 

<br>

<br>

### 🏮 프로미스 에러 처리는 가급적 catch()를 사용

 앞에서 프로미스 에러 처리 방법 2가지를 살펴봤습니다. 개개인의 코딩 스타일에 따라서 `then()`의 두 번째 인자로 처리할 수도 있고 `catch()`로 처리할 수도 있겠지만 가급적 `catch()`로 에러를 처리하는 게 더 효율적입니다.

<br>

그 이유는 아래의 코드를 보시면 알 수 있습니다.

```js
// then()의 두 번째 인자로는 감지하지 못하는 오류
function getData() {
  return new Promise(function(resolve, reject) {
    resolve('hi');
  });
}

getData().then(function(result) {
  console.log(result);
  throw new Error("Error in then()"); // Uncaught (in promise) Error: Error in then()
}, function(err) {
  console.log('then error : ', err);
});
JsCopy
```

<br>  `getData()` 함수의 프로미스에서 `resolve()` 메서드를 호출하여 정상적으로 로직을 처리했지만, `then()`의 첫 번째 콜백 함수 내부에서 오류가 나는 경우 오류를 제대로 잡아내지 못합니다. 따라서 코드를 실행하면 아래와 같은 오류가 납니다.

<br>

![img](https://joshua1988.github.io/images/posts/web/javascript/then-not-handling-error.png)

<br>

<'에러를 잡지 못했습니다(Uncaught Error)' 로그>

<br>

하지만 똑같은 오류를 `catch()`로 처리하면 다른 결과가 나옵니다.

```js
// catch()로 오류를 감지하는 코드
function getData() {
  return new Promise(function(resolve, reject) {
    resolve('hi');
  });
}

getData().then(function(result) {
  console.log(result); // hi
  throw new Error("Error in then()");
}).catch(function(err) {
  console.log('then error : ', err); // then error :  Error: Error in then()
});
JsCopy
```

<br>

 위 코드의 처리 결과는 다음과 같습니다.

![img](https://joshua1988.github.io/images/posts/web/javascript/catch-handling-error.png)

<br>

 <발생한 에러를 성공적으로 콘솔에 출력한 모습>

<br>

**따라서, 더 많은 예외 처리 상황을 위해 프로미스의 끝에 가급적 catch()를 붙이시기 바랍니다.**

<br>

<br>

참고링크: [자바스크립트 Promise 쉽게 이해하기 • 캡틴판교 (joshua1988.github.io)](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)

<br>

<br>

### 📳 Routing

```bash
# 전통적 링크 방식
$ npm run link

# ajax 방식
$ npm run ajax

# hash 방식
$ npm run hash

# pjax(pushState + ajax) 방식
$ npm run pjax
```

- **전통적 링크 방식**
  - 각 페이지마다 고유의 URL이 존재하므로 history 관리 및 SEO 대응에 아무런 문제가 없다. 하지만 요청마다 중복된 리소스를 응답받아야 하며 전체 페이지를 다시 렌더링하는 과정에서 새로고침이 발생하여 사용성이 좋지 않은 단점이 있다.

<br>

- ajax 방식
  - ajax 요청은 주소창의 URL을 변경시키지 않는다. 이는 브라우저의 뒤로가기, 앞으로가기 등의 **[history](https://developer.mozilla.org/ko/docs/Web/API/History_API) 관리가 동작하지 않음을 의미한다.** 따라서 history.back(), history.go(n) 등도 동작하지 않는다. 주소창의 URL이 변경되지 않기 때문에 새로고침을 해도 언제나 첫페이지가 다시 로딩된다. 동일한 하나의 URL로 동작하는 ajax 방식은 **SEO 이슈**에서도 자유로울 수 없다.

<br>

- **hash 방식**

  - **URL이 동일한 상태에서 hash만 변경되면 브라우저는 서버에 어떠한 요청도 하지 않는다. 즉, URL의 hash는 변경되어도 서버에 새로운 요청을 보내지 않으며 따라서 페이지가 갱신되지 않는다.** hash는 요청을 위한 것이 아니라 fragment identifier(#service)의 고유 기능인 앵커(anchor)로 웹페이지 내부에서 이동을 위한 것이기 때문이다.
     또한 hash 방식은 서버에 새로운 요청을 보내지 않으며 따라서 페이지가 갱신되지 않지만 페이지마다 고유의 **논리적 URL이 존재하므로 history 관리에 아무런 문제가 없다.**

  -  hash 방식은 url의 hash가 변경하면 발생하는 이벤트인 [hashchange](https://developer.mozilla.org/ko/docs/Web/API/WindowEventHandlers/onhashchange) 이벤트를 사용해 hash의 변경을 감지하고 url의 hash를 취득해 필요한 ajax 요청을 수행한다.

    hash 방식의 단점은 url에 불필요한 #이 들어간다는 것이다. 일반적으로 hash 방식을 사용할 때 #!을 사용하기도 하는데 이를 [해시뱅(Hash-bang)](https://blog.outsider.ne.kr/698)이라고 부른다.

    hash 방식은 과도기적 기술이다. HTML5의 History API인 [pushState](https://developer.mozilla.org/ko/docs/Web/API/History_API)가 모든 브라우저에서 지원이 된다면 해시뱅은 사용하지 않아도 되지만 현재 pushState는 일부의 브라우저(IE 10 이상)에서만 지원이 가능하다.

    또 다른 문제는 **SEO 이슈**이다. [웹 크롤러](https://ko.wikipedia.org/wiki/웹_크롤러)는 검색 엔진이 웹사이트의 콘텐츠를 수집하기 위해 HTTP와 URL 스펙(RFC-2396같은)을 따른다. 이러한 크롤러는 JavaScript를 실행시키지 않기 때문에 hash 방식으로 만들어진 사이트의 콘텐츠를 수집할 수 없다. 구글은 해시뱅을 일반적인 URL로 변경시켜 이 문제를 해결한 것으로 알려져 있지만 다른 검색 엔진은 hash 방식으로 만들어진 사이트의 콘텐츠를 수집할 수 없을 수도 있다.

<br>

- **pjax** **방식**

  - pjax 방식에서 사용하는 history.pushState 메서드는 주소창의 url을 변경하지만 HTTP 요청을 서버로 전송하지는 않는다. 따라서 페이지가 갱신되지 않는다. 하지만 페이지마다 고유의 URL이 존재하므로 history 관리에 아무런 문제가 없다. 또한 hash를 사용하지 않으므로 SEO에도 문제가 없다.

    단, 브라우저의 새로고침 버튼을 클릭하면 브라우저 주소창의 url이 변경되지 않는 ajax 방식과 해시(fragment identifier)만 추가되는 hash 방식은 서버에 별도의 요청을 보내지 않지만 pjax 방식은 브라우저 주소창의 url이 변경되기 때문에 요청(예를 들어 localhost:5004/service)이 서버로 전달된다. 즉, **pjax 방식은 서버 렌더링 방식과 ajax 방식이 혼재되어 있는 방식으로 서버의 지원이 필요하다**

<br>

| 구분             | History 관리 | SEO 대응 | 사용자 경험 | 서버 렌더링 | 구현 난이도 | IE 대응 |
| :--------------- | :----------: | :------: | :---------: | :---------: | :---------: | :-----: |
| 전통적 링크 방식 |      ◯       |    ◯     |      ✗      |      ◯      |    간단     |         |
| ajax 방식        |      ✗       |    ✗     |      ◯      |      ✗      |    보통     | 7 이상  |
| hash 방식        |      ◯       |    ✗     |      ◯      |      ✗      |    보통     | 8 이상  |
| pjax 방식        |      ◯       |    ◯     |      ◯      |      △      |    복잡     | 10 이상 |

<br>

<br>

참고링크: [SPA & Routing | PoiemaWeb](https://poiemaweb.com/js-spa)

<br>