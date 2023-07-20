## 🫐 useEffect 간단한 사용법

![post-thumbnail](https://velog.velcdn.com/images/yeonsubaek/post/25d84862-d32f-431f-a15f-0dbc41a4b617/image.png)



<br>

## 1. useEffect란?

`useEffect`는 리액트 훅으로, 컴포넌트가 렌더링 될 때마다 사이드 이펙트(Side effect)를 실행할 수 있도록 하는 도구이다.

여기서 사이드 이펙트란 렌더링 된 후에 비동기로 처리되어야 하는 효과를 뜻한다.

`useEffect`는 다음과 같은 경우에 사용될 수 있다.

- 백엔드 서버에 http 리퀘스트를 보내기
- 브라우저 저장소에 저장하기
- 타이머나 간격 설정하기



<br>

## 2. 사용법

로그인 창을 구현하는 예시 코드로 사용법을 알아보자.

```jsx
// App.js
import React, { useState } from 'react';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const loginHandler = (email, password) => {
    setIsLoggedIn(true);
  };

  const logoutHandler = () => {
    setIsLoggedIn(false);
  };

  return (
    // 생략...
  );
}
```

![img](https://velog.velcdn.com/images/yeonsubaek/post/255ce5df-f588-4811-a2b0-615f6b1fff11/image.png)

이메일과 비밀번호를 받으면 유효성을 체크한 후 로그인의 성공 여부를 체크한다.

![img](https://velog.velcdn.com/images/yeonsubaek/post/68e5994d-7c30-4bd6-b35a-4023913cd670/image.png)

로그인에 성공하면 화면이 바뀌고, 로그아웃 버튼을 클릭하면 로그인이 풀린다.

여기서 문제점은 새로고침을 한 후에 자동으로 로그아웃이 되는 것이다.
이 문제를 해결하기 위하여 `useEffect`를 사용할 것이다.

<br>

### 1. 로컬 저장소에 정보 저장하기

로그인 여부 데이터는 `setIsLoggedIn`에 저장되어 있다.

```jsx
//생략
function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  const loginHandler = (email, password) => {
    localStorage.setItem('isLoggedIn', 'LOGIN');
    setIsLoggedIn(true);
  };
  //생략
}
```

로그인 버튼을 클릭할 때 실행되는 `loginHandler` 함수에서

```js
localStorage.setItem('isLoggedIn', 'LOGIN');
```

key: `isLoggedIn`, value: `LOGIN` 이라는 상태를 로컬 저장소에 저장한다.

![img](https://velog.velcdn.com/images/yeonsubaek/post/8b642dd9-1763-4a4a-ab4d-2910455f4fc3/image.png)

로그인을 하면 키와 값이 로컬 저장소에 저장된 것을 볼 수 있다.

<br>

### 2. 로컬 저장소의 정보를 가져오기

새로고침을 실행하면 `App` 컴포넌트는 다시 시작된다.

```jsx
//생략
function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const StoredUserLoggedInformation = localStorage.getItem('isLoggedIn');

  if (StoredUserLoggedInformation === 'LOGIN') {
    setIsLoggedIn(true);
  }

  const loginHandler = (email, password) => {
    localStorage.setItem('isLoggedIn', 'LOGIN');
    setIsLoggedIn(true);
  };

  //생략
}
```



<br>로컬 저장소의 키값을 받아와 로그인 상태를 유지시켜야 한다.

```js
const StoredUserLoggedInformation = localStorage.getItem('isLoggedIn');

if (StoredUserLoggedInformation === 'LOGIN') {
  setIsLoggedIn(true);
}
```

`isLoggedIn`의 값을 가져와 로그인 상태가 맞다면 `setIsLoggedIn`을 `true`로 수정한다.

로컬 저장소에서 데이터를 가져오기 때문에 더이상 새로고침을 해도 자동으로 로그아웃 되지 않는다.

**이렇게 끝낸다면 무한 루프를 경험할 수 있다.**

브라우저를 새로고침할 때마다 과정 1번과 2번을 계속해서 반복할 수 밖에 없다.

지금부터 `useEffect`를 사용해 이 단점을 해결해보도록 하자.

<br>

### 3. import하기

```jsx
import React, { useState, useEffect } from 'react';
```

리액트 패키지에서 `useEffect` 라이브러리를 불러온다.

<br>

### 4. useEffect 선언하기

```jsx
function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const StoredUserLoggedInformation = localStorage.getItem('isLoggedIn');

    if (StoredUserLoggedInformation === 'LOGIN') {
      setIsLoggedIn(true);
    }
  }, []);
  // 생략
```

`useEffect` 함수의 매개변수는 다음과 같이 이루어져 있다.

1. 실행될 함수
2. 의존성 배열 *(이것에 대한 자세한 내용은 다음 포스팅에...)*

`useEffect`가 실행되기 위해서 다음 조건을 모두 만족해야 한다.

1. 모든 컴포넌트의 재평가 후에
2. 의존성 배열의 요소들 중 하나라도 변경
   이 경우에는 배열이 비어있기 때문에 무시할 수 있다.
3. 함수 내의 state가 변경



<br>

### 5. 로컬 정보 삭제하기

```jsx
function App() {
// 생략
  const logoutHandler = () => {
    localStorage.removeItem('isLoggedIn');
    setIsLoggedIn(false);
  };
// 생략
```

로그아웃 버튼을 클릭하면 실행되는 `logoutHandler` 함수에서

```js
localStorage.removeItem('isLoggedIn');
```

`isLoggedIn` 키를 삭제하도록 한다.

이제 로그아웃 버튼을 클릭하면 로컬 저장소의 정보가 삭제되고 로그인 창으로 돌아간다.

------

`useEffect`에서 중요하게 다뤄지는 종속성에 대해서는 다음에 포스팅하도록

<br>

<br>

#### 참고링크: [[React\] Hooks - useEffect 간단한 사용법 (velog.io)](https://velog.io/@yeonsubaek/React-Hooks-useEffect-간단한-사용법)

<br>