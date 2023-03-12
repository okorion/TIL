css를 통해 animation을 사용하거나 마우스오버 혹은 특정 버튼을 클릭했을 때 클래스 추가하여 transform을 조정하게 될 경우 영역이 깜빡이거나 잠시 흐려지는 현상을 경험한 적이 있을 것이다.

 

### 1. CSS핵 (translateZ or translate3d) 사용

위와 같은 부자연스러운 transform, animation 현상이 발생하는 것을 해결하기 위해 '*****하드웨어 가속'을 활성화해 대상이 되는 엘리먼트를 빠르게 렌더링 처리하는 방법을 사용했다.

> *하드웨어 가속
> \- 하드웨어 가속은 중앙처리장치(CPU)가 하는 일을 그래픽 처리 장치(GPU)가 분담하여 처리해서 컴퓨터의 성능을 최대한으로 끌어올리고 브라우저 렌더링을 보다 빠르게 할 수 있게 만든다.

 

일반적인 css animation, transform, transition 속성에는 하드웨어 가속이 적용되지 않기 때문에 브라우저를 속여서 강제로 3D 처리를 하도록 브라우저에 지시해 하드웨어를 가속화 하는 방법을 사용했다.

그 방법이 translateZ 혹은 translate3d이다.

```
transform: translate3d(0,0,0);

transform: translateZ(0)
```

하지만 이러한 방법은 RAM이나 그래픽 처리 장치(GPU)의 사용량을 커지게하여 페이지에 병목 현상을 줘서 오히려 악영향을 끼치게 한다.

 

### 2. will-change

위 css핵을 대체할 수 있는 새로운 css 속성이 생겼다. 그 속성이 will-change 이다.

속성명 그대로 어떤 속성이 변경이 될 것인지 미리 엘리먼트에 적용하여 브라우저가 해당 css를 읽을 때 변경 될 속성을 알게하여 미리 그 변경에 대비할 수 있게 하는 것이다.

```
will-change: auto;		/* 기본 값 */
will-change: scroll-position;	/* 스크롤 위치가 변경 될 예정 */
will-change: contents;		/* 요소의 컨텐츠 내용이 변경 될 예정 */

/* 특정 css 속성 적용 */
will-change: transform;		/* transform 속성이 변경 될 예정 */
will-change: opacity;		/* opacity 속성이 변경 될 예정 */
will-change: left, top;		/* left, top 값이 변경 될 예정 */
will-change: transform, opacity
```

 

 

적용예시)

```
<style>
  .thmb {width:100px; height:100px; border-radius:50%; overflow:hidden;}
  .thmb img {transition:0.3s transform; will-change:transform;}
  .thmb:hover img {transform:scale(1.2);}
</style>

<!-- .thmb 마우스오버시 img 확대 -->
<div class="item">
  <div class="thmb">
    <img src="picture.jpg">
  </div>
</div>
```

위와 같은 소스상 .thmb에 마우스 오버시 img가 확대되는 효과를 구현하고자 할 때

transform을 통해 scale을 변경할 img태그에 미리 will-change 속성을 적용해줄 수 있다.

 

### 3. will-change 사용상의 주의사항

브라우저 성능을 최적화 하겠다고 will-change를 과다하게 사용하면 안된다.

브라우저는 기본적으로 브라우저가 사용할 수 있는 최적화를 최대한으로 적용한다.

그리고 브라우저가 적용한 최적화를 삭제하고 가능한한 빨리 브라우저가 처리해야할 다른 작업들을 실행한다.

그런데 will-change를 선언하게 되면 이러한 브라우저의 특성을 무시하고 브라우저가 최적화에 더 많은 시간을 쏟게 한다.

즉, 오히려 브라우저 최적화에 악영향을 끼친다.

 

그렇기 때문에 will-change는 **정말 필요한 경우에만 적절하게** 사용해야한다.

 

### 4. 자바스크립트를 이용한 will-change 적용

3번과 같은 브라우저 최적화 이슈가 있기 때문에 가능하면 will-change를 사용할 때는 자바스크립트를 사용해서 필요한 순간에만 적용하고 다시 will-change를 초기화 시키는 방법을 적용할 수 있다.

```
<!-- .thmb 마우스오버시 img 확대 -->
<div class="item">
  <div class="thmb">
    <img src="picture.jpg">
  </div>
</div>

<script>
  // 클릭할 때 애니메이션을 재생할 엘리먼트를 선택합니다.
  var item = document.querySelector('.item');

  // 엘리먼트의 조상 요소에 마우스 커서가 올라가면 will-change를 설정한다.
  item.addEventListener('mouseenter', hintBrowser);
  // 엘리먼트의 조상 요소에 마우스 커서가 내려가면 will-change를 초기화한다.
  item.addEventListener('mouseleave', removeHint);

  function hintBrowser() {
    this.querySelector('img').style.willChange = 'transform, opacity';
  }

  function removeHint() {
    this.querySelector('img').style.willChange = 'auto';
  }
 </script>
```

 

참고링크: [[css 속성\] will-change (애니메이션 성능 향상) :: About Web (tistory.com)](https://abcdqbbq.tistory.com/103)



---



목차

- will-change 속성이란?
  - [사용법](https://coding-farmer.tistory.com/7#사용법)
  - [언제 사용해야 할까?](https://coding-farmer.tistory.com/7#언제_사용해야_할까?)
  - [주의할 점](https://coding-farmer.tistory.com/7#주의할_점)

## will-change 속성이란?

**will-change css 속성은 요소의 변화를 미리 브라우저에게 알려주어 브라우저가 미리 최적화를 하게 할 수 있는 속성입니다.**

### 사용법

```css
will-change: auto; // 기본 값
will-change: scroll-position; // 요소의 스크롤의 위치가 변한다는것을 미리 알림
will-change: contents; // 요소의 내용이 바뀐다는 것을 미리 알림
will-change: transform; // 이렇게 CSS 속성을 직접 명시할 수 있습니다.
will-change: opacity;

/* 이렇게 적게되면 어느 부분에 적용될까요?*/
will-change: background;

/* 속기로 적게된 속성은 아래와 같이 모든 것에 적용하는 것과 동일합니다.*/
will-change: background-image;
will-change: background-position;
will-change: background-size; 등등등
```

### 언제 사용해야 할까?

이 속성은 언제사용하면 좋을까요? 

우리는 웹사이트 개발을 하다보면 JavaScript를 이용하여 CSS를 제어하는 상황이 생길 수 있습니다.

한 두번이야 괜찮지만 같은 엘리먼트를 계속해서 변형시키는 작업이면 어떨까요?? 브라우저가 CSS의 변형에 따라 계산을 해서 화면에 렌더링을 하는데 시간이 오래 걸릴 것입니다.

 

예를 들어, scroll에 따라 element의 transform: translateX 속성을 변경하는 일이 있을 수 있습니다.

그러면 사용자가 스크롤을 할 때마다 그 값에 따라서 css가 계속해서 바뀔 것입니다. 이런 경우 브라우저는 계속해서 바뀌는 translateX 값에 따라 계속해서 요소를 계산해서 렌더링을 할 것입니다. 이런 경우에 will-change를 사용하면 조금이나마 최적화에 도움이 될 것입니다.

 

한번 예시를 들어보겠습니다.

 

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="300" width="100%" name="cp_embed_1" scrolling="no" src="https://codepen.io/dnjs2618/embed/YzQxJjP?height=300&amp;default-tab=html%2Cresult&amp;slug-hash=YzQxJjP&amp;user=dnjs2618&amp;ke-size=size16&amp;name=cp_embed_1" title="CodePen Embed" loading="lazy" id="cp_embed_YzQxJjP" style="max-width: 100%; width: 860px; overflow: hidden; display: block;"></iframe>

 

 

 

위의 경우에는 will-change를 쓰면 브라우저가 최적화하기에 좋아보입니다. 

 

그러면 will-change가 브라우저에게 미리 변화를 알려주어 최적화를 진행할 수 있다면 그냥 전역 상태에 모든 변화를 걸어버리는게 좋을까요? 아래와 같이요.

```css
* {
 	will-change: oacity, left, top, transform;
}
```

이렇게하면 브라우저는 최적화하기 위해서 많은 시간을 들이기 때문에 최적화가 되기보다 되려 페이지의 속도가 저하될 수 있습니다. 그러면 이것을 방지하기 위해서 어떻게 작성하면 좋을까요?

 

**특정 엘리먼트에만 넣는방법**

```css
/*위에 보여드린 예시에서 특정 부분입니다.*/
.slide-wrapper {
	will-change: transform;
    /* 이런식으로 사용자에게 빠르게 반응해야 하는 페이지의 소수의
    지속적 UI 요소에 대해 will-change를 지정하는 것은 적절합니다.*/
}
```

**변화가 일어날 것 같을 때만 미리 will-change 넣고 auto로 되돌리기**

```javascript
// 아래는 MDN에 나와있는 예제입니다.
var el = document.getElementById('element');

// Set will-change when the element is hovered
el.addEventListener('mouseenter', hintBrowser);
el.addEventListener('animationEnd', removeHint);

function hintBrowser() {
  // The optimizable properties that are going to change
  // in the animation's keyframes block
  this.style.willChange = 'transform, opacity';
}

function removeHint() {
  this.style.willChange = 'auto';
}
```

 

이제 아래에서는 주의할 점에 대해서 알아볼 것입니다.

### 주의할 점

will-change가 마냥 좋지만은 않습니다.

MDN 문서에 보면 will-change로 인한 최적화는 성능 비용이 커서 요구 되기 전에 미리 실행시켜서 페이지의 반응성이 증가될 수 있다고 하면서 5가지의 조언이 남겨져있습니다.

우선 간단하게 살펴보고 아래에서 자세하게 설명하겠습니다.

 

1. **너무 많은 요소에 will-change를 적용하지 마라.**
2. **아껴서 사용하라.**
3. **최적화하기 위해 서둘러 will-change를 적용하지 마라.**
4. **브라우저가 작업할 시간을 충분히 줘라.
   **
5. **will-change 속성은 스택 Context가 미리 생기기 때문에 요소의 시각적인 모양에 영향을 미칠 수 있다.**

------

**1. 너무 많은 요소에 will-change를 적용하지 마라.**

**->** 이미 브라우저는 최적화를 하기 위해 모든 것을 시도하고 있는데 거기에서 will-change와 같이 강한 최적화는 기기 자원을 많이 소모할 것이며 과도한 사용은 페이지 속도를 느리게 하거나 엄청난 자원을 소비할 수 있다.

 

**2. 아껴서 사용하라.**

**->** 브라우저가 만드는 최적화의 기본 행동은 가능한 바로 최적화를 제거하고 기본 상태로 돌리는 것이다. 그러나 will-change를 스타일시트에 직접 추가하는 것은 목표요소가 곧 변경되어 더 오랫동안 최적화를 유지하라는 것이기에 기본상태로 돌리기 까지 시간이 걸린다.

 

**3. 최적화 하기위해 서둘러 will-change를 적용하지 마라.**

**->** will-change는 당장의 성능문제를 해결하기 위해 마지막 수단으로 이용하려고 만든 것이다. 성능 문제를 예상해서 굳이 잘 작동중인 웹사이트에 적용할 필요는 없다. 너무 많은 사용은 브라우저가 가능한 변화를 미리 다 준비하려고 하기 때문에 과도한 메모리 사용과 복잡한 렌더링으로 열악한 성능을 이끌 것이다.

 

**4. 브라우저가 작업할 시간을 충분히 줘라**

**->** user-agent(브라우저)가 변경가능한 속성을 미리 알 수 있게 하도록 고안된 속성이기에 브라우저는 실제 속성변화가 발생하기 전에 속성에 요구되는 최적화를 미리 적용하는 것을 선택할 수 있다. 브라우저가 실제 최적화를 할 수 있는 시간을 주는 것이 중요하다! 변화가 발생하기 전에라도 그 변화를 예상할 방법을 찾아 will-change를 설정하라.

 

만약에 hover시에 opacity가 바뀔 때 제가 will-change를 걸고 싶어졌다고 치고 코드를 작성하겠습니다.

```css
.element { 
	transition: opacity .2s linear; opacity: 1;
}
.container:hover > .element {
	will-change: opacity;
}

.element:hover {
	opacity: .3;
}
/* 이 경우에는 will-change 효과가 전혀 없습니다.  
아래에 속성이 변경되기 직전에 will-change 요소를 넣었기 때문에(container hover 시에 will-change)
will-change 최적화를 하기 위한 시간이 충분하지 않습니다.
그래서 무언가가 바뀔것이라고 미리 예측하는 방법을 찾아서 설정하는 것이 좋습니다.
*/
```

 

 

**5. will-change 속성은 스택 Context가 미리 생기기 때문에 요소의 시각적인 모양에 영향을 미칠 수 있다.**

**->** 브라우저에서 opacity 값이 1인 경우에는 스택 Context에 값이 생기지 않습니다. 그러나 opacity가 1이 아닐 경우에는

stack Context가 생깁니다. 그런데 will-change: opacity를 주게 되면 opacity가 1이어도 stack Context가 생성됩니다.

 

 

will-change는 정말 필요할 때가 아니면 가급적이면 사용을 안하는 것이 좋겠습니다. 그러나 위에서 보여드린 예시와 같이 저런 슬라이드를 구현하게 된다면 한번 쯤 사용해보시면 좋을 것 같습니다. 주의사항을 잘 읽어보시고 해당하지 않는다면 사용하시면 될것같아요.

 

긴 글 읽어주셔서 감사합니다.

공유하기

게시글 관리

*구독하기*



참고링크: [will-change를 이용하여 웹사이트 성능 향상 시키기 (CSS) (tistory.com)](https://coding-farmer.tistory.com/7)