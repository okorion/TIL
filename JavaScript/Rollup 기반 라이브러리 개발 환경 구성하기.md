## 📑 Rollup 기반 라이브러리 개발 환경 구성하기

오늘은 오랜만에 튜토리얼 포스트를 작성해봅니다. 사실 최근에 React 컴포넌트를 라이브러리로 제작하는 프로젝트를 개인적으로 진행하고 있었는데, 모든 환경 설정을 바닥부터 만들어보는 경험을 했습니다. 굳이 바닥부터 만든 이유는 그냥 공부해보고 싶어서…이긴 한데, 유익하긴 했지만 굉장히 험난했던(?) 기억이 나네요.

본격적으로 튜토리얼 포스트를 시작하기 전에, **롤업(Rollup)** 번들러에 대해 잠깐 소개를 하고 넘어가도록 하겠습니다. 아마 웹팩(Webpack)은 다들 많이 들어보셨을텐데요, 롤업도 웹팩과 비슷한 역할을 하는 자바스크립트 번들러의 한 종류입니다. 그런데 *왜 웹팩을 놔두고 굳이 롤업을 쓰는 이유가 있는지* 궁금하신 분도 계실 것 같네요.

[![ES6](https://wormwlrm.github.io/static/5b2a49082cc57241f3b9aaa0dcfbf6b9/a6d36/0.png)](https://wormwlrm.github.io/static/5b2a49082cc57241f3b9aaa0dcfbf6b9/97806/0.png)*롤업은 기본적으로 ES6 빌드를 지원하는 번들러다*

구글에서 제작한 [번들러 비교 리포트](https://bundlers.tooling.report/output-module-formats/es-modules/)에 따르면, 롤업은 빌드 결과물을 ES6 모듈 형태로 만들 수 있습니다. ES6 모듈로 빌드가 가능하다는 것은 사용하는 쪽에서 라이브러리 전체를 불러오는 게 아니라 필요한 부분만 콕 집어서 가져올 수 있다는 특징이 있죠. 즉 실제로 사용하지 않는 코드를 빌드 단에서 제거하는 **트리 쉐이킹 기법**을 활용할 수 있기 때문에, 빌드 크기를 효율적으로 줄일 수 있습니다. 그래서 롤업은 주로 라이브러리를 제작하는 용도에 특화된 번들러입니다. 아, 물론 일반적인 프론트엔드 개발 서버 목적으로도 사용 가능하구요.

> 번들러에 대한 추가 설명이 필요하신 분들은 제가 예전에 작성해 둔 포스트인 [『JavaScript 번들러로 본 조선시대 붕당의 이해』](https://wormwlrm.github.io/2020/08/12/History-of-JavaScript-Modules-and-Bundlers.html)를 읽어보시면 도움이 되실 것 같습니다.

롤업에 대한 설명은 여기까지 하고 바로 시작해보도록 할게요. 이번 포스트를 통해 **롤업(Rollup)을 이용한 라이브러리 개발 환경 구성에 관심이 있는 개발자** 분들께 도움이 되기를 바랍니다.

## Rollup

우선 당연하게도 롤업을 설치해야겠죠?

```bash
# 전역 설치
yarn global add rollup

# 프로젝트 의존성으로 설치
yarn add -D rollup
```

저는 패키지 매니저로 주로 yarn을 쓰기 때문에 위와 같은 명령어로 설치했습니다. 두 명령어 중 아무거나 사용해도 상관 없긴 한데, 프로젝트 의존성으로 사용하면 아래와 같이 `package.json`의 NPM 스크립트에 명령을 추가해야 합니다. `package.json`이 없다면 `yarn init` 명령어를 입력해 새로 추가하면 됩니다.

저는 전역으로도 쓰고 싶고, 롤업 버전을 패키지 내에 명시하는 게 좋을 것 같아서 둘 다 썼습니다.

```json
// package.json

{
  // ...
  "scripts": {
    "build": "rollup -c",
    "watch": "rollup -cw"
  }
}
```

NPM 스크립트에는 두 가지 플래그가 나오는데, 저 두 명령어만 알아도 큰 문제는 없기 때문에 굳이 외울 필요는 없어보입니다. 개발할 때는 주로 `watch` 명령을 쓰고, 빌드할 때에는 `build` 명령을 쓴다는 정도로만 알아두도록 하죠.

> - `c`(config): 프로젝트 루트 디렉토리에 별도 설정 파일(`rollup.config.js`)을 사용하겠다는 뜻입니다.
> - `w`(watch): 변경 사항을 감지하여 자동 빌드를 수행합니다.

우리는 `rollup.config.js` 파일에서 롤업 설정을 관리할 것이기 때문에, 해당 이름을 가진 파일을 프로젝트 루트 디렉토리에 새로 만들어줍니다.

```js
// rollup.config.js

export default {
  input: "./src/index.js", // 진입 경로
  output: {
    file: "./dist/bundle.js", // 출력 경로
    format: "es", // 출력 형식
    sourcemap: true, // 소스 맵을 켜놔서 디버깅을 쉽게 만들자
  },
};
```

인풋(input)과 아웃풋(output)이라는 속성에서 볼 수 있듯이, 간단하게 `/src/index.js` 라는 파일을 읽어와서, `/dist/bundle.js` 라는 경로에 빌드 파일을 것이라는 것을 명시했습니다. 인풋 경로는 유일해야 하지만, 아웃풋은 배열로도 관리할 수 있기 때문에 같은 코드를 CommonJS, ES6, UMD 등 다양한 포맷으로 빌드하는 것도 가능하답니다.

그 후, `package.json`으로 다시 돌아가서 프로젝트 진입점도 함께 수정해줍시다. 이렇게 하면 현재 개발 중인 라이브러리를 외부에서 `import` 할 때, 자동적으로 `/dist/bundle.js` 를 제일 처음으로 호출하게 됩니다.

```json
// package.json

{
  // ...
  "main": "./dist/bundle.js"
}
```

### 번들 맛보기

우선 빌드가 어떤 식으로 되는지 한 번 찍먹해보려고 합니다. 환경 설정의 인풋에 명시한대로, 해당 경로에 테스트용 JavaScript 파일을 하나 만들어줍니다. 저는 `"hello"`라는 문자열을 출력하는 변수를 하나 만들고 `export` 했습니다.

```js
// src/index.js

export const log = () => {
  console.log("hello");
};
```

그 후 `yarn build` 명령어를 수행해봅시다.

```bash
# NPM 스크립트
yarn build

# 그냥 롤업에서 바로
rollup -c
```

아까 설정한 NPM 스크립트 내용에 따라 롤업 빌드가 실행되게 됩니다.

[![dist](https://wormwlrm.github.io/static/e9348396a5ef2d093b29573736a9bc91/374ac/1.png)](https://wormwlrm.github.io/static/e9348396a5ef2d093b29573736a9bc91/374ac/1.png)*dist 디렉토리 내에 빌드 결과물이 생겼다*

실제 빌드 결과물을 아래에서 보도록 합시다.

```js
// dist/bundle.js

const log = () => {
  console.log("hello");
};

export { log };
//# sourceMappingURL=bundle.js.map
```

환경 설정에서 아웃풋 포맷을 ES 모듈로 설정했기 때문에 ES 방식으로 빌드가 된 것을 확인할 수 있습니다. 그리고 개발용 소스 맵(sourcemap)도 활성화를 해 놓아서, 이 역시 빌드 결과물에 추가가 된 것을 확인할 수 있습니다.

빌드가 잘 동작하는 것을 확인했으니, 지금부터는 빌드 명령어를 매번 입력하지 않게 `watch` 명령어로 빌드를 합시다.

```bash
# NPM 스크립트
yarn watch

# 그냥 롤업에서 바로
rollup -cw
```

### CJS로 빌드하면 어떻게 되나요?

아, 참고로 빌드 포맷을 `"cjs"`, 즉 CommonJS 방식으로 선택하면 아래와 같이 결과물이 나옵니다.

```js
// dist/bundle.js

"use strict";

Object.defineProperty(exports, "__esModule", { value: true });

var log = function log() {
  console.log("hello");
};

exports.log = log;
//# sourceMappingURL=bundle.js.map
```

## React

다음으로는 리액트를 설치해야겠죠? 그런데 주의할 점이 있습니다. **리액트를 현재 프로젝트에 직접 설치하면 안됩니다**. 이게 무슨 뚱딴지같은 소리인가 싶겠지만, 그 이유는 바로 *내가 만드는 라이브러리를 사용하는 쪽(호스트)의 리액트와 충돌이 일어날 수 있기 때문* 입니다.

따라서 리액트를 현재 라이브러리에 직접 설치하지 않고, 호스트에서 설치한 리액트를 사용하겠다고 명시해야 합니다. 이를 가리켜 피어 디펜던시(Peer Dependency)이라고 합니다. 참고로 yarn에서는 `P` 플래그를 이용해 패키지를 피어 디펜던시로 설치가 가능합니다.

```bash
# 피어 디펜던시로 설치
yarn add -P react react-dom
```

위 명령어를 수행하면 다음과 같이 `package.json`에 피어 디펜던시가 추가됩니다.

```json
// package.json
{
  // ...
  "peerDependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  }
}
```

그 후 `src` 내 파일을 다음과 같이 수정해보겠습니다. 간단한 컴포넌트를 하나 만들었습니다.

```js
// src/index.js

export * from "./Hello";
// src/Hello.jsx

import React from "react";
import ReactDOM from "react-dom";

export const Hello = () => {
  return <div>Hello World!</div>;
};
```

과연 결과물이 잘 나올까요?

[![babel](https://wormwlrm.github.io/static/8475cf4912d15ef47a7269f1edd29ea3/a6d36/2.png)](https://wormwlrm.github.io/static/8475cf4912d15ef47a7269f1edd29ea3/c929c/2.png)*아직 뭔가 부족해보인다*

그러나 단순히 이렇게만 하면 빌드가 되지 않습니다. 왜냐하면 우리는 단순히 리액트만 설치한 것이지, `.jsx` 파일을 해석할 수 있는 바벨을 아직 설치하지 않았기 때문입니다. 따라서 바벨 관련 패키지를 설치합니다.

```bash
# 바벨 설치
yarn add -D @babel/core @babel/preset-env @babel/preset-react

# 롤업에서 바벨을 사용하게 해주는 플러그인도 설치
yarn add -D @rollup/plugin-babel
```

그 후, `rollup.config.js`에 바벨 관련 설정을 추가해줍니다.

```js
// rollup.config.js

import babel from "@rollup/plugin-babel";

export default {
  input: "./src/index.js",
  output: {
    file: "./dist/bundle.js",
    format: "es",
    sourcemap: true,
  },
  plugins: [
    // 바벨 트랜스파일러 설정
    babel({
      babelHelpers: "bundled",
      presets: ["@babel/preset-env", "@babel/preset-react"],
    }),
  ],
};
```

그 후, 다시 빌드를 수행해보면 터미널에서 다음과 같은 결과물이 나옵니다.

[![빌드](https://wormwlrm.github.io/static/a09bcb18f07f3749792612d9949bf284/a6d36/3.png)](https://wormwlrm.github.io/static/a09bcb18f07f3749792612d9949bf284/e4ee8/3.png)*결과물이 잘 생성되었다고 한다*

아래 코드와 같이, 실제 빌드 결과물도 JSX 문법에서 JavaScript 코드로 잘 변환이 되었네요.

```js
// dist/bundle.js

import React from "react";
import "react-dom";

var Hello = function Hello() {
  return /*#__PURE__*/ React.createElement("div", null, "Hello World!");
};

export { Hello };
//# sourceMappingURL=bundle.js.map
```

## 완성되지 않은 라이브러리를 테스트할 수 있게 만들기

그렇다면 이 결과물을 사용하는 쪽에서 직접 써보고 싶다면 어떻게 해야할까요? 즉, 우리가 개발하고자 하는 라이브러리의 이름을 `'my-library'`라고 했을 때, 어떤 외부 프로젝트(호스트 프로젝트)에서 아래와 같이 불러오고 싶다는 얘기죠.

```jsx
// Q. 호스트 프로젝트에서 개발 도중인 라이브러리를 아래와 같이 불러와 쓸 수 있을까?

import { Hello } from "my-library";

export const Parents = () => {
  return (
    <div>
      <Hello />
    </div>
  );
};
```

그런데 문제가 있습니다. 프로젝트에서 라이브러리를 불러오려면 해당 라이브러리가 프로젝트 의존성으로 설치되어 있어야 합니다.

[![ES6](https://wormwlrm.github.io/static/6ca8e2c010bd51ad6f5110203755b7ec/a6d36/4.png)](https://wormwlrm.github.io/static/6ca8e2c010bd51ad6f5110203755b7ec/5ba90/4.png)*없는 걸 불러오면 이렇게 된다. 없는 걸 어떻게 불러와요!*

일단 여기에 대한 세 가지 접근법이 있는데요, 하나씩 알아보도록 합시다.

첫 번째 방법은 **NPM에 그냥 배포하기**(?)입니다. 그냥 개발 도중인 라이브러리를 바로 NPM에 배포해버리는 것이죠. 하지만 개발 도중인 라이브러리를 매 수정 사항이 생길 때마다 NPM에 배포해서 확인하는 것은 사실 말도 안되는 이야기죠. 그렇기 때문에 실용적인 해법은 아닙니다.

두 번째 방법은 **파일 경로 기반 라이브러리 설치**입니다. 즉, 호스트 프로젝트에서 라이브러리 프로젝트의 의존성을 파일 기반으로 가리키게 하는 것입니다. 이렇게 하면 해당 파일의 `package.json`에 명시된 `main` 경로를 호출하게 되죠.

이를 직접 확인하기 위해, CRA를 이용해 리액트 프로젝트를 하나 새롭게 만들고 아래처럼 이렇게 직접 `package.json`을 수정해보았습니다.

```json
// 호스트 프로젝트의 package.json
{
  // ...
  "dependencies": {
    "my-library": "file:../my-library"
  }
}
```

이 상태에서 호스트 프로젝트에서 `yarn install` 처럼 패키지 설치 명령어를 수행하면 어떻게 될까요?

[![ES6](https://wormwlrm.github.io/static/36f7a35302fb809b108a58acecccdecc/a6d36/6.png)](https://wormwlrm.github.io/static/36f7a35302fb809b108a58acecccdecc/94ec4/6.png)*파일 경로로 등록한 프로젝트도 설치가 가능하다*

놀랍게도(?) 잘 동작하는 것을 확인할 수 있습니다. 그런데 라이브러리 프로젝트에 수정 사항이 생겨서 `dist/bundle.js` 가 새로 생겨도 이게 즉시 반영될까요?

이를 확인해보기 위해 아까 만들었던 `Hello` 컴포넌트에 id 값을 새로 추가해봤습니다.

```jsx
import React from "react";
import ReactDOM from "react-dom";

export const Hello = () => {
  return <div id="component">Hello World!</div>;
};
```

그 후 저장을 누르게 되면 호스트 프로젝트에서 불러온 컴포넌트에도 id 변경이 적용되어야 할텐데…

[![ES6](https://wormwlrm.github.io/static/c9d183286d0cd73cc97858c45bc8452d/a6d36/7.png)](https://wormwlrm.github.io/static/c9d183286d0cd73cc97858c45bc8452d/be061/7.png)*오른쪽(라이브러리)에서의 변경이… 왼쪽(호스트)에 적용되지 않는다.*

아… 아쉽게도 변경이 되지 않습니다. 왜냐하면 호스트 프로젝트에서 설치한 라이브러리는 `yarn install` 을 실행할 당시의 사본을 가져오기 때문입니다. 그렇기 때문에 두 프로젝트는 그냥 물리적으로 복붙을 한 것이나 다름없고, 한 쪽에서의 변경 사항이 다른 쪽에 적용되지 않습니다.

이렇게 물리적으로 따로 떨어진 프로젝트를 동기화시킬 수 있는 방법이 없을까요? 있습니다! 바로 세 번째 방법인 **NPM link** 라는 명령을 쓰면 됩니다.

![img](https://miro.medium.com/max/4800/0*x8jMbWUMifff9Eao)*사진 출처는 [이 곳](https://medium.com/dailyjs/how-to-use-npm-link-7375b6219557).*

NPM 링크는 물리적으로 떨어진 프로젝트의 바로가기 같은 기능을 제공합니다. 이를 정확히는 심링크(symlink)라고 부르는데, 즉 원본 프로젝트에서 심링크를 만들면 이를 참조하는 프로젝트에서는 원본의 수정 사항을 바로 동기화할 수 있다는 기능을 제공합니다.

따라서 우리는 이 기능을 이용해 두 프로젝트 간의 동기화 문제를 해결하려고 합니다. 우선 라이브러리 프로젝트에서 아래 명령어를 입력합니다. 참고로 링크 명령어 역시 yarn에서 지원합니다.

```bash
yarn link
```

그러면 해당 리포지터리 이름이 적힌 링크가 생성이 되는데, 이를 호스트 프로젝트에서 입력하여 연결해주면 됩니다.

```bash
# 라이브러리 프로젝트 이름이 my-library 였을 경우
yarn link my-library
```

두 프로젝트 의존성이 연결된 상태라는 것은 호스트 프로젝트의 `node_modules` 디렉토리를 살펴보면 바로 알 수 있습니다.

[![ES6](https://wormwlrm.github.io/static/df0ffb5b0cb661c2fc104a2a61add9be/a6d36/5.png)](https://wormwlrm.github.io/static/df0ffb5b0cb661c2fc104a2a61add9be/f69df/5.png)*심볼릭 링크를 나타내는 화살표가 보인다*

그렇다면 과연 코드가 실제로 바뀌는지 확인해봅시다.

![ES6](https://wormwlrm.github.io/bb6fdce0e20a7005441bcae96ffbbd03/10.gif)*좌측(라이브러리)에서 수정한 코드가 우측(호스트)에도 바로 반영이 된다*

실제로 반영이 잘 되는 것을 확인할 수 있습니다. 이렇게 물리적으로 완전히 떨어진 두 프로젝트를 연결하고, 그 중 하나를 의존성으로 관리할 수 있게 되었습니다.

## TypeScript

사실 여기까지 했으면 타입스크립트를 적용하는 것은 그리 어렵지 않습니다. 롤업에서 공식 타입스크립트 플러그인을 지원하고 있기 때문입니다. 그리고 지금까지 사용한 라이브러리에 대한 타이핑 패키지도 추가를 해줘야 합니다.

```bash
# 롤업 타입스크립트 플러그인 설치
yarn add -D @rollup/plugin-typescript

# 롤업 타입스크립트 플러그인의 피어 디펜던시 설치
yarn add -D typescript tslib

# 바벨에서도 이를 해석하게 추가
yarn add -D @babel/preset-typescript

# 리액트, 리액트 DOM 타입 패키지 추가
yarn add -D @types/react @types/react-dom
```

그 후 `.js`, `.jsx` 확장자 파일을 `.ts`, `.tsx` 로 변경하고, `rollup.config.js` 파일에 플러그인을 추가합니다. 바벨에도 확장자 추가가 있으니 주의해주세요.

```js
// rollup.config.js

import babel from "@rollup/plugin-babel";
import typescript from "@rollup/plugin-typescript";

export default {
  input: "./src/index.ts",
  output: {
    file: "./dist/bundle.js",
    format: "es",
    sourcemap: true,
  },
  plugins: [
    // 바벨 트랜스파일러 설정
    babel({
      babelHelpers: "bundled",
      presets: [
        "@babel/preset-env",
        "@babel/preset-react",
        "@babel/preset-typescript",
      ],
      extensions: [".js", ".jsx", ".ts", ".tsx"],
    }),

    // 타입스크립트
    typescript(),
  ],
};
```

`tsconfig.json`은 프로젝트 루트 디렉토리에 만들되, 취향껏 만드시면 됩니다. 저는 일단 기본적으로 제공해주는 옵션 중에서 최소한의 설정만 적어봤습니다.

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "esnext"],
    "jsx": "react",
    "module": "es6",
    "moduleResolution": "node",
    "baseUrl": "./",
    "strict": true,
    "esModuleInterop": true
  }
}
```

결과가 잘 나오는지 확인해볼까요?

![ES6](https://wormwlrm.github.io/fe6e2c11c5b1bf4e6b12d2b9f33d6a4b/11.gif)*TypeScript 코드를 수정하면 JavaScript 코드로 빌드되고, 이를 호스트 프로젝트에서 심볼릭 링크로 참조한다.*

다행히 잘 나오네요. 가장 좌측에서부터 우측 순서대로 변경이 전파되는 것을 확인하시면 됩니다.

> 1. 라이브러리의 TypeScript 코드 수정
> 2. 롤업에서 이를 JavaScript로 빌드
> 3. 심볼릭 링크를 통해 호스트 프로젝트에도 변경사항 전파

이제 마지막으로, 심볼릭 링크를 이용한 개발 환경이 잘 구성되었는지를 살펴봅시다.

![ES6](https://wormwlrm.github.io/68e60ec77cd2bdb183a13a91f77df039/12.gif)*라이브러리의 코드를 수정하면호스트의 코드 수정 없이, 호스트 프로젝트 결과물에 반영된다.*

반시계 방향으로 시야를 이동하면서 이를 확인해보세요. 호스트 코드에는 별도 수정 없이, 라이브러리 단계에서의 수정이 바로 호스트 결과물에 반영되는 것을 확인할 수 있습니다.

## 살펴 볼만한 라이브러리

![img](https://media.giphy.com/media/rYEAkYihZsyWs/giphy.gif)*개발 특) 튜토리얼 보고 따라해도 한 번에 안 됨*

이렇게 해서 간단한(?) 리액트 컴포넌트 개발 환경 구성을 알아봤습니다. 본문에 나오는 구성은 정말 최소한의 라이브러리, 기능만 써서 작업 환경을 구성했기 때문에, 지금보다 많은 기능들을 포함하게 되면 추가 플러그인 설치가 필요할 것입니다.

그래도 웬만한 기능들을 롤업에서 공식적으로 지원해주기 때문에, 인내심을 갖고 천천히 찾아보시면 방법이 있을 것입니다. 그래서 본문에서 소개하지 않은 쓸만한 플러그인을 몇 개 소개하면서 글을 마무리하고자 합니다.

> - 공식 라이브러리
>   - @rollup/rollup-plugin-node-resolve
>     - `node_modules` 내 서드파티 모듈 사용 용도
>   - @rollup/rollup-plugin-commonjs
>     - CJS 디펜던시를 ES 방식으로 변환해주어 빌드 결과물에 포함 가능하게 만들어 줌
>   - @rollup/rollup-plugin-json
>     - JSON 파일을 빌드 결과물에 포함 가능하게 만들어 줌
>   - @rollup/rollup-plugin-url
>     - 파일을 빌드 결과물에 포함 가능하게 만들어 줌
>   - @rollup/rollup-plugin-replace
>     - 스트링 변환해줌, 환경변수 등 사용 목적

------

> - 비공식
>   - rollup-livereload
>     - 변경 사항 생기면 자동 새로고침
>   - rollup-plugin-typescript2
>     - 비공식 타입스크립트 라이브러리
>   - rollup-plugin-postcss
>     - postcss 도구 지원



<br>

<br>

#### 참고링크: [Rollup 기반 라이브러리 개발 환경 구성하기 - 재그지그의 개발 블로그 (wormwlrm.github.io)](https://wormwlrm.github.io/2021/11/07/Rollup-React-TypeScript.html)

<br>