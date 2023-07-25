## 🍭 Pull Request 사전 체크리스트 7가지

> 원문: https://evilmartians.com/chronicles/before-your-next-frontend-pull-request-use-this-checklist

### 프런트엔드 풀 리퀘스트에는 심각한 버그, 신경질적인 반응, 시간 낭비를 초래할 수 있는 일반적인 실수가 포함되는 경우가 많습니다. 하지만 이 7가지 사소하지만 중요한 규칙 목록을 따르면 이러한 실수를 쉽게 피할 수 있습니다. 아래 내용을 읽고 새 PR을 만들기 전에 확인해야 할 사항을 알아보세요.

편지나 이메일을 보내기 전에 항상 한 번 더 확인하는 것이 중요하지 않나요? 깃허브 또는 깃랩에서 "request review" 버튼을 누르기 전에도 같은 개념이 적용됩니다. 하지만 정확히 무엇을 확인해야 할까요?

아래 목록에 몇 가지 기본 규칙을 요약해서 안내해드리겠습니다.

작업 환경에 따라 최종 목록이 다를 수 있으므로 필요에 따라 자유롭게 수정, 삭제 또는 추가할 수 있다는 점에 유의하세요!

<br>

<br>

## 1. 번들 크기 최소화하기

프로젝트 크기가 클수록 브라우저에 표시하는 데 필요한 리소스를 다운로드하는 데 시간이 오래 걸리며, 페이지 로딩 속도가 느려지는 것을 경험한 사용자는 재방문할 가능성이 낮아집니다! 또한 모바일 기기로 브라우저를 이용하거나 네트워크에 문제가 있는 경우, 적절한 프로젝트 크기를 유지하는 것은 특히 중요합니다.

> 웹 개발 분야에서 크기가 중요한 이유에 대해 더 자세히 알고 싶으신가요? KeyCDN의 글: [웹 페이지 크기의 증가](https://www.keycdn.com/support/the-growth-of-web-page-size)를 확인하세요.

따라서 번들 크기가 제어되지 않고 증가하면 금방 문제가 될 수 있습니다. [트리 쉐이킹](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking), [지연 로딩](https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading), 사용하지 않는 종속성 제거 등 이미 언급한 것처럼 번들 크기를 작게 만드는 다양한 노하우와 방법이 있습니다.

하지만 이 글에서는 라이브러리 및 이미지를 다루는 PR에서 즉각적으로 큰 효과를 볼 수 있는 몇 가지 간단한 변경 사항을 소개하겠습니다.

<br>

### 더 작은 라이브러리 사용하기

설치하는 패키지의 크기를 염두에 두고 설치 시 전체 번들 크기가 어떻게 증가하는지 기록해 두는 것이 좋습니다.

다행히도 이 작업을 더 쉽게 하기 위해 라이브러리를 추가한 후 프로젝트의 번들 크기가 어떻게 영향을 받는지 보여주는 성능 측정 도구인 **[Size Limit](https://evilmartians.com/opensource/size-limit)**을 사용할 수 있습니다. Size Limit은 브라우저에서 코드를 다운로드하고 실행하는 데 걸리는 시간도 계산할 수 있습니다.

또한 여러 패키지 중에서 하나를 선택할 때 라이브러리 크기를 적절히 고려하면 작은 번들 크기를 보장할 수 있습니다. **[Bundlephobia](https://bundlephobia.com/)**는 npm 패키지의 크기를 확인하고 애플리케이션 성능에 미치는 영향을 분석하는 도구로 이 작업을 매우 쉽고 편리하게 해줍니다. 또한 특정 라이브러리의 크기를 단순히 표시하는 것 외에도 라이브러리 구성에 대한 종속성의 크기 효과, npm에서 다운로드 시간 등 다른 유용한 개발 정보도 제공합니다.

<br>

### 최적화된 이미지 사용하기

사진과 아이콘은 사이트 전체 리소스의 상당 부분을 차지하므로 이미지 크기가 작으면 프로젝트의 전체 크기에 큰 영향을 미칠 수 있습니다. 이에 대한 간단한 예시를 살펴보겠습니다.

페이지에 우주 공간의 큰 사진을 배치하고 싶다고 가정해 보겠습니다. 멋진 사진을 찾았지만 최적화되지 않은 버전은 9.8MB이고 PNG 형식이었습니다.

![img](https://evilmartians.com/static/6e1c781f0c5bf9acd6e1c9b09ebe9113/7db83/space.avif)

성능 측정 도구인 **[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)**를 통해 페이지에서 이 이미지를 렌더링하는 시간을 측정해보니, 50초 이상 걸리는 등 모바일 기기에서 성능이 매우 나쁜 것으로 나타났습니다!

![img](https://evilmartians.com/static/089d9edc1f6959139cafc1eb82bff7fb/08f0f/lighthouse-before.avif)

이 문제를 해결하기 위해 **[Squoosh](https://squoosh.app/)**가 구세주처럼 등장했습니다. 이미지 크기를 압축하고 줄여주는 정말 편리한 웹 앱입니다. 또한 압축 후 이미지를 즉시 보여주기 때문에 성능과 이미지 품질의 균형을 즉시 확인할 수 있다는 점도 매우 유용합니다. Squoosh를 사용하면 모든 최신 이미지 포맷으로 작업하고 이미지 포맷으로 작업 및 변환을 수행할 수 있습니다.

> 압축할 이미지가 많은 경우, [ImageOptim](https://imageoptim.com/)은 일괄 최적화에 특히 편리합니다. [Mac에서 다운로드](https://imageoptim.com/mac)하거나 원하는 OS의 [웹 버전](https://imageoptim.com/versions.html)을 사용하세요.



<br>

### 크기를 염두에 두고 적절한 이미지 형식을 사용하는 것도 매우 중요하며, WebP 및 AVIF와 같은 새로운 형식은 PNG와 같은 오래된 형식보다 성능이 더 좋습니다.

이제 Squoosh를 사용하여 우주 이미지를 더 작게 만들고 형식을 WebP로 변경해 보겠습니다. 그러면 100KB가 조금 넘는 최적화된 이미지가 생성됩니다. 지표를 다시 살펴봅시다.

![img](https://evilmartians.com/static/5acc68a747067964118794376548e836/ec502/lighthouse-after.avif)

특히 위 이미지에서 크게 개선된 총 차단 시간(Total Blocking Time,TBT는 매우 중요한 성능 지표입니다)을 주목하세요.

벡터 및 래스터 그래픽 콘텐츠 최적화에 대해 자세히 알아보려면 이 게시글을 참조하세요.

<br>

<br>

## 2. 사용하지 않는 종속성을 포함하지 않기

새로운 기능을 구현하는 과정에서 여러 패키지를 추가한 경우, PR에 모든 패키지가 정말 필요한지 확인하세요.

### 불필요한 종속성은 프로젝트 크기를 늘리고 설치 속도를 늦추며 개발자를 혼란스럽게 합니다.

프로젝트에 불필요한 종속성이 있는지 확인하는 데 가장 유용한 도구 중 하나는 **[depcheck](https://www.npmjs.com/package/depcheck)**입니다. depcheck는 프로젝트의 종속성을 분석하여 사용되지 않는 종속성 목록을 제공합니다.

<br>

<br>

## 3. 접근성 지원하기

모든 사용자가 콘텐츠와 기능에 접근할 수 있도록 하는 것은 정말 중요하며, 개발 과정에서 이를 염두에 두어야 합니다. 디지털 접근성(흔히 a11y로 약칭)이라는 주제는 매우 광범위하며, 더 나은 경험을 제공하기 위한 다양한 접근 방식이 있습니다. 염두에 두어야 할 몇 가지 기본 사항부터 시작해 보겠습니다.

<br>

### 키보드 접근성 보장하기

새 기능이 포함된 PR을 열기 전에 간단한 접근성 테스트를 수행하여 키보드만으로 기능을 사용할 수 있어야 합니다. 이는 마우스를 사용하지 않는 사용자에게 매우 중요합니다.

> [키보드 네비게이션에 대해 자세히 알아보고](https://webaim.org/techniques/keyboard/) 잠재적인 문제와 테스트 기술에 대해 알아보세요.
>
> <br>

### 미디어 콘텐츠에 텍스트를 함께 제공하기

페이지에 단순한 장식용이 아닌 이미지가 있는 경우, 스크린 리더를 사용하는 사람들이 콘텐츠를 더 잘 이해할 수 있도록 이미지를 설명하는 간결한 **[alt 텍스트](https://accessibility.huit.harvard.edu/describe-content-images)**를 제공하세요.

```diff
- <img src="images/contrast-comparison.jpg"/>
- <img src="images/contrast-comparison.jpg" alt="Contrast Comparison" />
+ <img src="images/contrast-comparison.jpg" alt="On the left, there is a demonstration of low color contrast which makes words hard to read. On the right, higher color contrast makes the text easier to read." />
```

비디오 또는 오디오 콘텐츠가 있는 경우, 캡션을 제공하면 해당 콘텐츠를 사용하는 사람들에게 큰 도움이 될 것입니다.

<br>

### 색상 대비가 높은 가독성 있는 글꼴 사용하기

사용자 지정 글꼴을 사용한다면 글꼴이 명확하게 읽히는지 확인하세요. 멋지고 아름다운 글꼴이 많지만 일부 사용자에게는 읽기 어려울 수 있습니다. 마찬가지로 글꼴 색 구성표를 염두에 두고 대비가 높고 뚜렷한 값을 선택해야 합니다. 적절한 대비가 없으면 사용자가 중요한 정보를 알아채지 못하거나 이해하지 못할 수 있습니다.

> [이 사이트에서 나열된 것들과 같은 색상 대비 도구](https://www.chhs.colostate.edu/accessibility/best-practices-how-tos/color-contrast-tools/)를 사용하여 사이트를 쉽게 확인할 수 있습니다.

Very important information

하지만 색상 대비가 높으면 페이지의 텍스트 및 기타 요소가 더 쉽게 눈에 띄게 됩니다.

Very important information

개발 과정에서 디자이너와 함께 작업하고 소통하면 접근성 관련 문제를 방지하는 데 도움이 됩니다.

접근성 디자인에 대해 더 자세히 알고 싶으신가요? 이 글을 읽어보세요.

<br>

<br>

## 4. 시맨틱 마크업 사용하기

이 내용은 이전 문단의 내용과 밀접하게 연결되어 있습니다. 우선, 시맨틱 HTML은 스크린 리더가 페이지를 더 잘 해석하기 때문에 사이트의 접근성을 개선하는 또 다른 방법입니다.

그 외에도 시맨틱 태그의 또 다른 장점은 검색 엔진이 페이지의 콘텐츠와 구조를 더 효과적으로 인식하도록 도와주어 검색 순위를 높일 수 있다는 것입니다.

> PR에 form이 있나요? 시맨틱 HTML, 접근성 등에 대한 전문적인 팁을 포함하여 PR을 보내기 전에 이 문서에서 다른 체크리스트를 확인하세요.

시맨틱 마크업 덕분에 팀의 다른 개발자들이 페이지의 구조와 계층 구조를 명확하게 이해할 수 있다는 점도 장점입니다.

HTML을 더 시맨틱하게 만드는 방법은 무엇일까요? 핵심은 외형이 아닌 의미에 따라 HTML 요소를 사용하는 것입니다.

예를 들어 페이지에 클릭 가능한 요소가 있는 경우, `<div>`가 아닌 `<button>` 또는 `<a>`태그를 사용하세요. 물론 스타일을 추가하여 `<div>`를 버튼처럼 보이게 할 수도 있지만, `<div>`와 달리 `<button>` 또는 `<a>` 태그는 문서의 탭 순서에 자동으로 추가되므로 키보드를 사용하여 초점을 맞출 수 있고 엔터 키를 눌러 활성화할 수 있습니다.

```diff
- <div>Sign In</div> //  Tab키로 선택할 수 없음
+ <button>Sign in</button> // Tab키로 선택 가능
```

HTML 태그를 올바르게 사용하는 것 외에도 태그에 사용하는 속성의 의미에 주의를 기울이는 것도 중요합니다. 특정 태그와 함께 일부 속성을 사용하거나 사용하지 않아야 합니다. 예를 들어 아이콘 전용 버튼을 사용하는 경우, 명확한 `aria-label` 값을 추가하세요. 반대로 버튼에 텍스트가 있는 경우, `aria-label`을 추가하면 중복됩니다. 마찬가지로 `<button>` 요소에 `role="button"`을 넣는 것도 버튼의 모양이나 기능에 영향을 주지 않으므로 불필요합니다.

이 주제는 심도 있는 주제이므로 HTML의 시맨틱을 더욱 개선하는 데 관심이 있다면 이 글을 계속 읽어보시기 바랍니다. **[Semantic HTML](https://web.dev/learn/html/semantic-html/)**.

<br>

<br>

## 5. 불필요한 리렌더링 방지하기

자바스크립트 프레임워크로 작업할 때 거의 필연적으로 리렌더링이 발생하는데, 이는 업데이트된 상태의 결과로 UI를 업데이트하는 프로세스입니다. 상태 업데이트는 일반적으로 사용자가 웹 페이지와 상호 작용할 때 또는 HTTP 요청을 통해 일부 데이터를 수신할 때 발생합니다.

하지만 가끔 불필요한 리렌더링이 발생하는 경우가 있습니다. 이는 컴포넌트 아키텍처의 실수 또는 단순한 임의의 오류로 인해 발생할 수 있습니다. 이러한 경우 사용자가 인터페이스와 상호작용할 때 눈에 띄는 지연이 발생하거나 시간이 지나면 완전히 응답하지 않을 수도 있습니다.

먼저 브라우저에서 페이지의 컴포넌트가 리렌더링되는 횟수를 확인할 수 있으며, 확인해야 합니다. 이를 확인하는 쉬운 방법 중 하나는 크롬 개발자 도구의 'Rendering' 탭에서 'Paint Flashing' 설정을 활성화하는 것입니다. 이 옵션은 페이지의 섹션이 렌더링될 때마다 편리한 시각화를 제공하므로 불필요한 리렌더링을 평가하는 데 매우 편리합니다.

> 이 글은 [Paint flashing을 활성화하는 기능과 방법에 대한 빠른 가이드](https://calibreapp.com/blog/investigate-animation-performance-with-devtools#chrome-devtools-paint-flashing)입니다.

또 다른 옵션은 이 기능이 있는 **[크롬](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)** 또는 **[파이어폭스](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/)**용 React Devtools 브라우저 확장 프로그램을 사용하는 것입니다.

그렇다면 애플리케이션이 너무 자주 리렌더링된다는 사실을 알게 되면 어떻게 해야 할까요?

<br>

먼저 코드에 무한 루프가 없는지 확인하세요. 예를 들어, 리액트에서 `useEffect` 훅의 종속성으로 자신이 의존하는 변수의 상태를 설정하면 무한 루프가 발생합니다.

```jsx
const TestComponent () => {
 const [textValue, setTextValue] = useState('');
 const [changesCount, setChangesCount] = useState(0);


 useEffect(() => setChangesCount(changesCount + 1), [textValue, changesCount]);


 return <input value={textValue} onChange={(event) =>  setTextValue(event.target.value)} />;
};
```

`textValue`는 인풋의 텍스트를 나타내고 `changesCount`는 사용자가 이 텍스트를 변경한 횟수를 나타냅니다. `useEffect` 훅에서 종속성으로 보이는 변수를 사용하기 때문에 이 코드를 실행하면 `Maximum update depth exceeded` 오류가 무한대로 표시됩니다. 이 문제는 `useEffect`를 다음과 같이 작성하여 해결할 수 있습니다.

```jsx
useEffect(() => setChangesCount(count => count + 1), [textValue]);
```

리렌더링의 또 다른 원인은 지저분한 애플리케이션 아키텍처입니다. 예를 들어, 많은 단계의 컴포넌트를 통해 긴 체인의 props를 전달하는 경우입니다. 이를 방지하기 위해 상태 로직을 컴포넌트에서 스토어로 옮길 수 있습니다. 초소형 상태 관리자 **[Nano Stores](https://evilmartians.com/opensource/nano-stores)**는 이러한 접근 방식을 촉진하고 이를 쉽게 수행할 수 있도록 지원합니다.

<br>

> 리액트 프로젝트의 속도를 높이는 방법을 모르시나요? 아래의 글은 앱 성능을 눈에 띄게 개선하고 일반적인 실수를 피하는 방법을 설명합니다.

[![img](https://velog.velcdn.com/images/surim014/post/014ff3d9-9e74-4db4-8cce-d69bd0ace0b3/image.png)](https://evilmartians.com/chronicles/optimizing-react-virtual-dom-explained)

성능을 개선하기 위해 값비싼 계산을 메모이제이션하는 것도 유용할 때가 있지만, 이는 신중하게 수행해야 합니다. 이 훌륭한 글에서는 **[리액트 훅을 사용하면 성능에 부정적인 영향을 미칠 수 있는 경우](https://kentcdodds.com/blog/usememo-and-usecallback)**에 대해 설명합니다.

리액트로 개발하면서 리렌더링과 메모이제이션 개념에 대해 더 깊이 이해하고 싶으시다면, 여기 몇 가지 훌륭한 자료를 참고하세요. **[Why React Re-Render](https://www.joshwcomeau.com/react/why-react-re-renders/)**는 리렌더링이 발생하는 이유와 불필요한 리렌더링을 피하는 방법에 대한 자세한 설명이며, **[Understanding useMemo and useCallback](https://www.joshwcomeau.com/react/usememo-and-usecallback/)**은 리액트의 메모이제이션 프로세스에 대한 완벽한 설명을 제공합니다.

<br>

<br>

## 6. 사용자 입력 새니타이징(Sanitize)하기

웹 애플리케이션 개발에서 취약점을 예방하는 것도 언급할 가치가 있는 또 다른 큰 주제입니다. JS에서 가장 크고 가장 흔한 보안 취약점 중 하나는 사용자 입력과 관련이 있습니다. 공격자는 임의의 작업을 수행하기 위해 악성 스크립트를 삽입하여 양식의 입력을 사용하여 악성 코드를 실행하려고 시도할 수 있습니다. 데이터 입력값을 새니타이징(즉, 검사, 정리, 필터링)하면 사이트에서 이러한 유형의 공격에 대한 방어 기능을 제공합니다.

HTML 문자열을 새니타이징하는 데는 여러 가지 옵션이 있습니다. **[HTML Sanitizer API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Sanitizer_API)**의 메서드를 사용하거나 간단한 HTML sanitizer가 포함된 라이브러리인 **[sanitize-html](https://www.npmjs.com/package/sanitize-html)**을 사용할 수 있습니다. 후자를 사용하면 HTML을 매우 쉽게 새니타이징할 수 있습니다.

```diff
const userInputValue = "<img src=x" onerror="alert('Some malicious code')";
- performHTML("<img src=x" onerror="alert('Some malicious code')">"); // onError 시 악성 코드를 실행합니다.
+ performHTML(sanitizeHtml("<img src=x" onerror="alert('Some malicious code')">")); // <img src=x"> 일때만 실행됩니다.
```

이는 웹 보안의 빙산의 일각에 불과하며, PR에서 간과하기 쉬운 부분입니다. 더 자세히 알고 싶으시다면 **[MDN 웹 문서의 공격 유형](https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks)**에 대한 글을 읽어보시기 바랍니다.

<br>

<br>

## 7. 코드를 최대한 깔끔하게 작성하기

이것은 이 글에서 가장 주관적이고 복잡한 권장 사항입니다. 코드 간결성에 관한 많은 책과 기사가 작성되었으며, 이 주제에 대한 열띤 논쟁이 계속되고 있습니다.

사실, "클린 코드"를 정확히 무엇으로 구성하는지에 대한 프로그래머의 의견이 다양하기 때문에 이것은 복잡한 주제입니다. 그럼에도 불구하고 "더티 코드"는 프로젝트를 서서히 죽이고 버그의 양을 증가시키며 유지보수성을 떨어뜨리기 때문에 매우 중요한 주제입니다.

따라서 PR 검토를 위해 코드를 보내기 전에 코드의 품질을 향상시킬 수 있는 몇 가지 일반적인 팁을 다루겠습니다.

<br>

### 복잡한 것을 분해하기

새로운 함수나 컴포넌트에 너무 많은 책임이 있는 경우 자세히 살펴보세요. 기능이 여러 가지 작업을 수행하고 쉽게 분리할 수 있는 요소를 포함하는 경우, 기능을 더 작은 부분으로 분해하는 것이 좋습니다.

예를 들어, 아래 함수는 배열의 요소 수를 특정 속성으로 계산한 다음 총 개수를 구하여 반환하는 두 가지 작업을 수행합니다.

```js
const funcThatDoesEverything = (list1, list2, list3) => {
   let count1 = 0;
   for (let i = 0; i < list1; i++) {
     count1 += ...
     // list1의 일부 항목을 계산하는 코드
   }
   let count2 = 0;
   for (let i = 0; i < list2; i++) {
     count2 += ...
     // list2의 일부 항목을 계산하는 코드
   }
   let count3 = 0;
   for (let i = 0; i < list3; i++) {
     count3 += ...
     // list3의 일부 항목을 계산하는 코드
   }
   const totalCount = count1 + count2 + count3;
   return totalCount;
 }
```

<br>

이를 쉽게 재작성하고 더 읽기 쉽고 재사용 가능한 코드로 분해할 수 있습니다.

```js
// list에서 일부 항목을 가져오는 함수
 const getCountOfSomeItems = (list) => ...


 const getTotalCountForLists = (list1, list2, list3) => {
   const totalCount = getCountOfSomeItems(list1) +    getCountOfSomeItems(list2) + getCountOfSomeItems(list3);
   return totalCount;
 }
```

하나의 함수를 두 개의 다른 함수로 분할하는 것 외에도 변수 이름을 더 명확하게 만들었습니다.

코드를 분해해야 하는 또 다른 징후는 애플리케이션 내에서 코드가 몇 가지 부분에서 반복되기 시작하는 경우입니다. 이런 일이 발생하면 반복되는 부분을 추출하여 재사용할 수 있는지 확인해보세요.

<br>

### 코드 네이밍시, 시맨틱을 염두에 두기

때때로 변수와 함수 이름을 명확하고 좋은 이름으로 유지하는 것은 매우 어려운 작업입니다. 그럼에도 불구하고 이는 코드의 명확성과 유지보수를 위해 매우 중요합니다.

간단한 예로, 프로그램에 다양한 과일 목록이 있고 가격이 높은(300 이상) 과일 목록을 정의하고 싶다고 가정해 보겠습니다. 이 변수에 대한 코드는 다음과 같이 작성할 수 있습니다.

```js
const filtered = fruitArr.filter((f) => f.price >= 300);
```

하지만 이 네이밍을 사용하면 1년 후에 다시 돌아왔을 때 높은 가격의 limit을 의미하는 변수를 변경해야 하는 부분이 명확하지 않을 수 있습니다.

<br>

아래 코드를 사용하면 훨씬 쉬워집니다.

```js
const MIN_HIGH_PRICE = 300;
const expensiveFruits = allFruits.filter(
 (fruit) => fruit.price >= MIN_HIGH_PRICE
);
```

물론 네이밍에 대한 질문은 매우 주관적일 수 있으며, 적절한 변수 네이밍에 대한 많은 조언에는 모순이 포함되어 있기도 합니다. 하지만 한 가지 권장 사항을 남겨두겠습니다. 문맥이 고려되지 않은 변수 명을 처음 본다고 상상해 보세요. 무슨 일이 일어나고 있는지 기본적인 개념이라도 이해할 수 있을까요? 그렇지 않다면 무언가를 고쳐야 할 때입니다.

<br>

### 코드 포맷팅 및 린팅에 통합 도구 사용하기

팀에서 린터를 사용하지 않는다면 꼭 한번 사용해 보세요. **[자바스크립트 코드용 ESLint](https://eslint.org/)**와 **[CSS용 stylelint](https://stylelint.io/)**는 프로젝트에서 코딩 규칙을 적용하는 데 큰 도움이 됩니다. 동료들과 바람직한 규칙에 대해 합의하고 원하는 대로 이러한 도구의 구성을 설정할 수 있습니다.

또한 자바스크립트 및 CSS 파일 서식을 지정하는 도구는 린터와 함께 사용할 때 훌륭하게 작동하므로 IDE에서 사용하는 것이 좋습니다. 예를 들어, **[Prettier](https://prettier.io/)**가 있습니다.

이러한 도구를 사용하면 코드의 품질이 훨씬 좋아지고 코드 스타일에 대해 더 이상 열띤 토론(종종 상당히 낭비적인 토론)을 할 필요가 없습니다. 포맷터와 린터가 만족스럽다면 일반적으로 코드 스타일에 대한 모든 것이 좋다고 볼 수 있습니다.

'Format on Save' 설정을 활성화한 상태에서 파일을 저장하면 다음 스크린샷의 코드가 어떻게 변하는지 비교해서 보세요.

```js
const insertNode = (node, newNode) => {
    if(newNode.data < node.data)
    {
        if(node.left === null)
            node.left = newNode;
        else
          insertNode(node.left, newNode)
    }
    else
    {
        if (node.right) === null)
            node.right = newNode
        else

          insertNode(node.right,newNode);
    }
}
```

<br>

다음 코드로 바뀝니다.

```js
const insertNode = (node, newNode) => {
    if (newNode.data < node.data) {
      if (node.left === null) node.left = newNode;
      else insertNode(node.left, newNode);
    }
    else {
      if (node.right) === null) node.right = newNode;
      else insertNode(node.right, newNode);
    }
}
```

코드가 이러한 규칙과 제약을 따르고 있는지 확인하려면 새로운 내용을 커밋하기 전에 파일에 있는 코드에 자동으로 명령을 적용할 수 있는 오픈 소스 프로젝트인 **[Lefthook](https://evilmartians.com/opensource/lefthook)**을 사용할 수 있습니다.

이 글에서는 Lefthook으로 사전 커밋 훅을 구성하고, Prettier로 자바스크립트 및 CSS 파일을 포맷하고, ESlint 및 stylelint로 린팅하는 방법에 대해 설명합니다.

<br>

## 📑 요약

코드가 제대로 작동하는지 확인한 후, 새로 작성한 풀 리퀘스트에 대한 검토를 요청하기 전에 다음 목록에 따라 코드를 확인하세요.

1. 번들 크기 최소화하기: 이미지를 최적화하고 새로운 라이브러리는 가능한 한 작아야 합니다.
2. 새로 추가된 모든 종속성이 실제로 필요한지 확인합니다.
3. 새로운 기능에 액세스할 수 있는지 확인하기: 키보드로 사용할 수 있어야 하고, 이미지에는 대체 텍스트가 있어야 하며, 글꼴은 선명하고 대비가 높은 색 구성표를 사용해야 합니다.
4. HTML 요소는 적절한 태그와 올바른 속성을 사용하여 의도한 대로 시맨틱 태그를 사용해야 합니다.
5. UI 지연을 유발할 수 있는 불필요한 리렌더링이 없는지 확인합니다.
6. 사용자 입력값을 새니타이징해야 합니다.
7. 코드를 최대한 깔끔하게 작성하세요.

이 체크리스트를 따르면 애플리케이션의 품질을 높이는 데 도움이 되며, 버그를 줄이고 동료의 골칫거리를 예방할 수 있습니다.

언제든지 항목을 추가하거나 변경하여 개인 목록을 만들 수 있습니다! 좋은 제안이 있으시면 언제든지 알려주세요.

한 가지 더, 동료가 검토를 요청하기 전에 실수로 다시 확인하는 것을 잊었다면 관대하게 대해주세요. 누구나 가끔은 실수할 수 있으니까요. 대신 이 글을 보여주세요!



<br>

<br>

#### 참고자료: [[번역\] 프런트엔드 풀 리퀘스트를 작성하기 전에 이 체크리스트를 사용하세요. (velog.io)](https://velog.io/@surim014/before-your-next-frontend-pull-request-use-this-checklist)

<br>