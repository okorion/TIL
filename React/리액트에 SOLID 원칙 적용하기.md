## 💥 리액트에 SOLID 원칙 적용하기

원문 : https://konstantinlebedev.com/solid-in-react/



![img](https://blog.kakaocdn.net/dn/dMxmfO/btrHvoYF4mR/5Eoybzb2VCxS67CpXbEDz0/img.jpg)Photo by Jeff Nissen on Unsplash



소프트웨어 산업이 성장하고 실수를 범함에 따라 모범 사례와 우수한 소프트웨어 설계 원칙이 나타나고

미래에 같은 실수를 반복하지 않도록 개념화됩니다.

특히 객체 지향 프로그래밍(OOP)의 세계는 이러한 모범 사례의 금광이며

SOLID는 의심할 여지 없이 가장 영향력 있는 것 중 하나입니다.

SOLID는 각 문자가 다음과 같은 5가지 디자인 원칙 중 하나를 나타내는 약어입니다.

- 단일 책임 원칙(SRP)
- 개방 폐쇄 원칙(OCP)
- Liskov 치환 원칙(LSP)
- 인터페이스 분리 원칙(ISP)
- 의존성 역전 원칙(DIP)

이 기사에서는 각 원칙의 중요성에 대해 이야기하고

SOLID에서 배운 내용을 React 애플리케이션에 어떻게 적용할 수 있는지 알아보겠습니다.

 

시작하기 전에 큰 주의 사항이 있습니다.

SOLID 원칙은 객체 지향 프로그래밍 언어를 염두에 두고 구상되고 설명되었습니다.

**이러한 원칙과 설명은 클래스와 인터페이스의 개념에 크게 의존하지만 JS에는 실제로 그런 개념이 없습니다.**

 

JS에서 우리가 흔히 "클래스"라고 생각하는 것은 프로토타입 시스템을 사용하여 시뮬레이션된 클래스 유사품일 뿐이며

인터페이스는 언어의 일부가 아닙니다(TypeScript의 추가가 약간 도움이 되기는 하지만).

 

더군다나 우리가 최신 React 코드를 작성하는 방식은 객체 지향이 아니라 오히려 더 함수적으로 느껴집니다.

 

**하지만 좋은 소식은 SOLID와 같은 소프트웨어 설계 원칙은 언어에 구애받지 않는 높은 수준의 추상화를 가지고 있다는 것입니다.**

즉, 우리가 충분히 곁눈질하고 해석에 자유를 준다면 더 함수적인 React 코드에 적용할 수 있습니다.

## **Single responsibility principle (SRP)** 

원래 정의는 "모든 클래스는 단 하나의 책임만 가져야 한다"고 명시되어 있습니다.

이 원칙은 해석하기 가장 쉽습니다.

**"모든 함수/모듈/컴포넌트는 정확히 한 가지 작업을 수행해야 함"으로 정의를 외삽할 수 있기 때문입니다.**

 

5가지 원칙 중 SRP는 가장 따르기 쉽지만 코드의 품질을 크게 향상시키기 때문에 가장 영향력 있는 원칙이기도 합니다.

컴포넌트가 한 가지 작업을 수행하도록 하기 위해 다음을 수행할 수 있습니다.

 

- 너무 많은 작업을 수행하는 큰 컴포넌트를 더 작은 컴포넌트로 나눕니다.
- 주요 컴포넌트 기능과 관련 없는 코드를 별도의 유틸리티 함수로 추출
- 연결된 기능을 커스텀 훅으로 캡슐화

이제 이 원칙을 적용하는 방법을 살펴보겠습니다.

활성 사용자 목록을 표시하는 다음 예제 컴포넌트를 고려하여 시작하겠습니다.

```
const ActiveUsersList = () => {
  const [users, setUsers] = useState([])
  
  useEffect(() => {
    const loadUsers = async () => {  
      const response = await fetch('/some-api')
      const data = await response.json()
      setUsers(data)
    }

    loadUsers()
  }, [])
  
  const weekAgo = new Date();
  weekAgo.setDate(weekAgo.getDate() - 7);

  return (
    <ul>
      {users.filter(user => !user.isBanned && user.lastActivityAt >= weekAgo).map(user => 
        <li key={user.id}>
          <img src={user.avatarUrl} />
          <p>{user.fullName}</p>
          <small>{user.role}</small>
        </li>
      )}
    </ul>    
  )
}
```

------

이 컴포넌트는 현재 비교적 코드가 짧지만

데이터를 가져오고, 필터링하고, 컴포넌트 자체와 개별 리스트 아이템을 렌더링하는 등 이미 몇 가지 작업을 수행하고 있습니다.

어떻게 분해할 수 있는지 봅시다.

 

#### 우선 **useState** 와 **useEffect** 훅은 커스텀 훅으로 추출할 수 있는 좋은 기회입니다.

```
const useUsers = () => {
  const [users, setUsers] = useState([])
  
  useEffect(() => {
    const loadUsers = async () => {  
      const response = await fetch('/some-api')
      const data = await response.json()
      setUsers(data)
    }

    loadUsers()
  }, [])
  
  return { users }
}


const ActiveUsersList = () => {
  const { users } = useUsers()
  
  const weekAgo = new Date()
  weekAgo.setDate(weekAgo.getDate() - 7)

  return (
    <ul>
      {users.filter(user => !user.isBanned && user.lastActivityAt >= weekAgo).map(user => 
        <li key={user.id}>
          <img src={user.avatarUrl} />
          <p>{user.fullName}</p>
          <small>{user.role}</small>
        </li>
      )}
    </ul>    
  )
}
```

------

**이제 useUsers 후크는 API에서 사용자를 가져오는 한 가지에만 관심이 있습니다.**

또한 메인 컴포넌트 코드가가 더 짧아졌을 뿐만 아니라

목적을 해독하는 것이 필요한 구조적 훅을

이름에서 즉시 알 수 있는 도메인 훅으로 대체했기 때문에

메인 컴포넌트를 더 읽기 쉽게 만들었습니다.

 

#### **다음으로 컴포넌트가 렌더링하는 JSX를 살펴보겠습니다.**

 

객체 배열에 대한 루프 매핑이 있을 때마다 개별 배열 항목에 대해 생성하는 JSX의 복잡성에 주의를 기울여야 합니다.

**이벤트 처리기가 연결되지 않은 단일 라이너인 경우 인라인으로 유지하는 것이 좋지만**

더 복잡한 마크업의 경우 **별도의 컴포넌트로** 추출하는 것이 좋습니다.

```
const UserItem = ({ user }) => {
  return (
    <li>
      <img src={user.avatarUrl} />
      <p>{user.fullName}</p>
      <small>{user.role}</small>
    </li>
  )
}


const ActiveUsersList = () => {
  const { users } = useUsers()
  
  const weekAgo = new Date()
  weekAgo.setDate(weekAgo.getDate() - 7)

  return (
    <ul>
      {users.filter(user => !user.isBanned && user.lastActivityAt >= weekAgo).map(user => 
        <UserItem key={user.id} user={user} />
      )}
    </ul>    
  )
}
```

------

이전 변경과 마찬가지로 사용자 아이템(배열 항목)을 별도의 컴포넌트로 **렌더링하는 논리를 추출하여**

**기본 컴포넌트를 더 작고 읽기 쉽게 만들었습니다.**

 

#### 마지막으로 API에서 얻은 모든 사용자 목록에서 비활성 사용자를 **필터링하는** 논리가 있습니다.

이 로직은 상대적으로 격리되어 있으며 애플리케이션의 다른 부분에서 재사용할 수 있으므로 유틸리티 함수로 쉽게 추출할 수 있습니다.

```
const getOnlyActive = (users) => {
  const weekAgo = new Date()
  weekAgo.setDate(weekAgo.getDate() - 7)
  
  return users.filter(user => !user.isBanned && user.lastActivityAt >= weekAgo)
}

const ActiveUsersList = () => {
  const { users } = useUsers()

  return (
    <ul>
      {getOnlyActive(users).map(user => 
        <UserItem key={user.id} user={user} />
      )}
    </ul>    
  )
}
```

------

이제 주 컴포넌트는 상당히 간단합니다.

그러나 조금 더 자세히 살펴보면 여전히 해야 할 것보다 더 많은 일을 하고 있음을 알 수 있습니다.

현재 우리의 컴포넌트는 데이터를 가져온 다음 필터링을 적용하고 있지만

이상적으로는 추가 조작 없이 데이터를 가져와 렌더링하기만 하면 됩니다.

**따라서 마지막 개선 사항으로 이 로직을 새로운 커스텀 훅으로 캡슐화할 수 있습니다.**

 

오직 렌더링만??

```
const useActiveUsers = () => {
  const { users } = useUsers()

  const activeUsers = useMemo(() => {
    return getOnlyActive(users)
  }, [users])

  return { activeUsers }
}

const ActiveUsersList = () => {
  const { activeUsers } = useActiveUsers()

  return (
    <ul>
      {activeUsers.map(user => 
        <UserItem key={user.id} user={user} />
      )}
    </ul>    
  )
}
```

------

여기에서 우리는 로직을 가져오고 필터링하기 위해

useActiveUsers 후크를 만들었으며(좋은 성능을 위해 필터링된 데이터도 메모했습니다),

**이제 주 컴포넌트는 훅에서 가져온 데이터를 렌더링하는 최소한의 작업만 수행합니다.**

 

이제 "한 가지"에 대한 해석에 따라 컴포넌트가 여전히 먼저 데이터를 얻은 다음 렌더링하는데 어떻게 "한 가지"냐고 주장할 수 있습니다. **한 컴포넌트에서 후크를 호출한 다음 그 결과를 다른 컴포넌트에 props로 전달하여 더 분할할 수 있지만**

실제 애플리케이션에서 이것이 실제로 유익한 경우는 거의 없었으므로 적당히 타협합시다.

"컴포넌트가 가져오는 렌더링 데이터"는 "한 가지 일처럼"로 간주됩니다.

 

요약하자면, 단일 책임 원칙에 따라 우리는 큰 모놀리식 코드 조각을 효과적으로 가져와 더 모듈화합니다.

모듈화는 코드를 더 쉽게 추론할 수 있게 하고, 더 작은 모듈은 테스트 및 수정하기 쉽고, 의도하지 않은 코드 중복을 도입할 가능성이 줄어들고, 결과적으로 코드를 보다 쉽게 유지 관리할 수 있기 때문에 훌륭합니다.

 

여기서 우리가 본 것은 인위적인 예이며 자신의 컴포넌트에서 서로 다른 움직이는 부분 간의 종속성이 훨씬 더 얽혀 있음을 알 수 있습니다. 많은 경우 이것은 잘못된 추상화 사용, 보편적인 do-it-all 컴포넌트 생성,

잘못된 데이터 범위 지정 등의 잘못된 디자인 선택을 나타내는 것일 수 있으며,

광범위한 리팩토링을 통해 분해할 수 있습니다.



## **Open-closed principle (OCP)**

OCP는 "소프트웨어 엔터티는 확장을 위해 열려야 하지만 수정에는 닫혀 있어야 합니다"라고 말합니다.

React 컴포넌트와 함수는 소프트웨어 엔티티이기 때문에 위의 정의를 그대로 적용할 수 있습니다.

 

개방 폐쇄 원칙은 원본 소스 코드를 변경하지 않고 확장할 수 있는 방식으로 컴포넌트를 구조화하는 것을 지지합니다.

실제로 작동하는 모습을 보기 위해 다음 시나리오를 고려해 보겠습니다.

다른 페이지에서 공유 Header 컴포넌트를 사용하는 응용 프로그램에서 작업하고 있으며

현재 있는 페이지에 따라 Header가 약간 다른 UI를 렌더링해야 합니다.

```
const Header = () => {
  const { pathname } = useRouter()
  
  return (
    <header>
      <Logo />
      <Actions>
        {pathname === '/dashboard' && <Link to="/events/new">Create event</Link>}
        {pathname === '/' && <Link to="/dashboard">Go to dashboard</Link>}
      </Actions>
    </header>
  )
}

const HomePage = () => (
  <>
    <Header />
    <OtherHomeStuff />
  </>
)

const DashboardPage = () => (
  <>
    <Header />
    <OtherDashboardStuff />
  </>
)
```

------

여기에서 현재 페이지에 따라 다른 페이지 컴포넌트에 대한 링크를 렌더링합니다.

더 많은 페이지를 추가하기 시작할 때 어떤 일이 일어날지 생각하면 이 구현이 나쁘다는 것을 쉽게 알 수 있습니다.

새 페이지가 생성될 때마다 헤더 컴포넌트로 돌아가서 렌더링할 작업 링크를 알 수 있도록 구현을 조정해야 합니다.

이러한 접근 방식은 Header 컴포넌트를 취약하게 만들고 사용되는 컨텍스트와 밀접하게 연결하며, 개방형 원칙에 위배됩니다.

 

이 문제를 해결하기 위해 컴포넌트 합성을 사용할 수 있습니다.

Header 컴포넌트는 내부에서 무엇을 렌더링할지 신경 쓸 필요가 없으며

**대신 children prop을 사용하여 이를 사용할 컴포넌트에 이 책임을 위임할 수 있습니다.**

```
const Header = ({ children }) => (
  <header>
    <Logo />
    <Actions>
      {children}
    </Actions>
  </header>
)

const HomePage = () => (
  <>
    <Header>
      <Link to="/dashboard">Go to dashboard</Link>
    </Header>
    <OtherHomeStuff />
  </>
)


const DashboardPage = () => (
  <>
    <Header>
      <Link to="/events/new">Create event</Link>
    </Header>
    <OtherDashboardStuff />
  </>
)
```

------

이 접근 방식을 사용하면 헤더 내부에 있던 변수 논리를 완전히 제거하고

이제 합성을 사용하여 컴포넌트 자체를 수정하지 않고도 문자 그대로 원하는 모든 것을 넣을 수 있습니다.

 

**비유적으로 이해하는 좋은 방법은 우리가 연결할 수 있는 컴포넌트에 플레이스홀더를 제공하는 것입니다.**

여러 확장 지점이 필요한 경우(또는 children prop이 이미 다른 용도로 사용되는 경우),

원하는 만큼의 다른 prop을 플레이스홀더로 사용할 수 있습니다.

 

**헤더에서 이를 사용하는 컴포넌트로 일부 컨텍스트를 전달해야 하는 경우 렌더 프롭 패턴을 사용할 수 있습니다.**

보시다시피 합성은 매우 강력할 수 있습니다.

개방-폐쇄 원칙에 따라 컴포넌트 간의 결합을 줄이고 확장성과 재사용성을 높일 수 있습니다.

## **Liskov substitution principle (LSP)**

지나치게 단순화된 LSP는 "하위 유형 개체가 상위 유형 개체를 대체해야 하는" 개체 간의 관계 유형으로 정의될 수 있습니다.

이 원칙은 슈퍼타입과 서브타입 관계를 정의하기 위해 클래스 상속에 크게 의존하지만,

클래스 상속은 고사하고 클래스를 거의 다루지 않기 때문에 React에서는 별로 적용할 수 없습니다.

클래스 상속에서 벗어나면 필연적으로 이 원칙이 완전히 다른 것으로 바뀌겠지만

상속을 사용하여 React 코드를 작성하면 의도적으로 나쁜 코드가 생성될 수 있으므로(React 팀은 이를 매우 권장하지 않음) 대신 이 원칙을 건너뛸 것입니다.

## **Interface segregation principle (ISP)**

ISP에 따르면 "클라이언트는 사용하지 않는 인터페이스에 의존해서는 안 됩니다."

**React 애플리케이션을 위해 "컴포넌트는 사용하지 않는 props에 의존해서는 안 됩니다"로 번역할 것입니다.**

 

여기에서 ISP의 정의를 확장하고 있지만 크게 확장되지는 않습니다.

**prop과 인터페이스는 모두 객체(컴포넌트)와 외부 세계(객체가 사용되는 컨텍스트) 간의 계약으로 정의할 수 있습니다.**

 

 

결국 정의에 대해 엄격하고 굴하지 않는 것이 아니라 문제를 해결하기 위해 일반적인 원칙을 적용하는 것입니다.

ISP가 목표로 하는 문제를 더 잘 설명하기 위해 다음 예제에서는 TypeScript를 사용합니다.

비디오 목록을 렌더링하는 응용 프로그램을 고려해 보겠습니다.

```
type Video = {
  title: string
  duration: number
  coverUrl: string
}

type Props = {
  items: Array<Video>
}

const VideoList = ({ items }) => {
  return (
    <ul>
      {items.map(item => 
        <Thumbnail 
          key={item.title} 
          video={item} 
        />
      )}
    </ul>
  )
}
```

------

각 항목에 사용하는 **Thumbnail** 컴포넌트는 다음과 같습니다.

```
type Props = {
  video: Video
}

const Thumbnail = ({ video }: Props) => {
  return <img src={video.coverUrl} />
}
```

------

이것은 업데이트된 VideoList 구성요소입니다.

**Thumbnail 컴포넌트는 매우 작고 간단하지만 한 가지 문제가 있습니다.**

전체 비디오 개체가 prop으로 전달되는 반면 속성 중 하나만 사용하는 것입니다.

 

이것이 문제가 되는 이유를 알아보기 위해

동영상 외에도 라이브 스트림에 대한 미리보기 이미지도 표시하기로 결정하고

두 종류의 미디어 리소스가 동일한 목록에 혼합되어 있다고 상상해 보십시오.

라이브 스트림 객체를 정의하는 새로운 타입을 도입합니다.

```
type LiveStream = {
  name: string
  previewUrl: string
}
```

------

이것은 업데이트된 VideoList 컴포넌트입니다.

```
type Props = {
  items: Array<Video | LiveStream>
}

const VideoList = ({ items }) => {
  return (
    <ul>
      {items.map(item => {
        if ('coverUrl' in item) {
          // it's a video
          return <Thumbnail video={item} />
        } else {
          // it's a live stream, but what can we do with it?
        }
      })}
    </ul>
  )
}
```

------

 

보시다시피 여기에 문제가 있습니다.

비디오와 라이브 스트림 개체를 쉽게 구분할 수 있지만

비디오와 라이브 스트림이 호환되지 않기 때문에 후자를 바로 Thumbnail 컴포넌트에 전달할 수 없습니다.

 

첫째, 타입이 다르기 때문에 TypeScript는 즉시 불평할 것입니다.

둘째, 다른 속성명 아래에 썸네일 URL이 포함되어 있습니다.

비디오 객체 내부의 coverURL, liveStream 아래의 coverURL입니다.

썸네일 컴포넌트는 Video만 받는데, 라이브스트림을 Video로 변환해야겠네요?

 

**이것이 컴포넌트가 실제로 필요한 것보다 더 많은 props에 의존하는 문제의 핵심입니다.**

즉 재사용 가능성이 줄어듭니다.

 

수정하겠습니다.

**Thumbnail 컴포넌트를 리팩터링하여 필요한 prop에만 의존하는지 확인합니다.**

```
type Props = {
  coverUrl: string
}

const Thumbnail = ({ coverUrl }: Props) => {
  return <img src={coverUrl} />
}
```

------

이 변경으로 이제 비디오와 라이브 스트림의 썸네일을 렌더링하는 데 사용할 수 있습니다.

```
type Props = {
  items: Array<Video | LiveStream>
}

const VideoList = ({ items }) => {
  return (
    <ul>
      {items.map(item => {
        if ('coverUrl' in item) {
          // it's a video
          return <Thumbnail coverUrl={item.coverUrl} />
        } else {
          // it's a live stream
          return <Thumbnail coverUrl={item.previewUrl} />
        }
      })}
    </ul>
  )
}
```

------

**인터페이스 분리 원칙은 시스템 구성 요소 간의 종속성을 최소화하여 컴포넌트가 덜 결합되어 더 많이 재사용할 수 있도록 합니다.**

(사용되는 컨텍스트와 소프트웨어의 분리)

<br>

<br>

#### 참고링크: [리액트에 SOLID 원칙 적용하기 (tistory.com)](https://itchallenger.tistory.com/entry/리액트에-SOLID-원칙-적용하기)

<br>