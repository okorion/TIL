# SvelteKit 라우팅 +page와 +layout 사용 방법(SvelteKit 1.0 기준)

2022-11-11 by [나루](https://osg.kr/author/onlylovenet)

SvelteKit이 지난 12월 14일 1.0 출시를 했습니다. 기존에는 아무래도 1.0 출시 이전이라 페이지 라우팅 방식에 변경이 있었습니다. 이제는 1.0 출시를 했으니 안정이 좀 됐다고 봐도 괜찮을 것 같습니다. 그럼 SvelteKit 라우팅 +page, +layout 사용 방법을 알아보겠습니다.

<br>

## 목차

[SvelteKit 라우팅 방식의 변경](https://osg.kr/archives/674#svelte-kit-라우팅-방식의-변경)[라우팅 경로 = 디렉토리 경로](https://osg.kr/archives/674#라우팅-경로-디렉토리-경로)[+page.svelte](https://osg.kr/archives/674#page-svelte)[+layout.svelte](https://osg.kr/archives/674#layout-svelte)[중첩 +layout](https://osg.kr/archives/674#중첩-layout)[관련 자료](https://osg.kr/archives/674#관련-자료)[같이 읽으면 좋은 글](https://osg.kr/archives/674#같이-읽으면-좋은-글)

<br>

## SvelteKit 라우팅 방식의 변경

기본 라우팅 페이지를 index.svelte로 사용했던 적이 있었습니다. 하지만, 현재는 +page.svelte를 인덱스 페이지로 사용하고 있습니다. __layout.svelte도 +layout.svelte로 변경되었습니다. 그래서 다른 블로그나 유튜브 등에 아직도 과거에 작성했던 코드들이 혼란을 주는 지점이 있습니다.

이제 정식으로 1.0 릴리즈를 했다는 것만으로도 안정감이 느껴집니다. 이처럼, +page와 +layout으로 파일명을 사용하는 간단한 라우팅 방식은 매우 맘에 드네요.
그러면 SvelteKit의 라우팅 구조를 간단히 살펴보겠습니다.

<br>

## 라우팅 경로 = 디렉토리 경로

SvelteKit에서는 디렉토리 경로를 그대로 라우팅 경로로 사용합니다.

src/routes/+page.svelte 파일이 바로 루트 경로(/)가 됩니다.
src/routes/about/+page.svelte 파일은 /about 이라는 경로가 됩니다.

그럼 +page.svelte 파일이 무엇인지 확인해 봅시다.

<br>

## +page.svelte

우선 src/routes 하위 디렉토리에 있는 모든 +page.svelte가 index 파일의 역할을 합니다.

<br>

## +layout.svelte

웹 페이지의 공통 레이아웃에 대한 설정입니다. 아래 코드는 SvelteKit 공식문서에서 가져왔습니다.



```svelte
<nav>
  <a href="/">홈페이지</a>
  <a href="/about">오솔길은?</a>
  <a href="/settings">설정</a>
</nav>

<slot></slot>
```



위의 코드에서 nav 영역은 공통으로 들어가는 부분이고, slot이 각 페이지마다 다르게 들어가는 부분입니다. 위와 같이 +layout을 설정하면, 네비게이션이 모든 페이지에 공통으로 들어가고 각 페이지는 slot에 들어가게 됩니다.



```svelte
<h1>홈페이지</h1>
```



홈페이지를 위와 같이 작성하고, 이제 아래와 같이 /about 페이지를 작성해 보겠습니다.



```Svelte
<h1>오솔길은?</h1>
```



/about를 브라우저로 열면, 다음과 같이 slot 부분에 src/routes/about/+page.svelte의 내용이 들어갑니다.



```svelte
<nav>
  <a href="/">홈페이지</a>
  <a href="/about">오솔길은?</a>
  <a href="/settings">설정</a>
</nav>

<h1>오솔길은?</h1>
```



<br>

## 중첩 +layout

+layout을 각 라우팅에서 사용하면 중첩하여 사용할 수 있습니다. 이를테면, src/routes/about/+layout.svelte를 작성하면, about 하위에 있는 +page는 해당 레이아웃을 추가 적용받게 된다.
예를들어 about 하위에 introduction 이라는 페이지가 더 있는 경우 +layout가 있다고 가정해 봅시다.



```svelte
<nav>
  <a href="/about">오솔길은?</a>
  <a href="/about/introduction">소개</a>
<nav>

<slot></slot>
```



그리고 introduction을 다음과 같이 작성해 줍니다.



```svelte
<h1>소개</h1>
```



브라우저에서 /about/introduction을 열면 아래와 같은 페이지가 열립니다.



```svelte
<nav>
  <a href="/">홈페이지</a>
  <a href="/about">오솔길은?</a>
  <a href="/settings">설정</a>
</nav>

<nav>
  <a href="/about">오솔길은?</a>
  <a href="/about/introduction">소개</a>
<nav>

<h1>소개</h1>
```



스타일링만 잘 해 주면 사용자가 접근하기 좋은 네비게이션이 완성되겠죠.

<br>

## 관련 자료

SvelteKit을 처음 사용하면서 저는+page.svelte가 뭐지? 하는 궁금함에 공식 문서 확인하다가 알게 됐습니다. 자세한 내용은 https://kit.svelte.dev/docs/routing을 확인하시면 됩니다.
SvelteKit 라우팅 개념을 잡는데 도움이 되길 바랍니다.

<br>

## 같이 읽으면 좋은 글

- [slot tag 이용하여 svelte 컴포넌트에 HTML TAG 전달받기](https://osg.kr/archives/662)
- [vite 호스트와 포트 설정하기(feat. cli 명령어)](https://osg.kr/archives/648)
- [vite로 Svelte 배포용 빌드하고 테스트 서버 띄우는 방법](https://osg.kr/archives/653)





<br>

<br>

참고링크: [SvelteKit 라우팅 +page와 +layout 사용 방법(SvelteKit 1.0 기준) - 오솔길 (osg.kr)](https://osg.kr/archives/674)

<br>