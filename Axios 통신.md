## Axios란?

------

- Axios는 브라우저, Node.js를 위한 Promise API를 활용하는 HTTP 비동기 통신 라이브러리입니다.
- 쉽게 말해서 백엔드랑 프론트엔드랑 통신을 쉽게하기 위해 Ajax와 더불어 사용합니다.
  \- 저는 AJAX보다 AXIOS를 훨씬 많이 사용합니다.

### 브라우저 호환성

| ![img](https://raw.github.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png) | ![img](https://raw.github.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png) | ![img](https://raw.github.com/alrra/browser-logos/master/src/safari/safari_48x48.png) | ![img](https://raw.github.com/alrra/browser-logos/master/src/opera/opera_48x48.png) | ![img](https://raw.github.com/alrra/browser-logos/master/src/edge/edge_48x48.png) | ![img](https://raw.github.com/alrra/browser-logos/master/src/archive/internet-explorer_9-11/internet-explorer_9-11_48x48.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Latest ✔                                                     | Latest ✔                                                     | Latest ✔                                                     | Latest ✔                                                     | Latest ✔                                                     | 11 ✔                                                         |

[![img](https://saucelabs.com/open_sauce/build_matrix/axios.svg)](https://saucelabs.com/u/axios)

### axios 특징

- 운영 환경에 따라 브라우저의 XMLHttpRequest 객체 또는 Node.js의 http api 사용
- Promise(ES6) API 사용
- 요청과 응답 데이터의 변형
- HTTP 요청 취소
- HTTP 요청과 응답을 JSON 형태로 자동 변경

*[HTTP란?](https://developer.mozilla.org/ko/docs/Web/HTTP)*


여럽게 생각하지 마세요. 정말 사용하기 쉽습니다.

# Axios 사용법

------

- Axios 다운로드
- HTTP Methods
- Axios 사용해보기
  - GET
  - POST
  - PUT
  - DELETE
- async await에 관해 살펴보기
- Promise로 Axios사용해보기
- Axios 환경 구성

### Axios다운로드

자신이 사용하는 [패키지 매니저](https://www.opentutorials.org/course/1750/10064#:~:text=package manager. 패키지를 설치,소프트웨어가 패키지 메니저 입니다.)로 프로젝트에 추가해보자!

```null
yarn add axios

npm i axios


Then...

import axios from 'axios'
```

### HTTP Methods

클라이언트가 웹서버에게 사용자 요청의 목적/종류를 알리는 수단

HTTP Methods 중 Axios통신하는데 많이 사용하는 메서드를 정리했습니다!

### GET

------

#### 형태

```null
	axios.get(url,[,config])	
```

> GET : 입력한 url에 존재하는 자원에 요청을 합니다.

🤔 Get이 데이터를 받아오는 것이라고 했는데, 저는 로그인을 구현할때 GET을 사용했는데용?

GET으로 로그인을 구현했을때 웹 사이트 주소창의 형태를 잘 보면 이러한 형태가 나올 것입니다.

```null
	www.yourserver.com/login?id=Hnk&pw=1234
    // 실제로 없는 사이트입니다! 이해를 돕기 위해서 추가했습니다.
```

- 웹 사이트 뒤에 [쿼리스트링](https://ysoh.tistory.com/entry/Query-String)이 붙여진 것을 확인하실 수 있습니다.

✔ GET은 서버에서 어떤 데이터를 가져와서 보여준다거나 하는 용도이다. 주소에 있는 쿼리스트링을 활용해서 정보를 전달하는 것이지 **GET메서드는 값이나 상태등을 바꿀 수 없습니다.**

#### 예제 코드

```null
import axios from 'axios';

axios.get('https://my-json-server.typicode.com/zofqofhtltm8015/fs/user').then((Response)=>{
    console.log(Response.data);
}).catch((Error)=>{
    console.log(Error);
})
```

- [실행중 오류가 나신다면? 클릭해주세요!](https://github.com/zofqofhtltm8015/FrontEnd/tree/master/axios)

```null
[
  { id: 1, pw: '1234', name: 'JUST' },
  { id: 2, pw: '1234', name: 'DO' },
  { id: 3, pw: '1234', name: 'IT' }
]
```

json 형태로 잘 받아온 걸 확인할 수 있습니다.

### POST

#### 형태

```null
	axios.post("url주소",{
    	data객체
    },[,config])
    
```

> ✔새로운 리소스를 생성(create)할 때 사용합니다.

post 메서드의 두 번째 인자는 본문으로 보낼 데이터를 설정한 객체 리터럴을 전달합니다.

🤔 Post는 새로운 리소스를 생성할 때 사용되는데 그러면 언제 POST를 사용하나요?

✔ 로그인, 회원가입 등 사용자가 생성한 파일을 서버에다가 업로드할때 사용합니다. Post를 사용하면 주소창에 쿼리스트링이 남지 않기때문에 👍 GET보다 안전해요!

- Post 예제는 로그인 구현 예제로 할게요!

### Delete

> REST 기반 API 프로그램에서 데이터베이스에 저장되어 있는 내용을 삭제하는 목적으로 사용합니다.

#### 형태

```null
	axios.delete(URL,[,config]);
```

✅ Delete메서드는 HTML Form 태그에서 기본적으로 지원하는 HTTP 메서드가 아닙니다!

Delete메서드는 서버에 있는 데이터베이스의 내용을 삭제하는 것을 주 목적으로 하기에 두 번째 인자를 아예 전달하지 않습니다.

#### 예제 코드

```null
axios.delete("/thisisExample/list/30").then(function(response){
    console.log(response);
      }).catch(function(ex){
      throw new Error(ex)
}
```

### PUT

> REST 기반 API 프로그램에서 데이터베이스에 저장되어 있는 내용을 갱신하는 목적으로 사용됩니다.

#### 형태

```null
	axios.put(url[, data[, config]])
```

✅ PUT메서드는 HTML Form 태그에서 기본적으로 지원하는 HTTP 메서드가 아닙니다!

PUT메서드는 서버에 있는 데이터베이스의 내용을 변경하는 것을 주 목적으로 하고 있습니다.



참고링크: [Axios란? / Axios 사용 및 서버 통신 해보기! (velog.io)](https://velog.io/@zofqofhtltm8015/Axios-사용법-서버-통신-해보기)