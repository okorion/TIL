## 🧇 forwardRef란?

## 🧈 forwardRef

React에서 특수한 목적으로 사용되기 때문에 일반적인 용도로 사용할 수 없는 prop이 몇 가지 있습니다. 대표적인 예로 루프를 돌면서 동일한 컴포넌트 여러 번 랜더링할 때 사용하는 `key` prop을 들 수 있는데요. `ref` prop도 마찬가지로 HTML 엘리먼트 접근이라는 특수한 용도로 사용되기 때문에 일반적인 prop으로 사용을 할 수 없습니다.

HTML 엘리먼트가 아닌 React 컴포넌트에서 `ref` prop을 사용하려면 React에서 제공하는 `forwardRef()`라는 함수를 사용해야 합니다. React 컴포넌트를 `forwardRef()`라는 함수로 감싸주면, 해당 컴포넌트는 함수는 두 번째 매개 변수를 갖게 되는데, 이를 통해 외부에서 `ref` prop을 넘길 수 있습니다.

예를 들어, 위에서 작성한 `<Input/>` 컴포넌트에 `forwardRef()`라는 함수를 적용해보겠습니다.

```jsx
import React, { forwardRef, useRef } from "react";

const Input = forwardRef((props, ref) => {
  return <input type="text" ref={ref} />;
});

function Field() {
  const inputRef = useRef(null);

  function handleFocus() {
    inputRef.current.focus();
  }

  return (
    <>
      <Input ref={inputRef} />
      <button onClick={handleFocus}>입력란 포커스</button>
    </>
  );
}
```

이제 버튼을 클릭해보면 기존과 같이 입력란으로 포커스가 이동하는 것을 볼 수 있을 것입니다! 😄

<br>

## 예제: audio 엘리먼트 제어

좀 더 실제 프로젝트에서 사용할 법한 예로 audio 엘리먼트 제어하는 컴포넌트를 작성해보겠습니다.

먼저 `<Audio/>` 자식 컴포넌트와 `<Controls/>` 자식 컴포넌트로 이루어진 `<Player/>` 부모 컴포넌트를 작성하겠습니다.

```jsx
// Player.jsx
import React, { useRef } from "react";
import Audio from "./Audio";
import Controls from "./Controls";

function Player() {
  const audioRef = useRef(null);

  return (
    <>
      <Audio ref={audioRef} />
      <Controls audio={audioRef} />
    </>
  );
}

export default Player;
```

`useRef()` 훅(hook) 함수로 `audioRef` 객체를 생성한 후, `<Audio/>` 컴포넌트에는 `ref` prop으로, `<Controls/>` 컴포넌트에는 `audio` prop으로 넘겨주고 있습니다.

`<Player/>` 컴포넌트에서 넘기는 `ref` prop을 제대로 받으려면 `<Audio/>` 컴포넌트는 `forwardRef()` 함수를 사용해야 합니다. 그러면 두 번째 매개 변수를 통해 `ref` 객체가 넘어오게 되고, 내부에 있는 `<audio>` 엘리먼트로 다시 넘겨(forward)줄 수 있습니다. 이를 통해 부모 컴포넌트인 `<Player/>`에서 자식 컴포넌트인 `<Audio/>`의 내부에 있는 `<audio>` 엘리먼트에 직접 접근할 수 있게 되었습니다.

```jsx
// Audio.jsx
import React, { forwardRef } from "react";
import music from "./music.mp3";

function Audio(prop, ref) {
  return (
    <figure>
      <figcaption>Eyes on You (Sting) - Network 415:</figcaption>
      <audio src={music} ref={ref}>
        Your browser does not support the
        <code>audio</code> element.
      </audio>
    </figure>
  );
}

export default forwardRef(Audio);
```

`<Controls/>` 컴포넌트에는 `ref`가 아닌 `audio`라는 일반적인 prop으로 `audioRef` 객체가 넘기기 때문에 굳이 `forwardRef()` 함수를 사용할 필요가 없습니다. `<Controls/>` 컴포넌트 내의 이벤트 핸들러 함수는 `<Player/>` 컴포넌트로 부터 넘어온 `audioRef` 객체를 통해서 `<audio>` 엘리먼트의 `play()`와 `pause()` 함수를 호출할 수 있습니다.

```jsx
// Controls.jsx
import React from "react";

function Controls({ audio }) {
  const handlePlay = () => {
    audio.current.play();
  };

  const handlePause = () => {
    audio.current.pause();
  };

  return (
    <>
      <button onClick={handlePlay}>재생</button>
      <button onClick={handlePause}>중지</button>
    </>
  );
}

export default Controls;
```

<br>

## 보너스: 디버깅 팁

`forwardRef()` 함수를 호출할 때 다음과 같이 익명 함수를 넘기면 브라우저에서 React 개발자 도구를 사용할 때 컴포넌트의 이름이 나오지 않아서 불편할 수가 있는데요.

```jsx
const Input = forwardRef((props, ref) => {
  return <input type="text" ref={ref} />;
});
```

React 개발자 도구에서 `forwardRef()` 함수를 사용해도 컴포넌트 이름이 나오게 하는 몇가지 방법을 알려드리겠습니다.

첫 번째 방법은 `forwardRef()` 함수에 익명 함수를 대신에 이름이 있는 함수를 넘깁니다.

```jsx
const Input = forwardRef(function Input(props, ref) {
  return <input type="text" ref={ref} />;
});
```

두 번째 방법은 `forwardRef()` 함수의 호출 결과로 기존 컴포넌트를 대체합니다.

```jsx
function Input(props, ref) {
  return <input type="text" ref={ref} />;
}

Input = forwardRef(Input);
```

마지막 방법은 `forwardRef()` 함수의 호출 결과의 `displayName` 속성에 컴포넌트 이름을 설정해줍니다.

```jsx
const Input = forwardRef((props, ref) => {
  return <input type="text" ref={ref} />;
});

Input.displayName = "Input";
```

위 세가지 방법 중에 본인의 취향에 맞는 방법을 사용하시면 되겠습니다. (저는 개인적으로 두 번째 방법을 선호합니다.)

<br>

## 전체 코드

본 포스팅에서 작성한 코드는 아래에서 직접 확인하고 실행해볼 수 있습니다.

<iframe src="https://codesandbox.io/embed/react-forward-ref-nqxh4?fontsize=14&amp;hidenavigation=1&amp;theme=dark" title="react-forward-ref" allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-variant-alternates: inherit; font-weight: 400; font-stretch: inherit; font-size: medium; line-height: inherit; font-family: &quot;Spoqa Han Sans Neo&quot;, -apple-system, BlinkMacSystemFont, &quot;avenir next&quot;, avenir, &quot;segoe ui&quot;, &quot;helvetica neue&quot;, helvetica, Ubuntu, roboto, noto, arial, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; vertical-align: baseline; color: rgb(0, 33, 77); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; width: 700px; height: 500px; border-radius: 4px; overflow: hidden;"></iframe>

<br>

## 마치면서

이상으로 React의 `forwardRef()` 함수를 사용하여 어떻게 React 컴포넌트에 `ref` prop을 넘길 수 있는지에 대해서 알아보았습니다.

일반적으로 `forwardRef()` 함수는 HTML 엘리먼트 대신에 사용되는 최말단 컴포넌트(ex. `<Input/>`, `<Button/>`)를 대상으로 주로 사용되며, 그 보다 상위 컴포넌트에서는 `forwardRef()` 함수를 사용하는 것이 권장되지 않습니다. 왜냐하면 어떤 컴포넌트의 내부에 있는 HTML 엘리먼트의 레퍼런스를 외부에 있는 다른 컴포넌트에서 접근하도록 하는 것은 컴포넌트 간의 결합도(coupling)을 증가시켜 애플리케이션의 유지보수를 어렵게 만들기 때문입니다.

<br>

<br>

#### 참고링크: [[React\] forwardRef 사용법 | Engineering Blog by Dale Seo](https://www.daleseo.com/react-forward-ref/)

<br>