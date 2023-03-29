## 🦯 axios.defaults.baseURL

axios 요청을 보낼 때 아래처럼 **url**을 적어주어야 한다. 그런데 'http://localhost:3065' 부분은 공통이라 계속 적어주어야 한다. 나중에 배포를 하게 되어 url이 바뀌게 되면, 모든 url 부분을 다 바꿔줘야 하는데 굉장히 귀찮은 일이다. 

 <br>

```
function loginAPI(data) {
  return axios.post('http://localhost:3065/user/login', data);
}

function logoutAPI() {
  return axios.post('http://localhost:3065/user/logout');
}

function signUpAPI(data) {
  return axios.post('http://localhost:3065/user', data);
}
```

 <br>

이럴 때, **axios.defaults**를 사용한다. 'axios.defaults'를 통해 모든 요청에 적용될 구성 기본 값을 지정할 수 있다.

 <br>

```
axios.defaults.baseURL = 'https://api.example.com';
axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
```

 <br>

나의 경우는 redux-saga를 사용했기 때문에 saga 폴더의 index.js 파일에서 baseURL을 지정해주었다. 이렇게 해주면, 나중에 배포 후에 baseURL이 변하더라도 이 부분만 변경해주면 된다.

 <br>

```
axios.defaults.baseURL = 'http://localhost:3065';
```

<br>

<br>

<br>

### 참고링크: [[TIL_개발일기_210405\] axios.defaults.baseurl / findOne (tistory.com)](https://dolphinsarah.tistory.com/m/26)