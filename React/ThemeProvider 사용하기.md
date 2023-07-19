## 🍝 ThemeProvider 사용하기

**1.**

styled-components에서 ThemeProvider를 import한다.

```react
import { ThemeProvider } from "styled-components";
```

<br>

**2.**

ThemeProvider 컴포넌트를 가장 상위 컴포넌트로 

(GlobalStyle보다 위에)

```react
function App() {
	return (
		<ThemeProvider>
			<GlobalStyle />
			<BrowserRouter>
				<Switch>
					<Route path="/login">
						<LogIn />
					</Route>
					<Route path="/">
						<Home />
					</Route>
				</Switch>
			</BrowserRouter>
		</ThemeProvider>
	);
}
```

<br>

**3.**

theme이라는 이름을 가진 비어있는 객체를 만든다.

```javascript
const theme = {}
```

<br>

**4.** 

위에서 생성한 theme 객체를 ThemeProvider의 props로 넣어준다.

```react
function App() {
	return (
		<ThemeProvider theme={theme}>
			<GlobalStyle />
			<BrowserRouter>
				<Switch>
					<Route path="/login">
						<LogIn />
					</Route>
					<Route path="/">
						<Home />
					</Route>
				</Switch>
			</BrowserRouter>
		</ThemeProvider>
	);
}
```

이렇게 해주면

styled-components가 모든 컴포넌트에 이 theme 변수를 inject해준다!

<br>

**5.**

원하는 theme 작성하기

(Object니까 camelCase)

```react
const theme = {
	primaryColor: "#f8049c",
	secondaryColor: " #fdd54f",
};
```

색깔을 넣어봤다!

그러면 이제부터 hex 값을 넣어주는 대신에

hex 값을 넣었던 자리에

```react
${props => props.theme.primaryColor}
```

이런 식으로 넣어주면 된다.

<br>

<br>

#### **🌞 예시**

```react
background-color: ${(props) =>
	props.secondary
		? props.theme.secondaryColor
		: props.theme.primaryColor};
```

 

```react
border-bottom: 3px solid ${(props) => props.theme.secondaryColor};
```

 

```react
const HeaderWrapper = styled.header`
	box-sizing: border-box;
	display: flex;
	height: 60px;
	width: 100%;
	padding: 0 16px;
	position: fixed;
	top: 0;
	background-image: linear-gradient(
		to right,
		${(props) => props.theme.primaryColor},
		${(props) => props.theme.secondaryColor}
	);
	border-bottom: 3px solid #fdd54f;
`;
```

 <br>

<br>

#### 참고링크: [ThemeProvider 사용하기(1) - 기본 문법 (tistory.com)](https://yumyumlog.tistory.com/252)

<br>