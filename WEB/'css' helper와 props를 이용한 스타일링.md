## 📇 'css' helper와 props를 이용한 스타일링

이 포스트는 Udemy 사이트에 올라 온 Tom Phillips의 "React styled-components v5 (2021 edition)" 강의를 듣고 정리한 것입니다.

 

🔗링크

https://www.udemy.com/course/react-styled-components/

 

React styled components v5 (2021 edition)

Ditch CSS stylesheets! Learn CSS in JS to quickly and cleanly style React components with the styled components library

www.udemy.com

 

 

 

 

 

 

### **📝 목표**

styled-component의 'css' 헬퍼를 이용해서

props의 조건에 따른 스타일링을 속성을

좀더 보기 쉽게 작성하기

 

 

 

 

 

#### **📂 components > App.js**

```
function App() {
	return (
		<>
			<GlobalStyle />
			<h1>App.js</h1>
			<Button>Primary Button</Button>
			<Button secondary>Secondary Button</Button>
			<Button large>Large Button</Button>
		</>
	);
}
```

첫 번째 버튼은 props가 없는 가장 기본 버튼.

두 번째 버튼에는 secondary라는 props를

세 번째 버튼에는 large라는 props를 넣어줬다.

 

 

 

 

 

 

#### **📂 components > common > Button.js**

 

 

**'css' 헬퍼를 사용하지 않는 경우**

모든 속성마다 interpolate function을 넣어준다.

```
const Button = styled.button`
	background-color: ${(props) => (props.secondary ? "black" : "#f8049c")};
	font-size: ${(props) => (props.large ? "1.5em" : "1em")};
	padding: ${(props) => (props.large ? "10px" : "8px")};
	border-radius: ${(props) => (props.large ? "8px" : "4px")};
`;
```

 

 

**'css' 헬퍼를 사용하면**

```
import styled, { css } from "styled-components";



const Button = styled.button`
	${(props) =>
		props.large
			? css`
					padding: 10px;
					border-radius: 5px;
					font-size: 1.5em;
			  `
			: css`
					padding: 8px;
					border-radius: 4px;
					font-size: 1em;
			  `}
`;
```

 

 

우선 'css' 헬퍼를 styled-components로부터 import해줘야한다!!!

그리고 props에 따라

즉, props.large가 true일 때의 padding, border-radius, font-size와

false일 때의 padding, border-radius, font-size를 하나로 묶어서(!) 

보기 쉽게 스타일링 할 수 있다!

 

 

 

 

 

 

 

 

### **🌞 정리**

이렇게 styled-components의 'css' helper를 사용하면

각각의 css 속성마다 interpolate function을 선언해서 props 조건에 맞게 렌더링하는 것이 아니라

**하나의 interpolate function 안에서** props에 따라 렌더링할 수 있다.

 



<br>

<br>

#### 참고링크: ['css' helper와 props를 이용한 스타일링 (tistory.com)](https://yumyumlog.tistory.com/244)

<br>