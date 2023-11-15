## 🔁 onbeforeunload란?

만약 사용자가 페이지에서 몇백자의 장문을 쓰다가 실수로 나가거나 모르고 새로고침을 한다면 어떻게 해야할까?

![img](https://postfiles.pstatic.net/20160716_259/rwans0397_1468680557397CRKTX_PNG/%C0%DA%B9%D9%BD%BA%C5%A9%B8%B3%C6%AE_%B3%AA%B0%A1%B0%C5%B3%AA_%BB%F5%B7%CE%B0%ED%C4%A7%BD%C3_%C0%CC%BA%A5%C6%AE.PNG?type=w966)

네이버 블로그 글을 쓰다가 닫기 버튼을 누를때 발생하는 이벤트

이러한 문제를 방지하기위해서는 window.onbeforeunload 윈도우 이벤트를 사용하면 된다. 

![img](https://postfiles.pstatic.net/20160717_179/rwans0397_1468681317062WnDFA_PNG/%C0%DA%B9%D9%BD%BA%C5%A9%B8%B3%C6%AE_%B3%AA%B0%A1%B0%C5%B3%AA_%BB%F5%B7%CE%B0%ED%C4%A7%BD%C3_%C0%CC%BA%A5%C6%AE2.PNG?type=w966)

페이지 새로고침시

![img](https://postfiles.pstatic.net/20160717_130/rwans0397_1468681364171V83av_PNG/%C0%DA%B9%D9%BD%BA%C5%A9%B8%B3%C6%AE_%B3%AA%B0%A1%B0%C5%B3%AA_%BB%F5%B7%CE%B0%ED%C4%A7%BD%C3_%C0%CC%BA%A5%C6%AE3.PNG?type=w966)

페이지를 나갈때

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
    <script type="text/javascript">
    window.onbeforeunload = function() {};
    </script>

  </head>
  <body>
    <h1>글작성하기</h1>
​    <input type="text" name="name" value="">
  </body>
</html>

window.onbeforeunload = function() {};
위에 코드만 선언해도 나가거나 새로고침시 이벤트가 발생한다.

**[출처]** [자바스크립트 이벤트 onbeforeunload 페이지를 나가거나 새로고침시 발생하는 이벤트](https://blog.naver.com/rwans0397/220764024791)|**작성자** [eggs30](https://blog.naver.com/rwans0397)



<br>

<br>

### 참고링크: [자바스크립트 이벤트 onbeforeunload.. : 네이버블로그 (naver.com)](https://blog.naver.com/rwans0397/220764024791)

<br>