![post-thumbnail](https://velog.velcdn.com/images/kandy1002/post/8202c0c5-71a2-4206-943f-3b31b3d5407b/image.jpeg)

# ⏳ React-Query란?

React-Query, 프론트엔드 공부를 하면서 분명 몇 번 들어본 적도 있고, velog 눈팅하다가 힐끗 본 적도 있는 라이브러리인데…도대체 뭐하는 친구지?? 이번 글을 통해 정확하게 알아보자.

------

👇 공식문서에서는 React-Query를 다음과 같이 설명하고 있다.

> 💡 fetching, caching, 서버 데이터와의 동기화를 지원해주는 라이브러리

설명을 간단히 해보면 이름처럼 React 환경에서의 비동기 Query(질의) 과정을 도와주는 라이브러리이다!! if(kakao)2021 컨퍼런스에서 언급된 내용 중, 아래와 같은 내용이 있었다.

> 🙌 「if(kakao)2021 - 카카오페이 프론트엔드 개발자들이 React Query를 선택한 이유」 세줄요약 🤟
>
> 
>
> 1. React Query는 React Application에서 서버 상태를 불러오고, 캐싱하며, 지속적으로 동기화하고 업데이트하는 작업을 도와주는 라이브러리입니다.
> 2. 복잡하고 장황한 코드가 필요한 다른 데이터 불러오기 방식과 달리 React Component 내부에서 간단하고 직관적으로 API를 사용할 수 있습니다.
> 3. 더 나아가 React Query에서 제공하는 캐싱, Window Focus Refetching 등 다양한 기능을 활용하여 API 요청과 관련된 번잡한 작업 없이 “핵심 로직”에 집중할 수 있습니다.

즉, React-Query는 프론트엔드에서 비동기 데이터를 불러오는 과정 중 발생하는 문제들을 해결해준다는 건데, 어떤 문제들을 어떻게 해결한다는 걸까?

------

## 1. 캐싱(Caching)

React-Query의 장점 중 하나는 **데이터를 캐싱**한다는 점이다.

> 캐싱이란 특정 데이터의 복사본을 저장하여 이후 동일한 데이터의 재접근 속도를 높이는 것을 말한다!

React-Query는 캐싱을 통해 동일한 데이터에 대한 **반복적인 비동기 데이터 호출을 방지**하고, 이는 불필요한 API 콜을 줄여 **서버에 대한 부하를 줄이는 좋은 결과**를 가져온다.

> 💡 최신의 데이터인지 어떻게 판별하는데??

❔여기서 궁금한 것은 데이터가 최신의 것인지 아닌지에 대한 것이다.

만일 서버 데이터를 불러와 캐싱한 후, 실제 서버 데이터를 확인했을 때 서버 상에서 데이터의 상태가 변경되어있다면, 사용자는 실제 데이터가 아닌 변경 전의 데이터를 바라볼 수밖에 없게 된다. 이는 사용자에게 잘못된 정보를 보여주는 에러를 낳는다.

> 💡 참고로, React-Query에서는 최신의 데이터를 fresh한 데이터, 기존의 데이터를 stale한 데이터라고 말한다!!

### 언제 데이터를 갱신해야하지?

위와 같은 에러를 발생시키지 않는 좋은 캐싱 기능을 제공한다는 것은 결국 필요한 상황에 적절하게 데이터를 갱신해줄 수 있다는 말과 같다. 그럼 그런 상황은 언제일까?

1. 화면을 보고 있을 때
2. 페이지의 전환이 일어났을 때
3. 페이지 전환 없이 이벤트가 발생해 데이터를 요청할 때

크게 보면 위의 3가지로 나눌 수 있다. 이를 위해 React-Query에서는 기본적인 아래의 옵션들을 제공한다.

```js
refetchOnWindowFocus, //default: true
refetchOnMount, //default: true
refetchOnReconnect, //default: true
staleTime, //default: 0
cacheTime, //default: 5분 (60 * 5 * 1000)
```

❗위의 옵션들을 통해 우리는 React-Query가 어떤 시점에 데이터를 Refetching하는지 알 수 있다.

1. 브라우저에 포커스가 들어온 경우(refetchOnWindowFocus)
2. 새로운 컴포넌트 마운트가 발생한 경우(refetchOnMount)
3. 네트워크 재연결이 발생한 경우(refetchOnReconnect)

### `staleTime`? `cacheTime` ?

**staleTime**

- staleTime은 데이터가 fresh → stale 상태로 변경되는 데 걸리는 시간이다.
- fresh 상태일 때는 Refetch 트리거(위의 3가지 경우)가 발생해도 Refetch가 일어나지 않는다!
- 기본값이 0이므로 따로 설정해주지 않는다면 Refetch 트리거가 발생했을 때 무조건 Refetch가 발생한다!

**cacheTime**

- cacheTime은 데이터가 inactive한 상태일 때 캐싱된 상태로 남아있는 시간이다.
- 특정 컴포넌트가 unmount(페이지 전환 등으로 화면에서 사라질 때) 되면 사용된 데이터는 inactive상태로 바뀌고, 이때 데이터는 cacheTime만큼 유지된다.
- cacheTime 이후 데이터는 가비지 콜렉터로 수집되어 메모리에서 해제된다.
- 만일 cacheTime이 지나지 않았는데 해당 데이터를 사용하는 컴포넌트가 다시 mount되면, 새로운 데이터를 fetch해오는 동안 캐싱된 데이터를 보여준다.
- 즉, 캐싱된 데이터를 계속 보여주는게 아니라 fetch하는 동안 **임시로** 보여준다는 것이다!!

이외에도 사용자가 특정 이벤트가 발생했을 때 Refetching을 하도록 설정해줄 수 있다. React-Query의 이러한 기능들을 통해 사용자는 언제나 최선의 데이터를 제공받게 된다.

## 2. Client 데이터와 Server 데이터 간의 분리

프로젝트의 규모가 커지고 관리해야할 데이터가 넘치다 보면, Client 에서 관리하는 데이터와 Server 에서 관리하는 데이터가 분리될 필요성을 느낀다.

> Client Data: 모달 관련 데이터, 페이지 관련 데이터 등등..
> Server Data: 사용자 정보, 비즈니스 로직 관련 정보 등등..
> *간단하게 생각해서 **비동기 API 호출을 통해 불러오는 데이터**들을 Server 데이터라고 할 수 있다.*

실제 Client 데이터의 경우 Redux, Recoil, mobX와 같은 **전역 상태 관리 라이브러리**들을 통해 잘 관리되어오고 있으나, 문제는 이러한 라이브러리들이 Server 데이터까지도 관리를 해야하는 상황이 발생한다는 것이다.

위의 상태 관리 라이브러리에도 비동기 함수를 처리하는 로직이 존재하거나, 서드 파티를 라이브러리를 지원하는 것이 많다. 그러나 이들이 Client 데이터와 Server 데이터를 완벽히 분리하여 관리에 용이하도록 충분한 기능이 지원된다고 보기 어렵다. 즉 위의 라이브러리들은 Client 데이터를 관리하는데 로직이 집중되어있기 때문에, Server 데이터까지 효율적으로 관리하기에는 한계가 분명하다.

👇 React-Query는 이러한 문제에 대한 해결책 또한 제시해 주는데, 아래 코드를 살펴보자.

```jsx
const { data, isLoading } = useQueries(
	['unique-key'],
	() => {
		return api({
			url: URL,
			method: 'GET',
		});
	},
	{
		onSuccess: (data) => {
			// data로 이것저것 하는 로직
		}
	},
	{
		onError: (error) => {
			// error로 이것저것 하는 로직
		}
	}
)
```

예시에서는 컴포넌트 내부에서 위와 같은 로직을 통해 Server 데이터를 가져오고 있는데, 이때 onSuccess와 onError 함수를 통해 fetch 성공과 실패에 대한 분기를 아주 간단하게 구현할 수 있다. 이는 Server 데이터를 불러오는 과정에서 구현해야할 추가적인 설정들을 진행할 필요가 없다는 이야기이다.

👉 **즉, Client 데이터는 상태 관리 라이브러리가 관리하고, Server 데이터는 React-Query가 관리하는 구조라고 생각하면 된다!! 이를 통해 우리는 Client 데이터와 Server 데이터를 온전하게 분리할 수 있다.**

> 🔎 물론 여기서 React-Query가 가져온 Server 데이터를 상태 관리 라이브러리를 통해 전역 상태로 가져올 수도 있는 건 사실이다. 그러나 refetch가 여러 번 일어나는 상황에 매번 Server 데이터를 전역 상태로 가져오는 것이 옳은지 판단하는 것은 여러분의 몫이다. 개발하는 서비스의 상황에 맞게 잘 선택해보도록 하자!!

## 3. 대표적인 기능들

React-Query에서 data fetching을 위해 제공하는 대표적인 기능들을 살펴보자!

기본적으로 GET 에는 useQuery가, PUT, UPDATE, DELETE에는 useMutation이 사용된다.

### useQuery

- 첫 번째 파라미터로 unique key를 포함한 배열이 들어간다. 이후 동일한 쿼리를 불러올 때 유용하게 사용된다.
- 첫 번째 파라미터에 들어가는 배열의 첫 요소는 unique key로 사용되고, 두 번째 요소부터는 query 함수 내부의 파라미터로 값들이 전달된다.
- 두 번째 파라미터로 실제 호출하고자 하는 비동기 함수가 들어간다. 이때 함수는 Promise를 반환하는 형태여야 한다.
- 최종 반환 값은 API의 성공, 실패 여부, 반환값을 포함한 객체이다.

Example

```ts
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from '@tanstack/react-query'

const queryClient = new QueryClient()

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Example />
    </QueryClientProvider>
  )
}

function Example() {
  const { isLoading, error, data } = useQuery({
    queryKey: ['repoData'],
    queryFn: () =>
      fetch('https://api.github.com/repos/tannerlinsley/react-query').then(
        (res) => res.json(),
      ),
  })

  if (isLoading) return 'Loading...'

  if (error) return 'An error has occurred: ' + error.message

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.description}</p>
      <strong>👀 {data.subscribers_count}</strong>{' '}
      <strong>✨ {data.stargazers_count}</strong>{' '}
      <strong>🍴 {data.forks_count}</strong>
    </div>
  )
}
```

- useQuery 함수가 반환하는 객체를 보면 `isLoading` 을 통해 로딩 여부를, `error` 를 통해 에러 발생 여부를, `data`를 통해 성공 시 데이터를 반환할 수 있다.
- `isLoading`과 `error`를 이용하여 각 상황 별 분기를 쉽게 진행할 수 있다.

### useQuery 동기적으로 실행

- useQuery에서 `enabled` 옵션을 사용하면 비동기 함수인 useQuery를 동기적으로 사용 가능하다.
- useQuery의 세 번째 인자로 다양한 옵션 값들이 들어가는데, 여기서 `enabled`에 값을 대입하면 해당 값이 true일 때 useQuery를 동기적으로 실행한다!

```ts
const { data: todoList, error, isFetching } = useQuery("todos", fetchTodoList);
const { data: nextTodo, error, isFetching } = useQuery(
  "nextTodos",
  fetchNextTodoList,
  {
    enabled: !!todoList // true가 되면 fetchNextTodoList를 실행한다
  }
);
```

### useQueries

여러 개의 useQuery를 한 번에 실행하고자 하는 경우, 기존의 `Promise.all()`처럼 묶어서 실행할 수 있도록 도와준다!

```ts
const results = useQueries({
  queries: [
    { queryKey: ['post', 1], queryFn: fetchPost, staleTime: Infinity},
    { queryKey: ['post', 2], queryFn: fetchPost, staleTime: Infinity}
  ]
})

// 두 query에 대한 반환값이 배열로 묶여 반환된다!!
```

### useMutation

- 위에서 언급한 것처럼 PUT, UPDATE, DELETE 와 같이 값을 변경할 때 사용하는 API다. 반환값은 useQuery와 동일하다.

빠르게 예시를 살펴보자.

```ts
function App() {
  const mutation = useMutation({
    mutationFn: (newTodo) => {
      return axios.post('/todos', newTodo)
    },
  })

  return (
    <div>
      {mutation.isLoading ? (
        'Adding todo...'
      ) : (
        <>
          {mutation.isError ? (
            <div>An error occurred: {mutation.error.message}</div>
          ) : null}

          {mutation.isSuccess ? <div>Todo added!</div> : null}

          <button
            onClick={() => {
              mutation.mutate({ id: new Date(), title: 'Do Laundry' })
            }}
          >
            Create Todo
          </button>
        </>
      )}
    </div>
  )
}
```

- 위의 코드에서 볼 수 있듯이 반환값은 useQuery와 동일하지만, 처음 사용 시에 post 비동기 함수를 넣어주었다. 이때 useMutation의 첫 번째 파라미터에 비동기 함수가 들어가고, 두 번째 인자로 상황 별 분기 설정이 들어간다는 점이 차이이다.
- 실제 사용 시에는 `mutation.mutate` 메서드를 사용하고, 첫 번째 인자로 API 호출 시에 전달해주어야하는 데이터를 넣어주면 된다!!

# ↔️ SWR과의 비교

React-Query 가 장점만 보유하고 있다면, 다른 경쟁 라이브러리들이 살아남기 어려울 것이다. 그렇다면 React-Query가 가지는 단점으로는 어떤 것들이 있을까? 이를 React-Query만큼 대표적인 Data fetching 라이브러리인 SWR과 비교하면서 알아보자!

![img](https://velog.velcdn.com/images/kandy1002/post/1280ceac-6227-4afa-841f-1e3167fa1845/image.png)

위 사진은 [State of js](https://2022.stateofjs.com/en-US/other-tools/)에서 조사한 2022 라이브러리 사용 빈도이다. 보면 React-Query가 더 많이 사용되었지만, SWR도 상당 비율 차지하고 있음을 알 수 있다.

👇 먼저 아래 코드를 통해 두 라이브러리의 기본적인 사용 예시를 살펴보자.

### SWR

```tsx
import useSWR from "swr";

const App = () => (
  <div>
    <SWRProfile />
  </div>
);

const SWRProfile = () => {
  const {data, error} = useSWR("https://61b88c9d64e4a10017d19053.mockapi.io/user", url =>
    fetch(url).then(res => res.json())
  );

  if (error) return <div>failed to load</div>;
  if (!data) return <div>loading...</div>;

  return <Profile library="SWR" data={data} />;
}

const Profile = ({library, data}) => (
  <div>
    <h1>Users from {library}</h1>
    {data.map(user => <p>{user.level} developer <strong>{user.name}</strong></p>)}
  </div>
)

export default App;
```

### React-Query

```tsx
import { QueryClient, QueryClientProvider, useQuery } from "react-query";

const queryClient = new QueryClient();
const url = "https://61b88c9d64e4a10017d19053.mockapi.io/user";

const App = () => (
  <div>
    <QueryClientProvider client={queryClient}>
      <ReactQueryProfile />
    </QueryClientProvider>
  </div>
);

const ReactQueryProfile = () => {
  const {isLoading, error, data, isFetching} = useQuery("users", () =>
    fetch("https://61b88c9d64e4a10017d19053.mockapi.io/user").then(res => res.json())
  );

  if (error) return <div>failed to load</div>;
  if (isLoading) return <div>loading...</div>;

  return <Profile library="React Query" data={data} />;
}

const Profile = ({library, data}) => (
  <div>
    <h1>Users from {library}</h1>
    {data.map(user => <p>{user.level} developer <strong>{user.name}</strong></p>)}
  </div>
)

export default App;
```

위 코드를 통해 알아볼 수 있는 SWR의 강점은 다음과 같다.

#### Provider

SWR은 별도의 Provider 없이 컴포넌트에서 바로 사용할 수 있으나, React-Query는 기본적으로 컴포넌트를 감싸는 별도의 Provider가 필요해 이를 설정해주어야한다. 사실 이게 귀찮게 다가오는 정도는 아니지만, 초기 설정을 하나 더 해주어야한다는 점이 있다.

#### Fetcher

useSWR, useQuery 모두 두 번째 인자로 fetcher를 받는다. 이때 SWR의 경우 첫 번째 인자로 url을 받고, 두 번째 인자인 fetcher에 첫 번째 인자로 받은 url을 넘겨주는 방식을 사용한다. 또한 SWR은 전역 설정을 통해 fetcher를 정해둘 수 있다. 그러나 React-Query는 fetcher에 url을 직접 전달해주어야 한다.

------

이외에 React-Query가 가지는 장점들에는 무엇이 있을까?

#### Devtools

React-Query에서는 공식적으로 `react-query/devtools` 를 통해 Devtool을 지원한다. 개발 모드에서만 사용하며, devtools를 통해 좀 더 확실하게 데이터의 흐름을 파악할 수 있다.

SWR 또한 devtools를 사용할 수 있으나, 서드 파티 라이브러리를 이용해야한다.

![img](https://velog.velcdn.com/images/kandy1002/post/bd84a61d-bc30-4e95-afb3-35e72033f27f/image.png)

#### 무한 스크롤 구현

SWR과 React-Query 모두 무한 스크롤을 구현하는 데 필요한 기능들을 제공한다.

그러나 SWR로 무한 스크롤을 구현하려면 유저가 부가적인 코드를 작성해야하는 반면,

React-Query에는 `getPreviousPageParam`, `fetchPreviousPage`, `hasPreviousPage` 와 같은 다양한 페이지 관련 기능이 존재해 이를 이용해 무한 스크롤을 쉽게 구현할 수 있다!!

#### Selectors

React-Query에서는 `select` 키워드를 사용해 raw data로부터 원하는 데이터를 추출하여 반환할 수 있다. 아래 코드로 살펴보자.

```tsx
import { useQuery } from 'react-query'

function User() {
  const { data } = useQuery('user', fetchUser, {
    select: user => user.username,
  })
  return <div>Username: {data}</div>
}
```

👆 위의 예시처럼 `select` 를 통해 원하는 데이터에 접근한 뒤 추출이 가능하다!

#### Data Optimization

SWR과 다르게 React-query는 쿼리가 업데이트될 때만 refetch를 진행한다. 또한 여러 컴포넌트에서 동일한 쿼리를 사용하는 경우 한번에 묶어 업데이트를 진행한다! 이를 통해 렌더링 퍼포먼스를 개선해준다.

#### Garbage Collection

React-Query는 지정된 시간(기본 5분)동안 쿼리가 사용되지 않는다면 자동으로 메모리 해제를 하는 Auto Garbage Collection을 통해 메모리를 관리해준다.

# 🔘 버전 선택

지금 React-Query를 공부하고자 공식 문서를 들어가보면 공식 문서는 v3을 가장 먼저 소개하고 있다.

그래서 아 v3이 최신 버전인가부다~하고 버전 선택 토글을 열어보면,,

![img](https://velog.velcdn.com/images/kandy1002/post/be05ecf9-78d3-4ccd-a5fe-6be433923c91/image.png)

> 으잉..? 젤 옛날 버전을 공부하라구요?

#### 그래서 알아봤더니 현재 최신으로 지원하는 버전은 v4, v5는 실험용 버전으로 보인다. 맨 위 Latest를 선택하면 v4를 표시해주니 v4에 맞춰 공부를 하면 좋을 것 같다!

## 🔄 v4에서의 변경점

React-Query v4에서는 패키지 이름부터 `@tanstack/react-query`로 변경되면서 **React에만 국한되지 않은 범용 프론트엔드 라이브러리로 개선**되었다. 즉 tanstack이라는 오픈 소스 소프트웨어 프로젝트 하위의 라이브러리인 것이다!! 공식문서도 tanstack에서 제공하고 있으니 헷갈리지 않도록 주의하자.

그 변경점을 중점적인 내용들만 다뤄보면 아래와 같다.

### 1. 라이브러리 이름 변경

라이브러리 이름이 변경되면서 import를 할 때 `@tanstack/react-query`로 진행해야한다. `react-query`라는 라이브러리는 더는 없다!!

### 2. Query key에 배열을 넣어주자

useQuery 훅을 사용하면서 첫 번째 인자로 unique key를 정해주었는데, 이제 해당 입력값이 하나만 있더라도 무조건 배열의 형태를 띄어야 한다!!

```null
- useQuery('todos', fetchTodos)
+ useQuery(['todos'], fetchTodos)
```

### 3. useQueries에 여러 쿼리를 넘길 때 queries를 명시하자

기존의 코드에서는 useQueries를 사용할 때 인자로 다음과 같이 쿼리 정보를 담은 배열을 보내줬다. 그러나 이제는 이를 묶어서 `queries`라는 파라미터로 전달해주어야한다!!

```null
- useQueries([{ queryKey1, queryFn1, options1 }, { queryKey2, queryFn2, options2 }])
+ useQueries({ queries: [{ queryKey1, queryFn1, options1 }, { queryKey2, queryFn2, options2 }] })
```

### 4. 이제 undefined 대신 Error를 반환해요!

비동기 함수들 중에는 query가 잘못된 경우 모종의 이유로 결과값이 undefined인 경우가 있다.

이전까지는 이러한 경우 그저 반환값 undefined를 그대로 우리에게 보내주었는데, 이제는 React-Query 자체적으로 이를 감지하고 이런 경우 API 호출을 Failed라고 표시하고 Error를 반환한다. 값이 없는 경우도 Error로 분기해서 보내준다니, 아주 편리한 기능이라고 할 수 있다!!!

> 이외에도 v4에서는 좋은 기능들을 많이 제공하지만, 나머지 기능들은 좀 더 깊이 있게 다뤄야 할 내용들이어서 간단한 것들만 적어뒀다. 더 공부가 필요하다면 [tanstack/react-query](https://tanstack.com/query/latest/docs/react/guides/migrating-to-react-query-4#new-api-for-usequeries)를 직접 방문한 뒤 정독해봅시다!!

------

여기까지 SWR과의 대표적인 차이를 알아보았다. 당연히 SWR 또한 좋은 라이브러리이며, SWR만의 강점이 더 존재하겠지만 이번 시간에 소개하지는 않겠다. 다른 다양한 기능들을 알아보고자 한다면 [SWR](https://swr.vercel.app/ko) | [React-Query](https://tanstack.com/query/latest/docs/react/overview)를 확인해보자!!

지금까지 React-Query의 개념과 사용 이유를 알아보고, 간단한 예시와 SWR과의 비교를 진행해보았다!!

## Reference

[TanStack Query](https://tanstack.com/query/latest/docs/react/overview)
[react-query 개념 및 정리](https://kyounghwan01.github.io/blog/React/react-query/basic/)
[[React-Query\] 총 정리](https://velog.io/@94applekoo/React-Query-총-정리#1-알아보기)
[React Query vs SWR](https://tech.madup.com/react-query-vs-swr/)

<br>

<br>

#### 참고자료: [[React-Query\] React-Query 개념잡기 (velog.io)](https://velog.io/@kandy1002/React-Query-푹-찍어먹기)

<br>