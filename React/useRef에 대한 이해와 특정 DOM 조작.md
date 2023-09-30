## 🌼 useRef에 대한 이해와 특정 DOM 조작

목차

1. 브라우저에서 Javascript의 존재 이유는 DOM 조작이다. 

2.Javascript로 특정 DOM을 선택하는 방법은?

3. React에서는 특정 DOM을 어떻게 조작하는가?
4. React의 가상 DOM과 상호 작용하며 실제 DOM 조작하기

  4-1. useRef 예제: useRef와 useState 함께 활용

5. useState와 useRef의 실질적인 차이점은?

 

## useRef에 대한 이해와 특정 DOM 조작 (부제: useRef로 특정 DOM 선택하기)

*(\* 이해의 흐름을 바탕으로 작성한 글이기에 지식을 뽑기보다 천천히 정독함을 권장해드립니다. )*

필자는 useRef가 useState와 useEffect처럼 한 번에 이해되지 않았다. 드디어 이해했기에 글을 작성해본다.

 

#### **TODO: "특정 DOM 객체 찾기 - 선택 - 조작"**

 

### 1. 브라우저에서 Javascript의 존재 이유는 DOM 조작이다. 

어떤 이벤트를 받아 처리하고 객체를 움직이거나 변화하는 모든 DOM의 조작은 js를 사용함으로써 정적 정체성을 벗어난다. 

HTML과 CSS를 배우고 난 뒤, "JS를 통해 동적인 웹페이지를 만들어보아요!~"와 같은 희미한 기억이 있을테다. 

물론, CSS를 이용하여 약간의 움직임을 첨가할 수 있지만, 다양한 이벤트 핸들링과 복잡한 처리는 불가능하다.

 



![img](https://blog.kakaocdn.net/dn/pTX9H/btsn0FSCcfP/ib5IgFT8SPJlK7kF4zW4Lk/img.png)요약: 브라우저는 Javascript를 알아듣게 설계됨 ! / 출처: Javascript 기초 https://bo5mi.tistory.com/91



 

### 2. Javascript로 특정 DOM을 선택하는 방법은?

여기서 본분을 잊지 않고 짚어보자면, 우리는 특정 DOM을 선택해야한다.
Javascript에서 특정 DOM을 선택하는 방법은 **getElementById**, **querySelector** 같은 DOM Selector 함수를 사용해서 DOM을 선택한다.

 



![img](https://blog.kakaocdn.net/dn/bFzH1R/btsnZIh1KbX/AL9ffPVK5wXAKNaeSUISek/img.png)getElementById,&nbsp; querySelector를 찾아보면서 알게 된 점: getElementById는 BFS로, querySelector는 DFS로 구현되어있으며, 해당 메서드를 BFS, DFS알고리즘을 통해 구현할 수 있다. 출처: https://dev.to/ohpyupi/using-dfs-to-implement-getelementbyid-blo



 

그렇다면 Javascript가 아닌 React에서

**1)** 특정 엘리멘트의 크기를 가져오기 / **2)** 스크롤바의 위치를 가져오거나 설정 / **3)** input에 포커스 설정 과 같은

 

React에서 특정 DOM을 직접 선택해야하는 상황이 있을 경우, **useRef**를 사용해서 DOM을 선택한다.

**"아! 특정 DOM을 직접 선택하려면 useRef를 사용하면 되는구나" 를 넘어서
\*"왜 이렇게 사용하는가?"\* 를 이해하기 위해서는 React에서 DOM을 어떻게 조작하는지 알아야한다.** 

 

### 3. React에서는 DOM을 어떻게 조작하는가?

리액트는 렌더링을 하며 virtual DOM이라 불리는 가상 DOM을 먼저 만들고, 가상 DOM과 실제 DOM을 비교하여 차이가 있는 부분만 리렌더링 하는 방식을 통해 효율적으로 처리한다. 이러한 설계 방식은 DOM의 재사용성을 극대화하는 React의 철학을 보여준다. 

 

만약 여기서 React에 useRef가 없다고 가정하고, getElementById를 통해 특정 DOM을 선택했을 때 재사용성에 문제가 발생한다.

**id**는 **DOM의 개별 노드에 고유성을 부여**해주기 위해 사용되는데, **React의 재사용성 철학과 충돌한다.** 

그런데 이 getElementById가 쓰인 컴포넌트에 속한 DOM 노드에 id가 부여되면**,** **컴포넌트를 재사용할 때마다 해당 id를 가진 DOM이 복제되고, 이로 인해 id는 그 고유성을 잃게 된다.** 이러한 문제 때문에 useRef를 사용하여 DOM 요소에 접근하면, **컴포넌트를 재사용할 때마다 DOM 요소의 참조가 변경되지 않아 문제가 발생하지 않는다.**

 

***"useRef는 .current 프로퍼티를 전달된 인자(initialValue)로 초기화된 변경 가능한 ref 객체를 반환합니다.
반환된 객체는 \*컴포넌트의 전 생애주기를 통해 유지될 것입니다."***

 

### 4. React의 가상 DOM과 상호 작용하며 실제 DOM 조작하기

**React의 가상 DOM과 상호 작용하며 실제 DOM을 조작하는 방법**은

바로, **"useRef"**이다. useRef는 React의 가상 DOM과 재사용성 철학과 잘 어울리는 기능이다.

 

useRef를 반환된 ref 객체를 요소에 할당하면 해당 컴포넌트의 생애주기 동안 ref가 정의된 컴포넌트의 context 안에서 유일성을 보장하는 역할을 수행하게 되고, **이 때 반환된 객체의 .current 프로퍼티(값)를 통해 DOM의 직접 조작이 가능해진다.** 

**(그렇다면 여기서 DOM은 virtual DOM이 아니라 실제 그려지는 DOM(Real DOM) 이군!)**

 

### 4-1. useRef 예제: useRef와 useState 함께 활용



![img](https://blog.kakaocdn.net/dn/bIV1oJ/btsnTCwceQI/AKp3p8DtowlEKkvHLFo6I0/img.png)



<iframe src="https://play-tv.kakao.com/embed/player/cliplink/439636495?service=daum_tistory" width="150" height="148" frameborder="0" allowfullscreen="true" style="max-width: 100%; display: block; margin: 0px; width: 800px; height: 789.333px;"></iframe>

위 코드를 실행했을 때의 결과이다. input에 값을 입력했을 때, 상태가 변경함에 따라 Preview가 변경되는 것을 확인할 수 있다. 

### 5. useState와 useRef의 실질적인 차이점은?

처음에는 useStae와 useRef가 어디서 쓰이는지가 헷갈릴 수 있다.

헷갈리지 않기 위한 핵심은 **바로 렌더링에 관여하는지 여부** 이다.

 

.current 프로퍼티의 변경은 어디에서도 관찰 가능하지 않으며, 따라서 렌더링을 발생시키지 않는다. 이에 반해 state는 useState를 호출하는 순간 비동기적으로 state를 업데이트함에 따라 컴포넌트를 리렌더링 한다. 이러한 맥락에서 state와 ref는 차이를 갖게 된다.

 

아래 사진은React 공식 문서에서의 useRef 부분의 일부이다.

해석하자면, *ref.current 프로퍼티를 바꿀 때, React는 컴포넌트를 리렌더링 하지 않는다. ref는 분명한 자바스크립트 객체이기 때문에 리액트는 ref.current 프로퍼티를 바꾼 것을 인지하지 못한다.* (왜냐? 실제 DOM을 조작하기 때문!)

 



![img](https://blog.kakaocdn.net/dn/2ZeKQ/btsnYYlojuZ/OR8RzsfKtWvQXwxmDgIxR0/img.png)출처: React 공식 문서&nbsp;https://react.dev/reference/react/useRef



 

정리하자면, React에서 상태 관리 라이브러리나 (ex. redux, zustand ..) **useState를 통해 참조하는 값이 변경되면 해당 값을 참조하는 컴포넌트를 리렌더링시킨다.** 여기서, **참조하는 값이 변경되더라도 리렌더링이 필요하지 않은 경우는 useRef를 사용하면 된다!** 

(또 다른 특징: state는 component의 props로 전달하는 등의 방법을 통해 외부에서 context 접근이 가능하지만, useRef를 통해 생성된 ref의 조작은 useRef가 정의된 컴포넌트의 내부에서만 가능하다.)

------

***"useRef는 .current 프로퍼티를 전달된 인자(initialValue)로 초기화된 변경 가능한 ref 객체를 반환합니다.
반환된 객체는 \*컴포넌트의 전 생애주기를 통해 유지될 것입니다."***

 

*컴포넌트의 전 생애주기

: 컴포넌트가 마운트되어 생성되고, 업데이트되고, 언마운트 되기까지의 모든 단계를 포함하는 개념이다. 

1. **마운트(Mount)**: **컴포넌트가 DOM에 삽입되는 초기 단계**

: 컴포넌트가 처음으로 렌더링될 때 useRef를 사용하여 생성된 ref 객체는 컴포넌트 인스턴스와 함께 생성되며, 컴포넌트의 생명주기 동안 유지된다. 

 

2. **업데이트(Update)**: **컴포넌트가 업데이트 되는 단계**

: 업데이트는 컴포넌트의 상태(state) 또는 속성(props)가 변경되었을 때 발생한다. useRef로 생성된 ref 객체는 컴포넌트 업데이트 과정에서 유지되므로, 업데이트가 발생해도 ref 객체는 변경되지 않는다. 

 

3. **언마운트(Unmount): 컴포넌트가 DOM에서 제거되는 단계**

: 컴포넌트가 언마운트 되면 useRef로 생성된 ref 객체도 함께 소멸된다. 

 

 

Reference

책: 리액트를 다루는 기술

https://react.dev/reference/react/useRef

[https://eleste.tistory.com/14?category=833321 ](https://eleste.tistory.com/14?category=833321)

 

 

결론

\- Javascript로 특정 DOM을 선택하는 방법: **getElementById or querySelector 이용**

\- React에서는 특정 DOM을 조작 방법: **useRef 이용**

\- **useRef<?> : Typescript 이용 시, useRef 훅이 참조하는 DOM 요소의 타입 지정 필요**

\- useState와 useRef의 실질적인 차이점은? : **참조값 변경 시, useState 리렌더링 O / useRef 리렌더링 X** 



<br>

<br>

#### 참고링크: [[React\] useRef에 대한 이해와 특정 DOM 조작 (부제: useRef로 특정 DOM 선택) (tistory.com)](https://bo5mi.tistory.com/215)

<br>