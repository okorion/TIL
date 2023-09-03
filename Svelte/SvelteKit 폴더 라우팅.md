## SvelteKit 폴더 라우팅

## [폴더 방식 라우팅](https://mycodings.fly.dev/blog/2022-12-17-sveltekit-folder-routing-dynamic-routing-and-layout-page-scoped-style#폴더-방식-라우팅)

SvelteKit 라우팅 방식은 Next.js 13과 같은 폴더 방식 라우팅입니다.

제가 쓴 예전 글을 살펴보셨다면 SvelteKit이 2022년 8월 부터 폴더 방식 라우팅으로 바뀌었고, (+) 글자를 앞에 넣는다고 했었는데요.

폴더까지가 라우팅 주소가 되고 그 안에 +page.svelte 파일이 가장 기본이 되는 파일이 됩니다.

더 이상 index.svelte 파일은 사용하지 않으니 참고 바랍니다.

또 (+) 글자가 없으면 라우팅으로 인식되지 않으니 참고 바랍니다.

우리가 만들려는 블로그 시스템은 라우팅이 4개입니다.

/ ==> 루트 라우팅

/about

/blog

/contact

그러면 어떻게 폴더를 구성해야 할까요?

SvelteKit은 /src/routes 폴더 밑에 있는 걸 라우팅 하는데요.

/src/routes 폴더 밑에 해당 +page.svelte 파일을 만들면 됩니다.

먼저 루트 라우팅을 위한 /src/routes/+page.svelte 파일은 기본으로 작성되어 있고요.

그다음으로 about, blog, contact 라우팅을 위해 /src/routes 폴더 밑에 각각의 이름으로 폴더를 만들고 그 밑에 +page.svelte 파일을 아래와 같이 만들겠습니다.

```js
<!-- about/+page.svelte -->
<h1>Hi, I'm from mycodings.fly.dev</h1>

<p>This is my about page.</p>
<!-- blog/+page.svelte -->
<h1>Blog</h1>

<p>My blog posts will go here eventually…</p>
<!-- contact/+page.svelte -->
<h1>Get in touch</h1>

<p><a href="mailto:me@my.tld">Email me!</a></p>
```

위와 같이 코드를 작성했으면 아래와 같을 겁니다.

```js
📂 src
┗ 📂 routes
  ┣ 📜 +page.svelte
  ┣ 📂 blog
  ┃ ┗ 📜 +page.svelte
  ┣ 📂 about
  ┃ ┗ 📜 +page.svelte
  ┗ 📂 contact
    ┗ 📜 +page.svelte 
```

위와 같은 구조가 되어야 합니다.

이제 폴더 방식 라우팅이 재대로 작동하는지 한 번 볼까요?

![img](https://blogger.googleusercontent.com/img/a/AVvXsEixximypn1tOTPkwM_16Hq6lJbnLN8vVSUsNN63gbJoqmk0bsPebrvKH-8nQZuKUcuimwEqG9TPy9SsMqz_j_pTQcqbWEljEPeshAnb970VysC3GCLaiJD0_JUDnEaxSFdtGhkchN5uiyNo3g7RM5KTxGEjgjBVJTBQ0-AdSsvZyfhKvXaJeQNWbd7Z=s16000)

![img](https://blogger.googleusercontent.com/img/a/AVvXsEgzBSKLqNeDtwWYSMedK8My_iu1KyePNdlQMfgGIzdhvXPCy40r_TUy57Mj1BWvYKDLIibg93PmPKJtzSfnyw14x-P_ZsEAE6Ssy7IID7mN2Rt72QifcD8-o8t3xQp0YWREZtru21gBe1ky38MlHL9Xp2JgRKpvielsGpp0AaOAfDKC1P6ylA4weswi=s16000)

제대로 작동하네요.

<br>

<br>

#### 참고링크: [SvelteKit Tutorial 1 - 폴더 라우팅, 다이내믹 라우팅, 페이지 레이아웃, 스코프트 스타일 (mycodings.fly.dev)](https://mycodings.fly.dev/blog/2022-12-17-sveltekit-folder-routing-dynamic-routing-and-layout-page-scoped-style#폴더-방식-라우팅)

<br>