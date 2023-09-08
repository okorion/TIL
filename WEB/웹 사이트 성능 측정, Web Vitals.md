## 🧭 웹 사이트 성능 측정, Web Vitals

## '그래서 얼마나 좋아진 건가요?'

웹 사이트의 성능은 어느 정도 정량적으로 측정될 수 있습니다. 여러 가지 지표와 방법론이 있겠지만, 일반적으로는 Google의 [Web Vitals](https://web.dev/vitals/) 메트릭을 주요한 가이드라인으로 삼습니다.

> Web Vitals는 Google 검색 순위를 결정하는 요소로도 활용됩니다. [참고](https://developers.google.com/search/blog/2020/11/timing-for-page-experience)

'사용자 경험' 이라는 개념을 다룰 때, 이게 중요하다는 건 알겠는데 구체적으로 설명하거나 측정하기는 좀처럼 쉽지 않습니다. 추상적이고 모호한 부분이기 때문입니다. `Web Vitals`는 사용자가 체감할 수 있는 성능을 수치화한 것이므로, 이런 문제를 어느 정도 와닿을 수 있게 이해하고 설명하는 데 활용할 수 있습니다.

![img](https://velog.velcdn.com/images/sejinkim/post/4db325c9-1d6e-4c77-9adb-ae6a017cb91c/image.avif)

물론 사용자 경험이 성능으로만 결정되는 것은 아닙니다. 하지만 절대적인 지분을 차지하는 것도 사실입니다. 일단 페이지가 빠르게 렌더링되고, 기능이 잘 동작해야 그 다음을 판단할 수 있을 것이므로 당연한 이치입니다. '로딩 시간을 몇 초 단축시켰더니 사용자들의 이탈률이 몇 퍼센트 줄고, 매출이 얼마 증가했다더라' 하는 성공 사례는 굉장히 흔하게 인용됩니다. 역시 개발자에게 있어서는 **Performance Matters**, 성능 문제가 제일의 화두인 셈입니다.

개인적으로도, 회사에서 무언가 업무를 진행할 때면 항상 이 성능 문제를 고민해야 했습니다. 서비스 업력이 오래되어 코드 베이스가 노후되었고, 아직 경험도 부족해 '그냥 다 갈아엎고 처음부터 새로 만드는 것' 말고는 마땅한 해결책을 생각해내기가 어려웠던 상황에서, 꾸준히 무언가 비즈니스 피처는 추가하며 개발을 해야 했기 때문입니다.

어쨌든 어딘가 느리다고 한다면 구체적으로 어떻게 느린 건지, 또 개선 작업을 했다고 하면 어느 부분이 개선이 된 건지를 스스로도 이해하고 파악할 필요가 있었고, 또 그걸 다른 사람들에게 공유하고 설명할 수 있어야 했습니다. `Web Vitals`는 이런 상황에서 아주 유용한 데이터가 되었습니다.

------

## Web Vitals

`Web Vitals`는 아래와 같은 메트릭으로 구성됩니다. 제각기 초점을 두는 문제가 다르고, 여러 변인들로 인해 항상 정확하고 절대적인 수치를 제공해주지는 않으며, 정의를 정확하게 알아야지만 이해할 수 있기 때문에 자세히 살펴볼 필요가 있습니다.

### 1. 로딩 (Loading)

#### Time To First Byte, TTFB

![img](https://velog.velcdn.com/images/sejinkim/post/b65dda5d-953f-4674-a99b-1da7feaac046/image.png)

브라우저가 웹 페이지 리소스 요청의 응답에 대해, 첫 번째 바이트를 수신하기까지 소요된 시간을 나타냅니다. 연결을 설정하고, 웹 서버가 응답한 시간을 측정하는 메트릭으로, **사용자가 페이지에 진입하는 시점**이 빠른지, 느린지를 알 수 있습니다. 백엔드 레벨의 문제를 파악하기에 적절합니다.

![img](https://velog.velcdn.com/images/sejinkim/post/05de9ae9-7bbe-4e4f-9bea-588a3ba5b145/image.avif)

위 이미지에서 `startTime`와 `responseStart` 시점 사이에 소요된 시간으로, 아래 프로세스들로 구성됩니다.

- 리디렉션 시간
- [서비스 워커](https://developer.mozilla.org/ko/docs/Web/API/Service_Worker_API) 시작 시간
- DNS 조회
- 연결 설정 및 TLS 협상(핸드쉐이크)

일반적으로 **0.6 ~ 0.8초 이내**가 권장되며, 사용자 입장에서 체감하기 쉬운 영역이기 때문에, 과도하게 지연되고 있다면 개선이 필요합니다.

특히 웹 페이지 렌더링 방식으로 `SSR(Server-Side Rendering)`을 채택할 때 문제가 될 가능성이 높은 부분이기도 한데, 서버에서 데이터를 fetch하고 document를 완성하는 데 소요된 시간이 그대로 반영되기 때문입니다.

그래서 `TTFB`는 `SSR`에서 대체로 불리하게 측정되는 반면, 아래에서 설명할 `LCP` 메트릭은 `CSR(Client-Side Rendering)`에서 열악하게 측정될 수 있는 등, 렌더링 프로세스에 따라 차이가 있을 수 있다는 점도 알아두면 좋습니다.

web.dev에서 설명하는 내용에 따르면, `TTFB`를 개선할 수 있는 방법으로 다음의 방법들을 제시하고 있습니다.

> - [다중 리디렉션 회피](https://web.dev/redirects/)
> - [필수 외부 리소스에 사전 연결하기](https://web.dev/uses-rel-preconnect/)
> - HTTP-to-HTTPS 리디렉션 대기 시간을 제거하기 위해 [HSTS preload](https://hstspreload.org/) 설정하기
> - [HTTP/2](https://web.dev/uses-http2/), [HTTP/3](https://en.wikipedia.org/wiki/HTTP/3) 사용하기
> - [Predictive Prefetching(예측 프리페칭)](https://web.dev/predictive-prefetching/) 사용하기

#### First Contentful Paint, FCP

![img](https://velog.velcdn.com/images/sejinkim/post/2cd50aed-5969-44c1-acab-804bcf830fdf/image.png)

페이지가 로드되기 시작한 시점부터, 화면에 처음으로 콘텐츠가 렌더링될 때까지의 시간을 측정한 수치입니다. 이때 콘텐츠란 텍스트, 이미지, svg, 흰색이 아닌 canvas 요소를 의미합니다. 가령 로딩 인디케이터/스피너 같은 요소가 노출되는 순간도 `FCP` 시점으로 측정될 수 있습니다.

![img](https://velog.velcdn.com/images/sejinkim/post/20ec196d-6242-4526-a21f-ec5d0ee8718f/image.avif)

**1.8초 이내** 수준일 때 사용자 경험 측면에서 우수하다고 하며, 일단 페이지가 그냥 흰 화면이 아닌, 뭐라도 보이기 시작한 시점이기 때문에 사용자 입장에서는 실질적으로 **로딩의 시작을 인지하기 시작하는 시점**입니다. 페이지가 유의미하게 모두 페인트된 것은 아니니 핵심적인 메트릭은 아니라고 할 수 있지만, 체감적인 측면에서 로딩 속도를 결정하는 요소가 될 수 있어 중요합니다.

`FCP`를 개선하기 위한 방법은 다양한데, 아래와 같이 웹 페이지 성능 최적화 문제의 전반을 다루고 있다고 해도 과언이 아닙니다.

> - [렌더링 차단 리소스 제거하기](https://web.dev/render-blocking-resources/)
> - [CSS 축소(minify)하기](https://web.dev/unminified-css/)
> - [사용하지 않는 CSS 제거하기](https://web.dev/unused-css-rules/)
> - [대규모 네트워크 페이로드 방지하기](https://web.dev/total-byte-weight/)
> - [정적 에셋 리소스에 적절한 캐시 정책 적용하기](https://web.dev/uses-long-cache-ttl/)
> - [과도한 DOM 크기/깊이 지양하기](https://web.dev/dom-size/)
> - [Critical Rendering Path](https://web.dev/critical-rendering-path/) [연결에 의한 영향 최소화하기](https://web.dev/critical-request-chains/)
> - [웹폰트 로드 중에도 텍스트가 표시되도록 하기](https://web.dev/font-display/)
> - [리소스 요청 수를 최소화하고 전송 크기를 작게 하기](https://web.dev/resource-summary/)

#### Largest Contentful Paint, LCP

![img](https://velog.velcdn.com/images/sejinkim/post/576fdfef-61ee-4f5d-9ae9-227a61122979/image.png)

페이지 로드가 시작된 시점부터, 뷰포트 내에서 가장 큰 콘텐츠(텍스트, 이미지, 비디오...)가 렌더링된 시점까지 소요된 시간을 측정한 메트릭입니다. 일반적으로 **2.5초 이내**일 때 우수하다고 봅니다.

사용자가 실제로 로딩이 (거의) 완료되었다는 사실을 인지하려면, 그 페이지에서 가장 핵심적인 **'메인 콘텐츠'**들이 눈에 들어와야 합니다. 하지만 프로파일러 입장에서는 페이지 내에서 무엇이 메인 콘텐츠인지를 파악하기가 어렵기 마련입니다.

때문에 여러가지 메트릭으로 핵심에 근접하기 위한 시도들이 이루어졌었는데, 대부분 복잡하거나 정확하지 않다는 문제가 있었습니다.

그러다 결국 단순한 접근이 가장 효과적이라는 사실을 알게 되었는데, 대체로 물리적으로 크기가 큰 요소는 실제로도 의미 있는 콘텐츠일 가능성이 높다는 것이었습니다. 그래서 `LCP`는 **실질적인 로딩 완료 시점**을 나타내는 핵심 메트릭이 되었습니다.

> 요소의 크기를 판단할 때, 아래와 같은 부분은 고려되지 않습니다.
>
> - 뷰포트 외부로 확장되거나 잘려서 보이지 않는(overflow) 영역
> - CSS box model에서의 margin, padding, border
> - 기본 크기(intrinstic size)에서 축소 조정되어 표시된 이미지인 경우, 가시적 크기(rendered size)가 아닌 기본 크기를 기준으로 합니다.

그런데, 페이지 렌더링 방식에 따라 측정 시점이 모호할 수 있습니다. `CSR(Client-Side Rendering)`의 경우가 그러한데, 페이지의 요소들이 단계적으로 로드될 것이기 때문입니다. 예를 들어 텍스트 블록과 대표 이미지가 존재하는 경우, 대체로 이미지 렌더링 시점이 더 늦기 마련이므로 텍스트가 먼저 `LCP` 시점으로 측정될 수 있습니다.

![img](https://velog.velcdn.com/images/sejinkim/post/e284b559-4429-4aa3-93b7-0baff8c3a26b/image.avif)

때문에 브라우저에 큰 요소가 렌더링될 때마다 `LCP` 시점을 변경하는 방법을 통해 이러한 케이스를 보완하게 됩니다. 무언가 뒤늦게 새로운 요소가 렌더링되었고, 이것이 이전 `LCP` 요소보다 큰 경우라면 메트릭이 갱신됩니다. 만약 `LCP` 요소가 제거되더라도, 이것보다 더 큰 요소가 새로 렌더링되지 않는 이상 삭제된 이전의 요소가 `LCP` 요소로 유지됩니다.

![img](https://velog.velcdn.com/images/sejinkim/post/49fe7e79-c0e2-45ca-8db5-4d43fd52aa35/image.avif)

앞서 크기가 큰 콘텐츠가 대체로 메인 콘텐츠일 가능성이 높다고 했지만, 어디까지나 경향성에 기반한 추론(휴리스틱)이므로 얼마든지 `LCP`가 메인 콘텐츠를 의미하지 않는 경우가 있을 수도 있습니다.

이때는 개발자가 직접 메인 콘텐츠를 지정해주어야 하며, [사용자 지정 메트릭](https://web.dev/custom-metrics/#element-timing-api)이라는 것을 활용해볼 수 있습니다.

`LCP`를 최적화하는 방법은 아래 아티클을 참고합니다. 기본적으로 `TTFB`, `FCP`가 양호해야 `LCP`도 우수할 수 있습니다.

> - [최대 콘텐츠풀 페인트 최적화(느린 리소스 로드 시간 최적화, 클라이언트 사이드 렌더링 최적화 ...)](https://web.dev/optimize-lcp)

### 2. 상호작용/반응성 (Interactivity)

#### Total Blocking Time, TBT

브라우저의 메인 스레드가 사용자의 입력에 대한 응답을 오래 차단했을 때, `FCP` 시점부터 아래 설명할 `TTI(Time To Interactive)` 시점까지의 시간을 측정한 메트릭입니다.

'차단(Blocking)'은 메인 스레드에서 '긴 작업(Long Task)'이 발생한 경우를 의미하는데, 이때 기준은 **50ms**입니다. 만약 어떤 작업이 실행 중일 때 사용자가 페이지와 상호작용하려 했다면, 브라우저는 일단 처리 중이었던 작업이 완료되어야만 응답할 수 있습니다. 그래서 이것을 차단이라고 표현하는 것이며, 50ms 정도를 넘어가면 사용자는 답답한 느낌을 받게 됩니다.

![img](https://velog.velcdn.com/images/sejinkim/post/49929c95-31db-4433-8b63-ecbd062d3075/image.png)
![img](https://velog.velcdn.com/images/sejinkim/post/f8314f20-4823-49b4-b8ae-b1ccce0c9c5c/image.png)

구체적으로는 위와 같이 측정됩니다. 메인 스레드에서 5개의 작업이 실행되고 있고, 이 중 50ms를 초과하는 세 작업들이 `Long Task`이며, 각각 50ms를 초과하여 작업이 차단된 시간을 모두 합산한 결과, 즉 **345ms**가 `TBT`가 되는 것입니다.

이러한 `TBT` 같은 상호작용 관련 메트릭은 로딩 관련 메트릭들에 비해 자바스크립트와 특히 깊은 상관 관계가 있습니다. 페이지 요소들은 이제 거의 다 눈에 보이는 시점이기는 한데, 무언가 너무 많고 비대한 코드로 인해 빠릿하게 동작은 하지 않는 문제를 파악할 수 있습니다.

디바이스 성능 - 컴퓨팅 파워에 따라 측정값의 격차가 크기 때문에, 측정시 시뮬레이션할 성능에 대해 명확한 기준점을 마련하고 적절한 통제가 이루어져야 하는 부분이기도 합니다. Google에서는 평균적인(mid-tier) 모바일 디바이스에서 테스트했을 때 **300ms** 미만 수준이 될 수 있어야 한다고 가이드하고 있습니다.

> - [제 3자(Third-Party) 스크립트 코드의 영향 줄이기](https://web.dev/third-party-summary/)
> - [JavaScript 실행 시간 단축](https://web.dev/bootup-time/)
> - [메인 스레드 작업 최소화](https://web.dev/mainthread-work-breakdown/)
> - [리소스 요청 수를 최소화하고 전송 크기를 작게 하기](https://web.dev/resource-summary/)

#### Time To Interactive, TTI

페이지가 **완전히** 상호작용이 가능하게 되기까지 소요된 시간을 측정한 것으로, `TBT`와 연관지어 보아야 하는 메트릭입니다. 마지막 `Long Task`가 완료된 이후, **5초** 동안 네트워크 및 메인 스레드가 유휴(idle) 상태에 진입한 시점을 체크하는 식으로 측정됩니다. 완전한 상호작용이 가능한 시점이란 아래를 의미합니다.

- 페이지에 `FCP`로 측정되는 콘텐츠가 표시됨
- 가장 많이 노출되는 요소에 이벤트 핸들러가 등록됨
- 페이지가 50ms 내에 사용자의 상호작용에 대해 응답함

일반적으로 **3.8초 이내**를 빠른 것으로 보며, `TBT`에서 설명한 것처럼 자바스크립트를 최대한 경량화하는 것이 `TTI`를 최적화할 수 있는 방법입니다. 모던 프론트엔드 환경에서 적극적으로 자바스크립트 코드를 분할(Splitting)하고, 불필요한 코드는 제거하기 위해 트리 쉐이킹(Tree Shaking)하는 행위 등이 적절한 사례가 될 수 있을 것입니다.

#### First Input Delay, FID

버튼을 클릭하는 등 사용자가 처음으로 사이트의 특정 요소와 상호작용 할 때, 브라우저가 해당 상호작용에 대한 응답으로 이벤트 핸들러를 실행하기 시작하는 순간까지의 시간을 나타냅니다.

위에서 언급한 것처럼, 브라우저가 즉시 응답할 수 없는 것은 메인 스레드가 다른 작업을 처리하고 있어 차단이 발생하기 때문입니다. 사용자 경험 측면에서 매우 민감하게 작용하는 부분이기 때문에, **100ms** 이하여야 우수하다고 할 수 있습니다.

텍스트 필드, 체크박스, 라디오 버튼과 같은 `<input>`, `<textarea>` 요소, 드롭다운과 같은 `<select>` 요소, 앵커 `<a>` 요소 역시 상호작용이 가능하려면 메인 스레드가 idle 상태여야 하기 때문에, 설령 이벤트 리스너를 명시적으로 추가하지 않았다고 해도 이런 요소를 기준으로 `FID`를 측정하게 됩니다.

`scroll`, `zoom` 같은 상호작용은 예외적으로 별도의 스레드에서 실행되기 때문에 `FID` 측정에는 포함되지 않고, `click`, `touch`, `key` 같은 '입력' 이벤트를 기준으로 한다는 점도 특기할 만한 점입니다.

개인적인 경험으로는, 서비스 기획/운영자들이 성과 및 사용자 행동 측정을 위해 온갖 솔루션을 추가해달라고 요청한 탓에, 외부(Third-Party) 스크립트가 너무 많아져 페이지가 눈에 띄게 버벅이고 둔해지는 문제를 체감한 적이 있었습니다. 이렇게 비즈니스적 요구와 상충하는 문제는 최적화하기 난감한 부분으로 작용하기도 합니다.

### 3. 시각적 안정성 (Visual Stability)

#### Cumulative Layout Shift, CLS

![img](https://velog.velcdn.com/images/sejinkim/post/48b07c94-beb5-43e0-9ea5-b0a9cef56e4c/image.png)
![img](https://velog.velcdn.com/images/sejinkim/post/7897130a-e798-4712-93c1-7e85fce4131a/image.gif)

사용자가 **예상하지 못한** 레이아웃의 이동이 발생했을 때, 이동 전/후 렌더링된 각각의 두 프레임 사이에서 뷰포트의 크기와 뷰포트 내에서 이동한 요소의 이동 거리 및 크기의 비율을 계산하여 수치화한 것입니다.

무언가 비동기식으로 로드되어 동적으로 DOM 요소가 기존 콘텐츠 위에 추가되면서 발생하는 것이며, 주로 이미지, 동영상, 폰트, 광고 등으로 인한 경우가 많습니다. 위 이미지에서처럼, 사용자에게 굉장한 불쾌감이나 피해를 유발할 수 있는 부분이기 때문에 사용자 경험에 있어 핵심적인 메트릭으로 작용합니다.

`CLS` 수치는 **0.1 이하**를 우수하다고 보는데, 이를 산출하는 산식은 아래에서 이어서 설명하겠습니다.

![img](https://velog.velcdn.com/images/sejinkim/post/68bbb5bd-b416-4a8d-9b4b-ac38b6400f37/image.avif)

뷰포트의 50%를 차지하는 요소가 있고, 다음 프레임에서 뷰포트 높이의 25%만큼 이동했다고 한다면, 이 경우 요소의 가시 영역은 75%(위 이미지에서 붉은 점선 사각형으로 표시된 부분)가 됩니다. 이전 프레임과 현재 프레임에서 '불안정함'이 발생한 영역의 합집합으로, 이를 `영향분율(impact fraction)`이라고 합니다.

![img](https://velog.velcdn.com/images/sejinkim/post/72289696-e9ba-4fe3-aaa4-acbde80fe4df/image.avif)

뷰포트를 기준으로, 요소가 이동한 거리는 뷰포트의 25% 만큼입니다. 수평 또는 수직으로 이동한 최대 거리를 뷰포트 너비/높이 중 큰 것으로 나눈 것을 `거리분율(distance fraction)`이라고 합니다.

`CLS`는 영향분율과 거리분율을 곱한 수치입니다. 위의 경우라면 `0.75 * 0.25 = 0.1875`가 됩니다. 즉, 요소의 크기 또는 이동 거리가 클 수록 `CLS` 수치가 높다는 것이고, 이는 그만큼 시각적 안정성을 해친 것이라고 볼 수 있습니다.

레이아웃의 이동으로 노드의 위치가 다시 계산되고 배치된다는 것은 곧 `reflow`를 의미하는 것이기도 하므로, 렌더링 퍼포먼스의 측면에서도 좋지 않다고도 할 수 있을 것입니다.

![img](https://velog.velcdn.com/images/sejinkim/post/d006f95e-12ae-43c2-9876-323483d0bbfe/image.webp)

완성된 페이지를 렌더링하는 `SSR`에서 우위를 점하기 쉬운 부분이기도 하며, 무언가 동적으로 렌더링해야 할 경우 `Skeleton/Placeholder UI`를 활용하여 렌더링될 요소에 대한 공간을 미리 확보하는 테크닉으로 `CLS`를 적극적으로 방어해야 합니다.

그리고, `CLS`는 어디까지나 사용자가 '예상하지 못한' 레이아웃 이동에서만 해당하는 개념이기도 합니다. 레이아웃 이동 자체가 죄악시되는 건 아니며, 명확히 사용자의 상호작용에 의해 발생하였고, 요청에 대한 응답이 완료되기까지 기다리는 동안 무언가 로딩되고 있다는 사실을 인지할 수만 있다면 `CLS`에 해당하지 않습니다.

예로 사용자 입력 이후 **500ms** 이내에 발생한 레이아웃 이동이라면 `CLS`로 측정되지 않습니다. 다만 이때의 '사용자 입력'이란 scroll, zoom, drag, pinch 등과 같이 연속적인 상호작용은 해당하지 않는다는 점에 주의합니다.

`CLS`를 개선할 수 있는 방법은 아래와 같습니다.

> - 이미지, 비디오 요소에 항상 크기(width/height) 또는 [종횡비(aspect-ratio)](https://css-tricks.com/aspect-ratio-boxes/) 속성을 명시하여 미리 필요한 공간을 확보하기
> - 사용자의 상호작용에 대한 응답이 아니라면, 기존 콘텐츠 위에 동적으로 콘텐츠를 삽입하지 않기
> - 레이아웃 이동을 유발하는 애니메이션보다 `transform`을 속성을 사용한 애니메이션을 사용하기

------

## 'Core' Web Vitals

![img](https://velog.velcdn.com/images/sejinkim/post/671b0b63-a2ce-4164-9f37-ab78f1b26c46/image.png)

지금까지 설명한 메트릭들 중에서도, 사용자 경험을 측정하는 데에 있어 특히 중요하게 작용하는 핵심 메트릭을 특별하게 구분하기도 하는데, 이것을 `Core Web Vitals`라고 합니다. 위에서 분류한 것처럼 `Loading`, `Interactive`, `Visual Stability` 측면에서 각각 하나씩 대표됩니다.

- LCP : 사용자가 인식하는 로딩 성능을 측정하며, 메인 콘텐츠가 로드되었을 가능성이 높은 시점을 나타냄
- FID : 사용자가 페이지와 처음 상호작용하려 할 때의 경험을 정량화
- CLS : 사용자가 예상하지 못한 레이아웃의 변화를 정량화하여 시각적 안정성을 측정

------

## Web Vitals 측정 도구

1. [PageSpeed Insights (PSI)](https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect)
   `Lighthouse`를 사용하여 사이트를 프로파일링해볼 수 있습니다. CPU/Memory 및 네트워크 성능을 사전에 설정된 프리셋으로 스로틀하여 통제된 환경에서 측정합니다. 성능에 중점을 두고 실험실 데이터와 실제 필드 데이터를 모두 사용하여 요약된 리포트를 제공해 줍니다.

2. [Search Console - Core Web Vitals Report](https://support.google.com/webmasters/answer/9205520)
   수집된 실제 필드 데이터를 기반으로, `Core Web Vitals`에 대한 리포트를 제공받을 수 있습니다.

3. [web-vitals library](https://github.com/GoogleChrome/web-vitals)
   실제 필드 데이터를 측정하고자 할 때 유용하게 사용될 수 있는 JS 라이브러리입니다. `Google Analytics`와도 연동이 가능합니다.

   ```javascript
   import {onLCP, onFID, onCLS} from 'web-vitals';
   
    onCLS(console.log);
    onFID(console.log);
    onLCP(console.log);
   ```

4. [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
   실험실 환경에서 `Web Vitals`를 종합적으로 측정하는 도구입니다. DevTools에서도 사용할 수 있지만, [Node CLI 또는 module](https://github.com/GoogleChrome/lighthouse)로도 가능합니다. 스로틀 프리셋을 DevTools에서는 커스터마이즈 할 수 없는 반면, CLI에서는 가능하기 때문에 환경을 정확히 통제하려면 CLI를 사용해야 합니다.

5. [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
   ![img](https://velog.velcdn.com/images/sejinkim/post/425adbf6-28cd-476a-b12d-ecd4f74357b7/image.png)
   위에서 언급한 것처럼, DevTools의 `Lighthouse` 패널에서도 간편하게 측정해볼 수 있지만 고정된 프리셋으로만 스로틀되며, 호스트 시스템의 성능에 따라서도 측정된 결과가 다르므로 정확한 데이터를 얻기 어려울 수 있습니다.

![img](https://velog.velcdn.com/images/sejinkim/post/3d791f39-41c2-4486-8013-b299d88f7955/image.png)
대신 `Performance` 패널에서는 `Experience` 섹션에서 `CLS`를 상세하게 디버깅해볼 수 있으므로 유용합니다. 정확히 어떠한 요소가 어떻게, 얼마나 이동하여 레이아웃이 변경되었는지 알 수 있습니다. 물론 `FCP`, `LCP`, `TBT` 타이밍 등도 파악할 수 있습니다.

------

## 참고 문서

> - [web.dev, Web Vitals](https://web.dev/vitals/)
> - [web.dev, Web Vitals 측정 도구](https://web.dev/vitals-tools/)
> - [Google Developers, Web Vitals 소개: 건강한 사이트를 위한 필수적인 측정항목](https://developers-kr.googleblog.com/2020/05/Introducing-Web-Vitals.html)
> - [Toast UI, 성능 최적화](https://ui.toast.com/fe-guide/ko_PERFORMANCE)



<br>

<br>

#### 참고링크: [웹 사이트 성능 측정, Web Vitals (velog.io)](https://velog.io/@sejinkim/웹-사이트-성능-측정-Web-Vitals)

<br>