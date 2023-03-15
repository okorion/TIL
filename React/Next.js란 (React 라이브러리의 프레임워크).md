### Next.js란? (React 라이브러리의 프레임워크)

=> 기본적인 React CSR(Client Side Rendering)에서 SSR(Server Side Rendering) 구현을 도와준다!

=> CSR과 SSR은 무엇이고, SSR으로 구현하는 이유는?

=> SEO(Search Engine Optimization)을 위해서!



✅ Vue에서는 SSR을 지원하는 프레임워크 **Nuxt.js!**



### 🧊 추가 기능

#### 1. 직관적인 페이지 기반 라우팅 시스팀

next.js는 pre-rendering 뿐만 아니라 `페이지 기반 라우팅 시스템`도 제공한다. 프로젝트의 가장 바깥 폴더인 `/pages` 폴더에서 컴포넌트를 export하면 폴더명이 페이지 route가 된다. (`/pages/indext.s` -> `/`, `/pages/store/t-shirt` -> `/store/t-shirt`)

또, `/look/[id]`와 같은 dynamic route도 지원하는데, 다음 장에서 다루도록 하겠다.



#### 2. 페이지간 빠르고 매끄러운 전환을 위한 client-side navigation

next는 `< Link />` 컴포넌트를 통해 페이지간의 빠르고 매끄러운 이동을 가능하게 한다. HTML의 a 태그와 달리 페이지를 리로딩하지 않고도 페이지간 이동이 가능하고, `link 컴포넌트가 뷰포트에 보였을 때 관련 페이지를 백그라운드에서 미리 가져다 놓기 때문에` 사용자가 링크를 클릭했을 때 매우 빠르게 해당 페이지로 이동할 수 있게 해준다. (이것도 제대로 알고나니 와..하고 감탄했다. 이제 link만 써야지)



출처: [[Next.js\] 기본 개념 : Next.js 란? Next.js를 왜 사용할까? Next.js의 장점은? (velog.io)](https://velog.io/@syoung125/Next.js-기본-개념-1-Next.js-란-Next.js를-왜-사용할까-Next.js의-장점은)
