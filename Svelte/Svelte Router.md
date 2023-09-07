# 🚂 Svelte Router

- `[완성 소스]` : https://github.com/pahkey/fastapi-book/tree/v2.05.2
- `[변경 내역]` : https://github.com/pahkey/fastapi-book/commit/59bf63d9e7a0df718111bbfd692bad7c12c27b04

질문 목록 화면을 작성했으니 이제 질문 상세 화면을 작성할 차례이다. 하지만 다음으로 진행하기 전에 해결해야 할 것이 있다.

- [필요한 화면들](https://wikidocs.net/176335#_1)

- [svelte-spa-router 설치하기](https://wikidocs.net/176335#svelte-spa-router)

- 라우터 적용하기

  - [routes 디렉터리 생성하기](https://wikidocs.net/176335#routes)
  - [Home.svelte 파일 작성하기](https://wikidocs.net/176335#homesvelte)
  - [App.svelte 파일 수정하기](https://wikidocs.net/176335#appsvelte)

- [동작 확인](https://wikidocs.net/176335#_3)

  

  <br>

## 필요한 화면들

질문 답변 사이트인 파이보는 다음과 같은 화면들이 필요하다.

- 질문 목록 - 질문의 목록을 표시하는 화면
- 질문 상세 - 질문의 상세 내용을 확인하고 답변을 작성하는 화면
- 질문 작성 - 질문을 작성하는 화면
- 질문 수정 - 질문을 수정하는 화면
- 답변 수정 - 답변을 수정하는 화면
- 회원 가입 - 회원 가입을 위한 화면
- 로그인 - 로그인을 위한 화면

하지만 Svelte는 SPA이기 때문에 단 하나의 페이지에서만 내용을 달리하여 표시해야 한다.

> SPA(Single Page Application)란 웹 사이트의 전체 페이지를 하나의 페이지에 담아 동적으로 화면을 바꿔가며 표현하는 것을 말한다.

하나의 페이지에서 위와 같은 화면들을 바꾸어가며 만들려면 코드가 복잡해진다. 이런 경우 Svelte의 svelte-spa-router를 사용하면 간단히 해결할 수 있다.

<br>

## svelte-spa-router 설치하기

Svelte의 라이브러리중 하나인 `svelte-spa-router`를 설치하고 사용해 보자. VSCode 터미널에서 동작중인 서버를 중지시키고 `npm install svelte-spa-router` 명령을 실행하여 `svelte-spa-router`를 설치하자.

- svelte-spa-router - https://github.com/ItalyPaleAle/svelte-spa-router

```
[VSCode 터미널]
frontend % npm install svelte-spa-router
```

설치 후에는 `npm run dev` 명령으로 서버를 다시 시작하자.

<br>

## 라우터 적용하기

라우터를 적용하려면 이 챕터에서 처음에 살펴 보았던 필요한 화면들 각각에 대한 URL주소 네이밍이 필요하다. 예를 들어 질문 작성 화면은 `http://127.0.0.1:5173/question-create` 와 같은 URL 주소 이름이 필요한 것이다.

파이보는 각각의 화면에 다음과 같은 URL 규칙을 지정할 것이다.

| URL명                         | 파일명                | 화면명    |
| :---------------------------- | :-------------------- | :-------- |
| /                             | Home.svelte           | 질문 목록 |
| /detail/:question_id          | Detail.svelte         | 질문 상세 |
| /question-create              | QuestionCreate.svelte | 질문 작성 |
| /question-modify/:question_id | QuestionModify.svelte | 질문 수정 |
| /user-login                   | UserLogin.svelte      | 로그인    |
| /user-create                  | UserCreate.svelte     | 회원가입  |
| /answer-modify/:answer_id     | AnswerModify.svelte   | 답변 수정 |

> `/detail/:question_id` 에서 `:question_id` 는 가변적인 변수로 `/detail/2` 처럼 호출되었을 때 question_id 변수에 2라는 값이 대입된다는 의미이다.

해당 URL을 호출하면 그에 매핑되는 svelte 파일이 화면을 렌더링하도록 설계할 것이다. 예를 들어 `/` 에 해당되는 주소가 요청되면 Home.svelte 파일이 동작하여 화면을 생성해야 한다. 지금은 질문 목록 화면만 작성한 상태이므로 질문 목록만 등록하여 시작해 보자. 이러한 URL 규칙은 App.svelte 파일에 작성해야 한다.

<br>

### routes 디렉터리 생성하기

하지만 App.svelte 파일을 수정하기에 앞서 App.svelte 파일을 Home.svelte 파일로 복사해야 한다. 왜냐하면 App.svelte 파일에는 이미 질문 목록 화면이 구현되어 있기 때문이다. 그리고 Home.svelte와 같은 URL주소와 매핑되는 파일들을 따로 관리하기 위해 다음과 같이 src 디렉터리 하위에 routes 디렉터리를 먼저 생성하자.

![img](https://wikidocs.net/images/page/176335/O_2-05_3.png)



<br>

### Home.svelte 파일 작성하기

그리고 생성한 routes 디렉터리에 Home.svelte 파일을 다음과 같이 만들자.

```
[파일명: projects/myapi/frontend/src/routes/Home.svelte]
<script>
    let question_list = []

    function get_question_list() {
        fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
            response.json().then((json) => {
                question_list = json
            })
        })
    }

    get_question_list()
</script>

<ul>
    {#each question_list as question}
        <li>{question.subject}</li>
    {/each}
</ul>
```

App.svelte 파일의 내용을 변경없이 그대로 복사했다.

<br>

### App.svelte 파일 수정하기

그리고 App.svelte 파일을 다음과 같이 수정하자.

```
[파일명: projects/myapi/frontend/src/App.svelte]
<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"

  const routes = {
    '/': Home,
  }
</script>

<Router {routes}/>
```

`/` 주소에 매핑되는 컴포넌트로 `<Home />`을 등록했다. 여기서 `<Home />`은 새로 작성한 Home.svelte 파일의 내용을 의미한다. 이 후 추가되는 URL 규칙들도 routes 변수에 추가하면 된다.

<br>

## 동작 확인

이렇게 수정하고 `http://127.0.0.1:5173/` 사이트에 접속해 보자. 이전과 동일한 질문 목록이 나타날 것이다.

![img](https://wikidocs.net/images/page/176335/O_2-05_4.png)

`/` 주소에 해당하는 Home.svelte가 호출되어 화면에 표시된 것이다.

<br>

<br>

#### 참고링크: [2-05-2 스벨트 라우터 - 점프 투 FastAPI (wikidocs.net)](https://wikidocs.net/176335)

<br>