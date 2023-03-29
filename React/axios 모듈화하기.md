# React에서 axios 모듈화하기 🎶

안녕하세요! 오늘은 **React에서 axios 모듈화 하기**라는 주제로 글을 작성 해보도록 하겠습니다. **axios**는 흔히 자바스크립트에서 **서버 통신 작업**을 진행할 때 널리 쓰이고 있는 라이브러리 인데요, 이 라이브러리를 좀 더 효율적으로 쓰는법을 알아보겠습니다.

<br>

## 1. 일반적인 axios 사용 😒

일반적으로, **글 작성하기**라는 api를 사용할 때, 일반적인 axios 활용 코드는 아래와 같습니다.

```typescript
import axios from 'axios';
import cookies from 'js-cookie';

const SERVER = 'http://localhost:8080/api/v1';

const requestPost = async (postDto) => {
  const res = await axios.get(`${SERVER}/write-post`, postDto, {
    headers: {
      access_token: cookies.get('access_token'),
    },
  });
}
```

만약 기능을 **위처럼** 구현한다고 가정하면, **일일히 headers에 토큰을 넣는 코드를 작성하고, 기본 서버 URL을 계속해서 작성하는 코드를 넣게 됩니다.**
그런데 이 작업들을 일일히 하지 않고, 자동으로 값이 삽입이 된다면 어떨까요?

**그래서 저희는 이 axios를 커스텀하여 사용해보도록 하겠습니다.**

<br>

## 2. customAxios.ts 파일 생성하기 💽

가장 먼저 파일을 생성해보도록 하겠습니다. 저는 **src/lib** 경로에 **customAxios.ts**라는 파일을 생성하겠습니다. 이 파일에는 **axios 인스턴스**를 생성해주도록 할거에요.

> **참고 문서: [https://xn--xy1bk56a.run/axios/guide/api.html#http-%EB%A9%94%EC%84%9C%EB%93%9C-%EB%B3%84%EC%B9%AD](https://xn--xy1bk56a.run/axios/guide/api.html#http-메서드-별칭)**

**customAxios** 파일에 아래의 코드를 추가하도록 하겠습니다.

```typescript
import axios, { AxiosInstance } from 'axios';
import cookies from 'js-cookie';

export const customAxios: AxiosInstance = axios.create({
  baseURL: `${SERVER_ADDRESS}`, // 기본 서버 주소 입력
  headers: {
    access_token: cookies.get('access_token'),
  },
});
```

위의 **axios.create** 함수 안에 매개변수로 넘겨진 **baseURL**과 **headers** 객체는 무엇을 의미하는 걸까요?
**baseURL**은 서버의 기본 URL을 의미하며, **headers**에는 자신이 매번 전달해야하는 객체 (예: 사용자 토큰)를 넣어주시면 자동으로 삽입이 됩니다.

해당 customAxios를 **export**를 하였으니, 이제 직접 사용해보도록 하겠습니다.

<br>

## 3. customAxios 활용하기 🎶

1번 주제에서 구현하였던 **글 작성하기 API 활용** 기능을 customAxios를 사용하여 구현해보도록 하겠습니다. 코드는 아래와 같습니다.

```typescript
import { customAxios } from 'lib/customAxios';

const requestPost = async (postDto) => {
  const res = await customAxios.post('/write-post', postDto);
}
```

위의 일반적인 axios 코드와 비교하여 어떤 느낌이 드시나요? **URL 경로에는 baseURL의 뒷부분만 삽입을 해도 되며, headers에는 일일히 토큰을 넣어주지 않아도 됩니다.**

**저는 위의 두가지 장점이 axios를 커스텀하여 사용하는데 가장 큰 이유가 되었던 것 같습니다.**

<br>

<br>

<br>

### 참고링크: [React에서 axios 모듈화 하기 🎶 (velog.io)](https://velog.io/@yiyb0603/React에서-axios-커스텀하기)