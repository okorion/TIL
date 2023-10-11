# 🏗️ env 파일에 대하여

## env ??

- 웹,앱 개발을 하다보면 포트, DB관련 정보, API_KEY등.. 개발자 혼자서 또는 팀만 알아야 하는 값 즉, git, 오픈소스에 올리면 안되는 값들이 있습니다.
- 이때 필요한 것이 **dotenv 패키지** 이며 환경변수 파일을 외부에 만들어 URL,포트, API_KEY등.. 을 저장시켜 소스코드 내에 하드코딩하지 않고 사용 할 수 있습니다.

## .env 파일

- .env 파일은 프로젝트의 최상위 루트에 파일을 만듭니다.
- 외부 파일(.env)에 환경변수를 정의하여 변수로 받아오는 이유는 보안과 유지보수에 용이하기 때문 입니다.

## .env 파일 사용법

- .env.{mode명}

- .env.--- 파일의 내용을 수정하면 npm 으로 다시 시작해야합니다.

  

## React 에서 .env 사용하기

- `process.env.REACT＿APP＿` 는 예약어이므로, 다른 이름은 사용하면 React가 인식하지 않습니다.

### .js

```js
const abc = {
	key : process.env.REACT_APP_지정한 변수
}
```

### .env

```js
REACT_APP_지정한 변수 = 값
```

## .env 활용 모듈 - dotenv

- nodeJS 의 모듈로, npm 을 사용해 설치하고 사용 할 수 있습니다.
- dotenv 를 사용해 현재 디렉토리에 위치한 .env 파일로부터 환경 변수를 읽어 낼 수 있습니다.
- `npm install dotenv`

## require("dotenv").config();

- 애플리케이션이 작동될 때 가장 먼저 실행되는 js파일의 최상단에서 config() 함수를 호출 하면 .env파일에 저장된 환경 변수를 process.env 모듈을 통해 불러올 수 있습니다.

## 정리

- env 파일은 " 환경 변수 파일 " 을 의미한다.
- 이 파일은, 애플리케이션이 실행될 때 넘기고 싶은 특정 값을 담고 있는 변수가 기록되어 있다.
- 미리 정의된 값을 애플리케이션에서 활용하고 싶을 때 이 .env 파일을 활용한다.

## 참고

- https://carmack-kim.tistory.com/110
- [https://velog.io/@jhyounyaho/env-%ED%8C%8C%EC%9D%BC](https://velog.io/@jhyounyaho/env-파일)
- https://code-designer.tistory.com/102
- [hoje15v.log](https://velog.io/@hoje15v/환경변수-관리해주는-.env-파일-만들기)



<br>

<br>

#### 참고링크: [env 파일에 대하여 (velog.io)](https://velog.io/@hoho_0815/env-파일에-대하여)

<br>