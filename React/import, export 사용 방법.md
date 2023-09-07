## 🛰️ import, export 사용 방법

![[React]import, export 사용 방법](https://blog.kakaocdn.net/dn/kx8HN/btrbtovnQSk/a22IOmS2vmaFn5dZ67niL0/img.png)



**React**에서 애플리케이션의 크기가 커질수록 하나의 파일에서 코드를 작성하기에는 한계가 존재합니다. 이러한 문제를 해결하기 위해 자바스크립트에서는 **모듈(module)**이라는 기능을 지원하여 하나의 파일을 여러개의 파일로 나눌 수 있습니다.



![[React]import, export 사용 방법](https://blog.kakaocdn.net/dn/OBK2y/btrbtniXpWg/RyPX1ShSTO4qW9HfMggmA1/img.png)React 파일 구조 예시



위 사진은 App.js에서 Page와 관련된 로직을 컴포넌트로 분리하였으며, Page 폴더에서 관리하는 구조입니다. 

App.js가 Page 폴더 내부에 있는 파일들의 코드를 접근하는 방법은 두 가지 입니다.

 

**방법 1. 파일경로를 직접 접근하여 import**

```
import DefaultPage from "./Page/DefaultPage";
import Page001 from "./Page/Page001";
import Page002 from "./Page/Page002";
import Page003 from "./Page/Page003";
import Page404 from "./Page/Page404";
```

 

**방법 2. 폴더 내부에 index.js 파일을 생성**

```
import { DefaultPage, Page001, Page002, Page003, Page404 } from "./Page";
```

 

파일 경로를 직접 접근하여 import하는 방법에는 몇 가지 문제점이 존재합니다. 대표적으로 프로젝트의 규모가 커지고 여러개의 파일을 import하는 경우에는 파일 개수만큼 import하므로 비효율적인 코드를 생성하고 코드를 작성하는데, 불필요한 시간을 소모합니다.

------

### **export와 import**

> **export**
> 변수, 함수, 클래스 앞에 export 키워드를 붙여서 모듈의 기능을 외부에서 사용할 수 있도록 내보냅니다.
>
> **import**
> export로 내보낸 모듈을 가져오는 기능을 담당합니다.

 

**import 키워드 사용 방법**



![[React]import, export 사용 방법 - undefined - export와 import](https://blog.kakaocdn.net/dn/cJ0ww4/btrbotxT4MK/NKb7k2mmax8G7WxbNY7qk1/img.png)



**import** 키워드 다음에 식별자(사용할 변수, 함수, 클래스)를 작성합니다.

**from** 키워드 다음에 불러올 모듈의 경로를 작성합니다.

 

**사용 방법 1.**

변수, 함수, 클래스를 작성 후 **export** 키워드를 작성하는 방법입니다.

Page001이라는 함수형 컴포넌트를 작성 후 마지막 줄에서 **export** 키워드를 작성하여 내보냅니다.

 

**Page001.js**

```
const Page001 = () => {
  return (
    <div>
      <h1>Page001 컴포넌트</h1>
    </div>
  );
};

// export Page001로 작성할 경우 에러가 발생합니다.
export { Page001 };
```

**App.js**

import를 작성한 line에서 중괄호 {} 를 제거할 경우 에러가 발생합니다.

```
import { Page001 } from "./Page001";

export default function App() {
  return (
    <React.Fragment>
      <Page001 />
    </React.Fragment>
  );
}
```

 

**사용 방법 2.**

변수, 함수, 클래스 작성과 함께 **export** 키워드를 붙이는 방법입니다.

맨 앞에 **export** 키워드를 붙입니다.

 

**Page002.js**

```
export const Page002 = () => {
  return (
    <div>
      <h1>Page002 컴포넌트</h1>
    </div>
  );
};
```

**App.js**

```
import { Page002 } from "./Page002";

export default function App() {
  return (
    <React.Fragment>
      <Page002 />
    </React.Fragment>
  );
}
```

 

**사용 방법 3.**

**as** 키워드를 사용하여 별칭을 붙여서 내보냅니다.

 

**Page404.js**

```
const Page404 = () => {
  return (
    <div>
      <h1>페이지가 존재하지 않습니다.</h1>
    </div>
  );
};

export { Page404 as ErrorPage };
```

**App.js**

Page404.js의 경로는 변경되지 않았으므로 식별자와 경로의 혼동을 주의하여 작성합니다..

```
import React from "react";
import { ErrorPage } from "./Page404";

export default function App() {
  return (
    <React.Fragment>
      <ErrorPage />
    </React.Fragment>
  );
}
```

 

**사용 방법 4.**

**default** 키워드를 붙여서 내보내는 방법입니다.

 

**Page003.js**

일반 함수로 작성할 경우에는 함수 작성과 함께 **export default** 키워드를 사용 할 수 있습니다.

```
export default function Page003() {
  return (
    <div>
      <h1>Page003 컴포넌트</h1>
    </div>
  );
}
```

**Page004.js**

화살표 함수로 작성할 경우에는 마지막 줄에 **export default** 키워드를 사용하여 내보냅니다.

```
const Page004 = () => {
  return (
    <div>
      <h1>Page004 컴포넌트</h1>
    </div>
  );
};

// default 키워드를 사용하는 경우 중괄호 {} 없이 export 가능합니다.
export default Page004;
```

**App.js**

**default** 키워드가 추가된 변수, 함수, 클래스는 **중괄호 {}** 없이 식별할 수 있습니다.

```
import React from "react";
import Page003 from "./Page003";
import Page004 from "./Page004";

export default function App() {
  return (
    <React.Fragment>
      <Page003 />
      <Page004 />
    </React.Fragment>
  );
}
```

------

### **한 파일에 여러 개의 변수, 함수, 클래스를 export하는 경우**

> **※ 주의사항**
> export default 키워드가 있는 모듈은 중괄호를 사용하여 import할 경우 에러가 발생합니다.
> 한 파일에서 export default 키워드는 오직 한 개만 존재해야합니다.

**MultiPage.js**

Page005 함수에는 **default** 키워드를 추가하였습니다.

```
export default function Page005() {
  return (
    <div>
      <h1>Page005 컴포넌트</h1>
    </div>
  );
}

export function Page006() {
  return (
    <div>
      <h1>Page006 컴포넌트</h1>
    </div>
  );
}

export function Page007() {
  return (
    <div>
      <h1>Page007 컴포넌트</h1>
    </div>
  );
}
```

위 코드는 아래 코드와 같이 **export**를 맨 마지막 줄에 작성하여 사용할 수 있습니다.

불필요하게 변수, 함수, 클래스 앞에 **export**를 추가하지 않고 맨 마지막 줄에서 한 번에 처리 가능합니다.

```
function Page005() {
  return (
    <div>
      <h1>Page005 컴포넌트</h1>
    </div>
  );
}

function Page006() {
  return (
    <div>
      <h1>Page006 컴포넌트</h1>
    </div>
  );
}

function Page007() {
  return (
    <div>
      <h1>Page007 컴포넌트</h1>
    </div>
  );
}

export { Page005 as default, Page006, Page007 };
```

 

**App.js**

**default** 키워드가 붙은 Page005는 **중괄호 {}** 없이 모듈을 가져옵니다.

**default** 키워드가 없는 Page006과 Page007은 **중괄호 {}** 를 사용하여 모듈을 가져옵니다.

```
import React from "react";
import Page005, { Page006, Page007 } from "./MultiPage";

export default function App() {
  return (
    <React.Fragment>
      <Page005 />
      <Page006 />
      <Page007 />
      <ErrorPage />
    </React.Fragment>
  );
}
```

 

지금까지 작성한 파일과 코드를 확인할 수 있습니다.



------

### **폴더 내부의 파일을 import하는 방법**

Page 폴더 내부에 **index.js** 파일을 생성합니다.

index.js 파일에서 Page폴더 내부에 있는 모듈을 관리할 수 있습니다.



![[React]import, export 사용 방법 - undefined - 폴더 내부의 파일을 import하는 방법](https://blog.kakaocdn.net/dn/scYJm/btrbllm1u15/KgecHLN0MIjkbt7VT0yYYk/img.png)



 

**index.js**

index.js 파일은 Page 폴더 내부에 작성된 모듈을 불러와서 내보냅니다.

즉, Page 폴더 내부에서 export하고자 하는 모듈은 index.js 파일에서 관리가 됩니다.

```
import DefaultPage from "./DefaultPage";
import { Page001 } from "./Page001";
import Page002 from "./Page002";
import Page003 from "./Page003";
import { ErrorPage } from "./Page404";

export { DefaultPage, Page001, Page002, Page003, ErrorPage };
```

**App.js**

index.js가 없었다면, 여러번 import 해야 하는 코드가 단 한줄로 처리되었습니다.

```
import { DefaultPage, Page001, Page002, Page003, ErrorPage } from "./Page";

export default function App() {
  return (
    <div>
      <DefaultPage />
      <Page001 />
      <Page002 />
      <Page003 />
      <ErrorPage />
    </div>
  );
}
```

 

 <br>

 <br>

#### 참고링크: [[React\]import, export 사용 방법 (tistory.com)](https://developer-talk.tistory.com/139)

 <br>