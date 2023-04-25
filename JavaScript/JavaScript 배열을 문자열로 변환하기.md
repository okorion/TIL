# 📮 JavaScript 배열을 문자열로 변환하기

## **1. join() 함수 사용하기**

> arr.join(separator)

join() 함수는 배열의 모든 값들을 연결한 문자열을 리턴합니다.

이때 각각의 값들 사이에는 파라미터로 입력된 구분자(separator)가 들어가게 됩니다.

만약, separator를 입력하지 않은 경우, default로 ','가 들어갑니다.

 <br>

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="328" width="100%" name="cp_embed_1" scrolling="no" src="https://codepen.io/hianna/embed/GRjgdYm?height=328&amp;theme-id=dark&amp;default-tab=js%2Cresult&amp;user=hianna&amp;slug-hash=GRjgdYm&amp;name=cp_embed_1" title="CodePen Embed" loading="lazy" id="cp_embed_GRjgdYm" style="max-width: 100%; width: 800px; overflow: hidden; display: block;"></iframe>

 <br>

***const str1 = arr.join();***

파라미터로 값이 아무것도 전달되지 않으면,

배열의 각 값들은 ','를 구분자로 하여 연결됩니다.

 <br>

***const str2 = arr.join('-');***

파라미터로 '-'가 전달되었기 때문에, 

'-'로 연결된 문자열이 리턴되었습니다.

 <br>

***const str3 = arr.join('');***

파라미터로 비어있는 문자열이 전달되었고,

배열의 각 값들을 구분자 없이 연결한 문자열이 리턴되었습니다.

 <br>

 <br>

 

## **2. toString() 함수 사용하기**

배열의 toString() 함수는 배열을 표현하는 문자열을 리턴합니다.

 

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="265" width="100%" name="cp_embed_2" scrolling="no" src="https://codepen.io/hianna/embed/zYKxjyg?height=265&amp;theme-id=dark&amp;default-tab=js%2Cresult&amp;user=hianna&amp;slug-hash=zYKxjyg&amp;name=cp_embed_2" title="CodePen Embed" loading="lazy" id="cp_embed_zYKxjyg" style="max-width: 100%; width: 800px; overflow: hidden; display: block;"></iframe>

 <br>

***arr.toString()***

배열의 toString() 함수는 배열의 값들을 ','로 연결한 문자열을 리턴합니다.

 <br>

***arr***

배열을 출력할 경우 자동으로 toString() 함수가 불려지고,

toString()을 호출했을 때와 같은 결과가 출력됩니다.

<br>

<br>

#### 참고링크: [[Javascript\] 배열을 문자열로 변환하기 - 어제 오늘 내일 (tistory.com)](https://hianna.tistory.com/447)

<br>