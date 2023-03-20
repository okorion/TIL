react로 구현을 하다보면, useState를 활용하여 데이터를 저장하고 수정한다. state란 한국어로 상태이다. 즉, 이러한 상태관리인 데이터관리를 효율적으로 하는 방법에 대해 알아보자. 당연한 말이지만, 상태 설계는 개발자마다 중요하게 생각하는 부분이 다르기 때문에 정답은 없다. 그리고 상태 설계는 한번 설계되어 프로젝트가 진행되면 고치기가 쉽지 않다. 따라서 상태 관리에 대한 많은 고민을 하고 프로젝트를 시작해야한다. 잘못된 상태 설계는 성능 이슈는 물론 유지보수 관점에서도 큰 영향을 끼친다.

 

 우선은 리액트를 기준으로 상태 관리에 대해 적어보려한다. 기본적으로 redux를 사용하지 않으면 우리는 데이터를 props로 컨포넌트간에 전달을 시켰다. 이러한 데이터는 전달된 컴포넌트에 국한 되어 영향을 주는 **지역 상태**라 할 수 있다. 그리고 redux와 같이 많은 컴포넌트에 영향을 주는 **전역 상태**가 있다. 이 글에서 이야기 하고자 하는 부분은 전역 상태와 관련이 있다. 또한 실무에서는 데이터(상태) 관리시 보안이 굉장히 중요하다. 이러한 컨셉을 잡고 이야기를 풀어나가 보겠다.

 



![img](https://blog.kakaocdn.net/dn/YRlaG/btrDHee8hs0/ojwdP69ZZKyUEz0rpnQ1D1/img.png)



 

전역 상태 라이브러리로 Redux가 여전히 대세로 쓰이고 있고 많은 프로젝트에서 전역 상태가 무분별하게 사용되고 있다. 점차 전역 상태 라이브러리를 안쓰는 게 좋다는 흐름이 생기고 있고 리액트 팀에서는 Recoil을 만들어서 기존의 전역 상태 라이브러리를 대체 하려고 하고 있다. 리액트의 상태 관리가 어떻게 진행되어 왔고 어떻게 진행 되려고 하고 있는지 또, 어떤 식으로 설계되는게 추천 되는지 써보려고 한다.

 

 

------

 

### react와 함께 사용하는 상태관리 라이브러리

초입자의 관점에서 react를 처음 접해 코딩을 하다보면, 어느 순간 데이터를 다루기가 힘든 시점이 있을 것이다. 그때가 바로 state management(상태관리)에 대해 생각해 볼 시점이다. 기본적으로 react는 사이드 이펙트를 원하지 않는다. 그리고 리액트 생태계 대부분은 컴포넌트이고, prop으로 시작해 리액트 엘리먼트를 반환하는 순수함수를 따른다. 즉, react에서는 비동기 같은 side effect가 존재하지 않아야 하지만, **side effect가 없는 서비스 개발을 할 수 없다.** 따라서 앞의 문제를 해결하고 상태 관리를 위해서 redux, react-saga, react-thunk, redux, Mobx, Zustand, SWR, React-Query 등등 **굉장히 많은 라이브러리들이 react와 함께 사용되고 있다.** 그렇다면 우리가 사용하는 프로젝트에서는 무슨 라이브러리와 react를 함께 사용해야할까?

 

 



![img](https://blog.kakaocdn.net/dn/AAqve/btrDEqnhtZ0/aLMdW9uxgRTw4ToXfNcwnk/img.png)https://www.npmtrends.com/react-redux-vs-redux-vs-recoil



 

 

위의 그래프를 보면, 우리는 redux를 사용해서 상태 관리를 하는 것이 당연해 보인다. 그러나 그것이 정답일지는 아래의 글을 읽어보며 생각해 보자.

 

state관리, 즉 데이터관리는 지역 상태와 전역 상태로 나눌 수 있다. props로 데이터를 전달하는 것은 **지역 상태**이고, 다른 저장소에서 데이터를 불러온다면 **전역 상태(redux)**라고 할 수 있다. props로 가까운 컴포넌트로 데이터를 전달하는 지역 상태를 사용 하면, 컴포넌트가 복잡해질 수록 코드가 난잡해진다. 그렇다면 지역 상태가 아닌 전역 상태로 핸들링을 해야하는 것이 항상 좋을까? 그렇지는 않다. 그렇다면 상태 관리를 어떻게 하는 것이 좋은지 공식문서를 정리하면 아래와 같다.

 

1. 기본적으로 **일반적인 경우에는 지역 상태로 데이터를 관리하는 것을 권장**한다.
2. 지역 상태로 데이터를 관리 시 **다수의 컴포넌트 간에 상태 의존성이 높아진다면 전역 상태로 데이터를 관리**하는 것을 권장한다.
3. 전역 상태 관리 시 서버에서 가져오는 데이터(db)와, 단순하게 UI 상태를 나타내는 데이터는 분리하여 다룬다.
4. 서버 데이터 캐싱 시 전역 상태로 다루면 안된다. 서버 상태를 관리하려면, SWR이나 React-Query 와 같은 서버 캐싱 전용 라이브러리를 사용하는 것을 권장한다.

그렇다면 리액트가 이러한 상태가 된 역사를 보면서 어떻게 프로젝트를 적용할지 좀 더 생각해 보자.

 

 

 

### MVC (Model-View-controller)

\> 사실 초기에는 상태관리가 중요하지 않았다. 그래서 데이터가 필요한 어디든지 데이터를 주고 받고가 가능하게 구성되어 있다..

![img](https://blog.kakaocdn.net/dn/FqFLk/btrDHdN6XAS/mRBnClLT7rrMKXH1pRJPkK/img.png)

초기 상태 관리는 위와 같은 MVC 방식인 ‘양방향 데이터 흐름’으로 UI를 관리했다. 예를들면, spring, django, nodejs 백엔드에서 제공하는 템플릿 UI을 사용하는 경우이다. 위 그림을 보면 알 수 있듯 모델 하나가 변경되면, 광범위한 View 수정이 일어나야한다. 이는 모델 하나에 의존되는 뷰가 많아지면, controller에 복잡도가 올라가가 데이터 흐름을 이해하기 힘들고, 에러발생 시 관리에도 많은 시간이 든다.

MVC 방식인 다른 frontend 프레임워크와 달리 리액트는 Model, View, Controller 중에 **VIew만 제공**한다. 따라서 프레임 워크보단 라이브러리에 가깝다. 이러한 문제점을 해결하기 위해 **React**가 탄생한다.

 

 

### React

2013년에 위의 복잡도를 해결하기 위해 단방향 흐름을 가지는 react를 릴리즈한다. 이때는 reat는 전역 상태 라이브러리가 없었고, props로 하나씩 데이터를 전달을 했다. 쉽게 이야기하면, 데이터를 수정, 변경하는 비지니스로직은 벡엔드에서 하고, react는 받은 데이터를 UI 컴포넌트로 props를 활용해 보내주기만 한다. 이러한 단방향 흐름을 **Flux**라고 한다.

 

 

### Flux

> Flux의 핵심은 View로 데이터가 들어가지만, 데이터나 View에서 나오지 않는 것이다.



![img](https://blog.kakaocdn.net/dn/bKXWTZ/btrDIniEjUC/lkmKPT19OXdCYltRoIxyQK/img.png)



 

2014년 페이스북은 단방향 흐름인 Flux 아키텍처 패턴을 공개했다. 이의 핵심은 단방향 데이터 흐름을 적용한 아키텍처 패턴이다. 위의 Flux의 흐름을 간단히 설명하면 아래와 같다.

#### Flux 흐름

1. Action은 버튼을 누르는 것과 같은 이벤트의 이름이다.
2. Dispatcher는 Action에서 발생한 이벤트의 이름에 따라 처리할 행동을 알려준다.
3. Store는 데이터가 저장되어 있는 저장소이다. Dispatcher에서 받은 행동에 따라 데이터를 핸들링한다.
4. View에서는 Store에서 데이터를 받는다. 그리고 Action을 통해 이벤트를 발생은 시키지만, 데이터는 전달하지 않는다.

위의 흐름을 바탕으로 조금씩 복잡하지게 상태관리가 발전하기 시작한다. 그 후에 2015년에 React + Flux 구조에 Reducer를 결합한 **Redux**가 등장했다.

 

 

### Redux

> flux와 redux의 가장 큰 차이는 reducer의 등장이다. 간단히 말하면, Flux에서는 store가 여러개였지만, Redux에서는 하나의 store에 여러개의 reducer가 존재한다고 이해를 하면 좋다.



![img](https://blog.kakaocdn.net/dn/csQiR9/btrDESqS4LC/OP3lOmv0yP2cxiUZjnYtUk/img.png)



 

redux는 prop drilling 문제와 데이터 공유에 따른 의존성을 해결할 대안 으로 떠올랐고, state management(상태관리) 라이브러리의 대세가 되었다. redux의 장점을 요약해 보면 데이터가 Centralized 되어 있어 Predictable 하고 데이터 흐름이 단방향이라 Debuggable (디버깅이 쉽다) 하다. redux의 생태계가 구축되어 있어 필요에 맞게 Flexible하게 구현 가능하다. (비동기 하려면 redux-thunk & redux-saga 같은 라이브러리를 추가로 사용해야한다.)

 

redux의 보안 적 측면에 대해 조금 더 이해를 해보자. 기본적으로 application(web/app)은 stateless protocol을 유지하는 것이 좋다. 쉽게 이야기하면, 화면은 해커의 위험성 때문에 데이터(상태)를 client 에 두지 않는다.(정보보안법과도 연관된다.) 즉, client인 react에 데이터를 저장하면 보안상 위험하다는 의미이다. 따라서 **Client와 Server 사이에 redux라는 미들웨어를 둔다고 생각하면 된다**. 정리하면, 미들웨어인 redux와 client인 react가 데이터를 주고 받는 것이기 때문에 실질적으로 server와 client는 데이터가 무엇인지 모르고 redux만 데이터를 가지고 있다가 필요시 client의 화면에 보여주기만 하는 것이다. 이러한 이유로 redux가 사용되기도 한다.

 

reducer에 대한 이해도 조금 더 높여보자. reduce라는 단어의 뜻 자체는 '줄이다'라는 뜻이다. 즉, action으로 text가 담겨져 오면, reducer는 switch~case문으로 action의 text에 대한 선택지를 줄인다는 의미로 생각해도 좋을 것 같다. switch문으로 선택된 행동을 상태(state)에 반영을 하는 것이다.

 

### Context API

> https://ko.reactjs.org/docs/context.html

redux 이 후에 Hooks이 나오면서 비대한 Redux 대신 Context API를 활용해서 하는 개발이 권장 된다. Context API 자체는 상태관리를 Redux의 useState와 useReducer로 한다. 하지만 Redux와 가장 큰 차이점은 Provider를 나눠서 관리가 가능하고, 최상단이 아닌 관련된 컴포넌트 들의 상위에 Provider를 감싸기만 하면 되기 때문에 데이터가 필요한 컴포넌트들에서만 상태를 관리 할 수 있다.

 

그러나 사용하는 값이 변할때 리렌더링 되는 것에 최적화 되어 있는 Redux와 달리 Context API는 해당 값 외의 다른 값이 변경될때도 컴포넌트가 재호출되어 리렌더링이 발생한다. 따라서 목표 값에 따라 분리 해서 관리를 해야하는데, 목표 값이 많아 질 수록 컴포넌트가 많아져서 성능 이슈가 발생한다. 이러한 명확한 한계로 인해 리액트 팀은 **Recoil**을 만들기 시작하고 있다.

 

 

### Recoil

> https://recoiljs.org/ko/



![img](https://blog.kakaocdn.net/dn/bvuswU/btrDJwGqZnq/Pv1slHZYDliyAfnzWC5Jv0/img.png)



 

**Redux, Mobx와 달리 Recoil은 리액트 만을 위해 생긴 라이브러리**다. Recoil은 Atom이라는 작은 데이터 조각을 만들어 해당 데이터 변화 시에 이를 참고하는 컴포넌트들만 re-render 시킨다. 사용자가 많이 없기 때문에 초입자라면, redux를 먼저 사용하는 것이 좋다. 그러나 위의 공식 문서에도 사용법이 상세히 나와 있기 때문에 꼭 사용해 보자.

 

 

 

### 최고의 상태관리 라이브러리

상태관리가 필요한데 Redux, MobX, Recoil 중 어떤 것을 사용하는 것이 좋을까에 대한 고민이 필요하다. 기본적으로는 모든 상태 관리 라이브러리를 사용해 보는 것을 추천한다. redux를 사용하고 있다면, redux-thunk & redux-saga 등을 이용해 비동기 처리를 하더라도 다른 라이브러리가 더 좋진 않을까하는 고민이 항상 필요하다.

 

기본적으로는 커뮤니티가 큰 Redux로 시작하는것이 당연히 좋다. 그러나 기본적으로 상태와 변이방법을 정의하기 위한 redux와 action의 코딩량이 많은데다가, 지속적으로 로컬 스토어 상태를 원격 서버 상태와 동기화를 위한 saga같은 미들웨어가 추가되면 기능 하나당 추가해야하는 코딩량은 더 많아진다. 

 

정리하면, 사실 정답은 없다. 규모가 작다면 비교적 쉽게 적용할 수 있는 context API를 사용하는 것이 좋고, 규모가 크고 확장성이 있고 비동기처리가 필요하다면 redux, thunk, saga까지 고려가 필요하다. 하지만 무언가를 판단을 하기 위해서는 시대의 흐름에 **주류가 되는 기술(redux)을 경험해 본 후에 다른 라이브러리를 적용**해야 한다고 생각한다.

개인적인 생각을 정리하면,

1. angular : 프레임워크의 한계로 data 상태가 blackbox 되는 치명적 문제가 있어, 점유율 감소 중 => 비추
2. **react** : 치명적 문제는 아직 발견 되지 않음. 향후 5년은 문제 없음 => 추천
3. **redux**: 대표적인 react 상태관리 라이브러리 => 추천(redux toolkit 추천)
4. **redux-actions** : redux 코드를 줄여준다 => 추천
5. **react-saga** : redux의 비동기 문제인 Side Effect를 훌륭히 관리한다. => 추천
6. 위의 이유로 redux의 단점은 코드가 길어진다. 그에 따른 대안으로 SWR 이나 recoil이 나왔다.
7. SWR, recoil은 위의 추천 라이브러리를 먼저 사용한 프로젝트를 진행 후에 적용을 하는 것을 고민해 보면 좋을 것 같다.
8. **SWR**은 상태관리 툴은 아니지만, API 기능으로도 상태관리가 가능하다. => 추천

 

 

 

**React 프로젝트 구조**는 아래와 같이 진행하는 것이 개인적으로는 좋아한다.

 



![img](https://blog.kakaocdn.net/dn/EtbZk/btrDFakw7Nw/O5IMgCkJzV3SOsSAg4Isy1/img.png)



**pages :**

- router에 따른 페이지당 파일을 하나씩 넣어준다.
- token 유무 확인 로직으로 redirect 로직 추가

**containers :**

- pages에서 containers로 컴포넌트를 연결한다.
- **redux 를 연결**한다

**components** :

- containers에서 components로 컴포넌트를 연결한다
- html로직이 포함된다.

**redux** :

- 상태관리를 진행한다.

**services** :

- API관리와 localhost 관리는 진행한다.

**types** :

- typescript에 맞는 타입을 지정한다.

 

 

 

 

 

상태 관리에 대한 고민은 사실 오늘도 하고 있다. 많은 프로젝트를 사용하면서 더 추가해볼 예정이다.





참고링크: [[react\] 상태관리 기초 - 효율적으로 데이터 저장하고 수정하기 (tistory.com)](https://han-py.tistory.com/487)