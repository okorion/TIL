## 🌴 상태 관리를 위한 라이브러리 jotai 훑어보기

이번에 신규 프로젝트 개발을 하면서 React-query와 함께 jotai를 도입하기로 했다.
전에 작업하면서는 거의 리덕스로 모든 데이터를 전역에 저장하고 썼었는데, 전역 상태를 관리하고 업데이트 하기 위해 귀찮은 작업들이 많았던 기억이 있었다. 이번 프로젝트에서는 그보다는 가볍게 각 페이지에서 필요한 데이터를 가져다 쓰는 형태를 기본으로 하고, 로그인 세션이나 전역 모달 처리 정도만 상태 관리 라이브러리를 사용해보기로 했다.

사실 비교적 익숙한 리덕스나 RTK로 쉽게 갈까 고민하다가, 전역에서 관리할 데이터들이 정말 많지 않은 상황에서 리덕스가 너무 무거워서 맞는 방법이 아닌 것 같다는 생각이 계속 들었다. 고민 끝에 좀더 가벼운 상태 관리 라이브러리로 최근 플랫폼에서 적극 도입하고 있는 jotai를 쓰기로 결정!

![img](https://velog.velcdn.com/images%2Fggong%2Fpost%2Fda7cc505-30c1-4dad-83fb-75939b495a28%2Fimage.png)

### 1. 상태 관리, Flux vs Atomic

최근의 상태 관리에 대한 접근 방식은 몇 가지로 나눠서 볼 수 있다.

> - Flux (Redux, Zusstand)
> - Proxy (Mobx, Valtio)
> - Atomic (Jotai, Recoil)

일반적으로 많이 쓰는 Flux 패턴인 리덕스를 보면 액션을 통해 앱 상태를 변화시키고, 컴포넌트는 selector를 사용해 전역 상태의 일부를 구독(subscribing) 하는 형태로 동작한다. 리덕스 환경에서 store에 있는 값을 변경하기 위해서는 액션 함수를 실행하고 특정 액션 타입을 리듀서에 전달하는 방식으로 변화를 전달해야 한다. 그러다보니 보일러플레이트가 아주 많고 데이터를 변화시키기 위해 작성해야 하는 코드 양도 많다.

반면 Proxy 패턴인 Mobx에서는 전체 상태에 대한 액세스를 제공하고, 컴포넌트에서 사용되는 일부 상태를 자동으로 감지하고 업데이트만 인지해서 사용한다. 리덕스보다 디버깅은 어렵지만 store에 있는 데이터를 바로 변경할 수 있는 Mobx가 더 편하게 느껴질 때도 많았다.

마지막으로, jotai와 recoil 같은 Atomic 접근 방식은 React에서 사용되는 state와 비슷하게 리액트 트리 안에서 상태를 저장하고 관리하는 방법이다. 나도 jotai에 대해 찾아보면서 `context`와 비슷하다고 느꼈었는데, 실제로 다른 상태 관리 라이브러리들보다는 `context`나 `useState`와 비교되는 경우가 더 많다.



### 2. Atomic features

jotai의 atom은 상태 조각(a piece of state), 아주 작은 단위의 상태를 의미한다. 상태들을 만들기 위한 atom 함수는 useState와 비슷하게 초기값으로 string, number, object, array와 같은 원시값을 받을 수 있다.

```javascript
import { atom } from 'jotai'

const countAtom = atom(0);
const mangaAtom = atom({ 'label': '', 'content': '' });
```

상태를 작게 쪼갰다는 특성 때문에 상태의 변화가 많고 업데이트가 잦은 케이스에서는 `useState`를 사용한 `context`보다 효율적으로 평가된다. (그렇지만 기본적인 작동 방식은 비슷하다고 느꼈다) 상태들은 여러 컴포넌트에 의존성을 가질 수 있고, 의존성을 가진 부분만 업데이트된다.

jotai의 atom은 아래 케이스로 나눌 수 있다.

- Read-only atom (값을 가져오는 경우)
- Write-only atom (값을 업데이트)
- Read-Write atom (둘 다)

```javascript
const readOnlyAtom = atom((get) => get(priceAtom) * 2)
const writeOnlyAtom = atom(
  null, // 첫번째 인자로 전달하는 초기값은 null로 전달
  (get, set, update) => {
    // update는 atom을 업데이트하기 위해 받아오는 값
    set(priceAtom, get(priceAtom) - update.discount)
  }
)
const readWriteAtom = atom(
  (get) => get(priceAtom) * 2,
  (get, set, newPrice) => {
    set(priceAtom, newPrice / 2)
    // set 로직은 원하는 만큼 지정할 수 있다.
  }
)
```

Read-only atom은 셀렉터 형태라고도 볼 수 있다. atom 함수의 인자로 이미 존재하는 상태를 읽어서 새로운 값을 반환하는 함수를 전달하면, 셀렉터와 동일하게 사용할 수 있다. `get` 메소드를 통해 존재하는 atom 값들에 접근한다.

이렇게 초기값을 넣고 상태를 생성하면, `useAtom` 함수를 사용해서 튜플 형태로 상태값을 가져올 수 있다.

```javascript
const [value, updateValue] = useAtom(anAtom)
```

`useAtom` hook은 상태에 있는 atom 값을 읽어오고, 값과 업데이트 함수를 배열 형태로 반환한다. (`useState`랑 엄청 비슷하다!) 초기에는 state에 저장된 값이 없다가 `useAtom` 함수를 통해 atom이 최초로 불러와지면, 초기값이 상태에 저장된다. atom이 더이상 사용되지 않으면 (그 상태를 사용하는 모든 컴포넌트들이 언마운트되면) 값은 가비지 콜렉트된다.
`updateValue`는 하나의 파라미터만 받으며, 이것은 위에서 본 write function에서처럼 `(get, set, newPrice)` 형태로 세번째 파라미터로 전달된다.

여기까지 전체적으로 보면서 느낀건 jotai의 작동 방식이 리액트 `useState`와 아주 비슷하다는 점이었다. 일단 기본적인 로직을 파악하는 데는 러닝커브가 높지 않았고 가볍게 상태를 관리하기에 적합하다는 느낌이 들었다.



### 3. jotai-utils

jotai는 유용한 유틸도 제공한다. (오히려 공식 문서만 보면 core보다 utils 내용이 더 길었다)
알아두면 좋을것 같은 유틸들을 몇가지 알아봤다.

#### 1) AtomWithStorage

```javascript
import { useAtom } from 'jotai'
import { atomWithStorage } from 'jotai/utils'

const darkModeAtom = atomWithStorage('darkMode', false)

const Page = () => {
  const [darkMode, setDarkMode] = useAtom(darkModeAtom)

  return (
    <>
      <h1>Welcome to {darkMode ? 'dark' : 'light'} mode!</h1>
      <button onClick={() => setDarkMode(!darkMode)}>toggle theme</button>
    </>
  )
}
```

`atomWithStorage` 함수는 로컬스토리지나 세션스토리지에 저장되는 값들을 생성할 수 있다. 파라미터로는 아래와 같은 값들을 받는다.

- key(required) : 스토리지에 저장된 값을 특정하기 위한 키
- initialValue (required) : 초기값
- storage (optional) : getItem, setItem 메소드를 실행할 object. 디폴트 설정은 localStorage이며, serialization을 지원한다.

#### 2) useUpdateAtom, useAtomValue

```javascript
import { atom, Provider, useAtom } from 'jotai'
import { useAtomValue } from 'jotai/utils'

const countAtom = atom(0)

const Counter = () => {
  const setCount = useUpdateAtom(countAtom)
  const count = useAtomValue(countAtom)
  return (
    <>
      <div>count: {count}</div>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </>
  )
}
```

useAtom처럼 배열 형태가 아니라 atom 값만, 혹은 set 함수만 가져올 수도 있다.

#### 3) selectAtom

데이터가 많을 경우 atom끼리도 나눠서 관리할 수 있도록 방법을 제공한다.
그중에서도 selectAtom은 파라미터로 아래의 값들을 받는다.

- atom : 원본 atom
- selector: (value) => slice 형태로, 가져올 특정 atom 값을 구하는 함수. 오리지널 atom이 변경될 때마다 함수가 실행된다.
- equalityFn : 값의 변경 여부를 판단하는 함수

```javascript
const defaultPerson = {
  name: {
    first: 'Jane',
    last: 'Doe',
  },
  birth: {
    year: 2000,
    month: 'Jan',
    day: 1,
    time: {
      hour: 1,
      minute: 1,
    },
  },
}

// 기본 atom
const personAtom = atom(defaultPerson)
// person.name을 추적하는 atom.
// person.name 객체가 변화하면 업데이트됨
const nameAtom = selectAtom(personAtom, (person) => person.name)
// person.birth를 추적하는 atom.
// deepEquals 옵션은 birth 객체가 같은 데이터 값을 가진 새로운 객체로 변경될 경우, 업데이트 하지 않음을 의미한다.
const birthAtom = selectAtom(personAtom, (person) => person.birth, deepEquals)
```

### 4. integration

jotai는 다른 라이브러리들과의 integration도 공식적으로 지원한다. 특히 이번 프로젝트에서 사용하고 있는 react-query와의 integration 문서가 잘 되어 있어서 반가웠다.

```javascript
import { useAtom } from 'jotai'
import { atomWithQuery } from 'jotai/query'

const idAtom = atom(1)
const userAtom = atomWithQuery((get) => ({
  queryKey: ['users', get(idAtom)],
  queryFn: async ({ queryKey: [, id] }) => {
    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    return res.json()
  },
}))

const UserData = () => {
  const [data] = useAtom(userAtom)
  return <div>{JSON.stringify(data)}</div>
}
```

`atomWithQuery`는 react-query의 useQuery문을 실행하는 것과 동일한 로직으로 atom을 생성할 수 있다. (jotai 로직과 react-query가 통합되어 있어서 신기했음)
로그인 이후 세션 처리를 하는 로직에서 유용하게 사용할 수 있을 것 같다는 생각이 들었다. `useMutation` 로직에도 적용이 가능한지 궁금했는데, 일단 `useQuery`만 지원하는듯? `jotai/query` 라이브러리를 좀더 뜯어봐야겠다.



기본적인 기능들만 훑어봤지만, 일단 사용 방법이 복잡하지 않고 가볍다는 느낌이 들었다. 그러면서도 스토리지 저장이나 다른 라이브러리들과의 연동을 고려한걸 보면 실제 사용하는 관점에서 유용한 방법들에 대해 많이 고민해서 만들어진 것 같다고 느꼈다.
더 디테일한 기능들은 실제 프로젝트에 사용해보면서 파악하는걸로!





**참고 :**
jotai 공식 문서 (https://docs.pmnd.rs/jotai/introduction)
Jotai vs. Recoil: What are the differences? (https://blog.logrocket.com/jotai-vs-recoil-what-are-the-differences/)
화해 기술 블로그 - Atomic state management – Jotai (http://blog.hwahae.co.kr/all/tech/tech-tech/6099/)



<br>

<br>

#### 참고링크: [상태 관리를 위한 라이브러리 jotai 훑어보기 (velog.io)](https://velog.io/@ggong/상태-관리를-위한-라이브러리-jotai)

<br>