## 🚲 Suspense란?

## React.Suspense

Suspense는 아직 렌더링이 준비되지 않은 컴포넌트가 있을때 로딩 화면을 보여주고 로딩이 완료되면 해당 컴포넌트를 보여주는 React에 내장되어 있는 기능이다.

[리액트 공식문서](https://ko.reactjs.org/docs/react-api.html#reactsuspense)

### 왜 사용하는가?

#### React.lazy와 함께 사용

SPA(Single-Page-Application)의 단점은 한번에 사용하지 않는 모든 컴포넌트까지 불러오기 때문에 첫 화면이 렌더링 될때까지의 시간이 오래걸리는 것이다. React는 lazy를 통해 컴포넌트를 동적으로 import를 할 수 있기 때문에 이를 사용하면 초기 렌더링 지연시간을 어느정도 줄일 수 있다.
*(이 방법도 한계가 있기 때문에 결국 애플리케이션의 크기가 커지게 되면 SSR 방식을 사용하는 것이 필연적이라고 생각한다.)*

```js
const SomeComponent = React.lazy(() => import('./SomeComponent'));
```

Router로 분기가 나누어진 컴포넌트들을 위 코드처럼 lazy를 통해 import하면 해당 path로 이동할때 컴포넌트를 불러오게 되는데 이 과정에서 로딩하는 시간이 생기게 된다. **이 로딩되는 시간동안 로딩 화면을 보여지도록 해주는 역할**을 하는 것이 바로 **Suspense** 이다.

#### Data-fetching

React를 사용할때 로딩 화면을 사용하는 경우를 생각해보면 비동기 네트워크 요청을 통해 데이터를 받아와서 화면에 보여지도록 하는 과정에서 사용하고 특히 처음에 컴포넌트가 렌더링 되는 과정에서 자주 사용한다.

```js
function ProfilePage() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser().then(u => setUser(u));
  }, []);

  if (user === null) {
    return <p>Loading profile...</p>;
  }
  return (
    <>
      <h1>{user.name}</h1>
      <ProfileTimeline />
    </>
  );
}

function ProfileTimeline() {
  const [posts, setPosts] = useState(null);

  useEffect(() => {
    fetchPosts().then(p => setPosts(p));
  }, []);

  if (posts === null) {
    return <h2>Loading posts...</h2>;
  }
  return (
    <ul>
      {posts.map(post => (
        <li key={post.id}>{post.text}</li>
      ))}
    </ul>
  );
}
```

위 코드처럼 `useEffect`를 사용하여 data fetching 과정을 거치고 로딩 여부를 나타내는 `state`를 사용하여 데이터를 불러오는 동안 로딩 화면을 보여지도록 설정한다. 당연하게 사용했던 방식이지만, 컴포넌트가 마운트 된 이후에 data fetching이 시작된다. 만약 위와 같은 컴포넌트 내부에 같은 형태의 컴포넌트가 존재한다면 데이터를 불러오는 시간이 그만큼 더 길어지게 된다.

data fetching 과정이 이루어지고 컴포넌트가 마운트 되도록 하고 그 시간동안 로딩 화면을 보여주도록 Suspense를 활용할 수 있다.

## Router 적용

```js
import React, { Suspense, lazy } from 'react';
import { Routes, Route } from 'react-router-dom';
import Spinner from './items/Spinner'
//import Login from './pages/Login';
//import Main from './pages/Main';
//import Search from './pages/Search';
//import Setting from './pages/Setting';
const Main = lazy(() => import('./pages/Main'));
const Login = lazy(() => import('./pages/Login'));
const Search = lazy(() => import('./pages/Search'));
const Setting = lazy(() => import('./pages/Setting'));

function App() {

  return (
    <div>
    	<Suspense fallback={<Spinner text='페이지를 불러오는'/>}>
          <Routes>
            <Route exact path='/' component={Main} />
            <Route path='/login' component={Login} />
            <Route path='/setting' component={Setting} />
            <Route path='/search/query=:word' component={Search} />
          </Routes>
		</Suspense>
    </div>
  );
}

export default App;
```

라우터에 Suspense를 적용하는 것은 매우 간단하다. 라우터가 분기되는 컴포넌트에서 각 컴포넌트를 lazy를 사용하여 import하고 Route 컴포넌트들을 Suspense로 감싼 후 로딩 화면으로 사용할 컴포넌트를 fallback 속성으로 설정해주면 된다. 초기 렌더링 시간이 줄어들기는 하지만 페이지를 이동하는 과정이 길어지고 로딩 화면이 보여지기 때문에 서비스에 따라서 적용 여부를 결정하는 것이 좋다.

## data fetching 적용

비동기 네트워크 요청도 Suspense가 알아서 인지해서 로딩 화면을 띄어주면 좋겠지만 이 부분은 자동으로 이루어지지 않는다. 데이터 요청 중인지 완료되었는지를 Suspense가 알 수 있도록 설정을 해주어야 한다.

```js
function wrapPromise(promise) {
  let status = 'pending'
  let response

  const suspender = promise.then(
    (res) => {
      status = 'success'
      response = res
    },
    (err) => {
      status = 'error'
      response = err
    },
  )

  const read = () => {
    switch (status) {
      case 'pending':
        throw suspender
      case 'error':
        throw response
      default:
        return response
    }
  }

  return { read }
}

export default wrapPromise
```

`wrapPromise` 함수는 비동기 요청의 상태를 나타내는 `status` 변수가 pending 일때 `suspender`을 throw하여 Suspense가 로딩 화면을 렌더링하도록 하고 요청이 완료된 이후 응답을 리턴하는 promise를 리턴한다.

```js
import wrapPromise from './wrapPromise'

function fetchData(url) {
  const promise = fetch(url)
    .then((res) => res.json())
    .then((res) => res.data)

  return wrapPromise(promise)
}

export default fetchData
import React, { Suspense } from 'react'
import fetchData from '../api/fetchData'

const resource = fetchData(
  'https://run.mocky.io/v3/d6ac91ac-6dab-4ff0-a08e-9348d7deed51'
)

const UserWelcome = () => {
  const userDetails = resource.read()

  return (
    <div>
      <Suspense fallback={<p>Loading user details...</p>}>
        <p>
          Welcome <span className="user-name">{userDetails.name}</span>, here are
          your Todos for today
        </p>
        <small>Completed todos have a line through them</small>
      </Suspense>
    </div>
  )
}

export default UserWelcome
```

`wrapPromise` 함수 덕분에 Suspense는 데이터가 불러온 이후에 컴포넌트를 렌더링하게 된다. 위 처럼 Suspense에 data fetching 상태를 공유하는 과정이 번거롭기 때문에 리액트 팀에서는 Relay와 같은 프레임워크를 사용하는 것을 추천한다.

## 참고문서

- https://ko.reactjs.org/docs/react-api.html#reactsuspense
- https://17.reactjs.org/docs/concurrent-mode-suspense.html
- https://blog.logrocket.com/async-rendering-react-suspense/



<br>

<br>

#### 참고링크: [[React\] Suspense란? (velog.io)](https://velog.io/@bbaa3218/React-Suspense란)

<br>