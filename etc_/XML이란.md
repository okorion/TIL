## 🌌 XML이란?

xml 파일은 간단하게 말하면 주로 웹에서 데이터를 전송하기 위해 미리 약속해둔 방식으로 만들어진 문서를 말한다. 줄임말은 eXtensible Markup Language 이며 우리말로 하자면 확장 가능한 마크업 언어 라고 볼 수 있다.



이를 이해하기 위해서는 마크업 언어라는 것에 대해서 간략하게 알아야 할 필요가 있다.



마크업 언어란? - 특정 양식이 있는 문서를 통틀어 말하는 것으로 아래 링크 참조

https://blog.naver.com/rodpold/222752172285

[![img](https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fblogimgs.pstatic.net%2Fnblog%2Fmylog%2Fpost%2Fog_default_image_160610.png%22&type=ff120)](https://blog.naver.com/rodpold/222752172285)

 

**마크업 언어란?**

개요 마크업 언어(Markup Language)는 양식이 있는 문서의 한 종류이며 그 양식을 태그(좌, 우 부등호 처...

blog.naver.com



xml 의 생김새

xml 은 기본적으로 이렇게 생겼다(w3schools 의 샘플)

<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>

첫 줄은 프롤로그라고 하며 이 문서가 xml 임을 알리고 버전이 몇인지, 그리고 문서의 인코딩이 어떻게 되는지 표시해준다. 인코딩이란 간략하게 말하면 글자를 컴퓨터에 어떤 형식으로 표현할 것인지 정해놓은 것이라 보면 된다. 관련된 내용은 추후 포스팅을 할 예정이다.



이 프롤로그는 생략이 가능하지만 정보를 제공하는 의미로써 대부분 작성해두기 때문에 적어두는 것이 좋다.





데이터를 보는 방식

위 예시의 꺽쇠 부분인 < 이 기호와 > 이 기호로 감싸져 있는 것을 태그(Tag)라고 한다. 이 태그는 HTML에서도 사용되는 것과 같은 것이다. 그렇기 때문에 이 태그는 <abc> 라는 이름으로 시작했다면 </abc>라고 종료를 알리는 태그로 감싸져 있어야 한다.



그리고 그 사이에 있는 글자나 숫자를 값(Value)이라고 한다. 실제로 데이터를 주고 받을 때 내용물이 되는 부분이다.



상당히 많은 통신들이 키와 값(Key Value Pair)으로 쌍을 이루어서 통신을 한다. 예를 들면 [생년월일:2000년 1월 1일] 같이 [생년월일]은 키가 되고 [2000년 1월 1일]은 값이 되는 것 처럼 이런 기본적인 규칙을 컴퓨터 역시 적용하여 통신을 하기 때문이다.



그런데 이 예시에 보면 <note> 라는 항목 아래에 <to> <from> 등의 키가 계층을 이루고 있다. 이런 계층을 이루는 구조로도 값을 설정할 수 있다. 예를 들어 "Jani"라는 값을 찾고 싶다면 note 아래의 from 항목에 있는 것이 된다.



이런 계층들은 보여주는 프로그램 마다 다르지만 조금 더 보기 쉽게 접어서 확인하는 기능을 제공하기도 한다. 크롬 브라우저로 xml파일을 열면 다음과 같이 생겼는데



![img](https://mblogthumb-phinf.pstatic.net/MjAyMjA1MzFfMTY5/MDAxNjUzOTY5NDE1ODg3.hzW-jlGPz_8-a6PW24D2iAc12BRiJmieMbrSkXbsmm4g.x8a97Xb0GMv4egwvVZ8z2HwvZppp5T8a7cCjRBnx1c0g.PNG.rodpold/image.png?type=w800)

크롬 브라우저로 xml 파일을 열어본 모습

왼쪽 위 <note> 옆의 화살표를 눌러 접으면 이렇게 된다.



![img](https://mblogthumb-phinf.pstatic.net/MjAyMjA1MzFfMzYg/MDAxNjUzOTY5NDU4NjEy.rlFmHvB1tzJZuwhRNoDVHwbV5SnE1AfWBjISVIrRJj0g.2NvdwfsJXPtjGrfEjPbnmlBKDsUG0IT1cf-mbEjF4Xgg.PNG.rodpold/image.png?type=w800)

화살표를 눌러 접음



구조가 훨씬 복잡한 xml 문서는 이런 형식으로 접어가며 값을 확인하는 것이 조금 더 도움이 된다.





규칙

xml 의 규칙의 세부 사항은 하단의 참고 링크를 눌러 더 자세하게 볼 수 있다.



여기서는 기본적인 몇 가지의 규칙만 정리해서 적어보고자 한다.



**가장 먼저 xml 은 하나의 가장 큰 루트 엘리먼트(root element)로 되어 있어야 한다.** 

이게 무슨 뜻이냐면 위의 샘플에서 가장 상위의 <note> 단 하나의 시작점이 있다고 생각하면 된다. 예를 들어 <note></note>하나를 만든 후 그 아래에 <note2></note2> 처럼 둘로 나뉘면 안 된다는 뜻이다. 이렇게라도 하고 싶다면 note와 note2 를 상위에 또 하나의 다른 이름으로 묶으면 된다.



**태그를 열었다면 반드시 닫아야 한다.** 

<naver> 라는 이름으로 태그를 열었다면 반드시 </naver> 로 태그를 닫아야 한다. 또는 이런 형태로 한 줄로 만들어서 태그를 열어둠과 동시에 닫는 태그를 만들 수도 있다. <naver /> (닫는 태그 왼편에 / 슬래쉬가 있다)

이 때 첫 줄의 프롤로그는 태그가 아니므로 닫는 태그가 필요 없다.



**태그는 대소문자를 구분한다.**

<Naver> 와 <naver>는 다른 태그이다. 컴퓨터는 대소문자를 다른 문자로 구분하여 이를 다른 것으로 인식한다. 어떤 마크업 문서나 다른 시스템에서는 대소문자를 구분하지 않는 것도 있기 때문에 각 규칙마다 대소문자를 구분하는지 안하는지 확인해 두는 것은 중요하다.



**띄어쓰기를 생략하지 않는다.**

HTML의 경우에 Im    fine     thank      you  라는 문장을 의도적으로 공백 을 포함하여 적으면 Im fine thank you 라고 한 개의 공백만 남겨둔 채 나머지는 생략한다. 그러나 XML은 이를 생략하지 않고 공백의 개수 그대로 값을 유지한다.



**여는 태그와 닫는 태그가 엉켜있으면 안 된다.**

예를 들어 <abc><def></abc></def> 처럼 <def>로 열린 태그가 먼저 열린 </abc>로 닫혀서는 안 된다. XML에서는 이러한 경우에 오류가 나며 이 경우엔 반드시 <abc><def></def></abc> 처럼 가장 마지막에 열린 태그가 먼저 닫혀야 한다.



사용되고 있는 곳

XML이 사용되고 있는 곳은 매우 다양하다. 게임의 세이브 데이터에도 사용할 수 있고, 문서의 저장 데이터를 XML로 할 수도 있다. 또, 다른 서비스간의 웹 상에서 통신을 위해 사용되는 경우도 많다.



예를 들면 A회사에서 B회사에게 정보를 전달하고 싶을 때 A회사의 홈페이지에 <hello>world</hello> 라는 xml 문서가 담긴 주소를 넘겨준다. 그럼 B회사는 이 주소에 방문해서 XML문서를 읽고 필요한 정보(여기서는 world)를 가져올 수 있게 되는 것이다.



그럼 그럴 필요 없이 A회사와 B회사가 서로 새로운 약속을 하고 hello|world 라는걸 만들어서 넘겨줄 수도 있지 않을까?



물론 가능하다. 그렇지만 우리가 이런 약속 문서를 사용하는 이유는 다른 수 많은 회사들과 각기 다른 약속을 할 수 없기 때문이다. 그러면 그 때 그때 그 회사에 맞는 프로그램을 짜야 하기 때문이다. 굉장히 심한 낭비가 아닐 수 없다.



이런 XML은 수많은 사람들이 이렇게 쓰기로 약속을 한 문서고 그렇기에 XML문서를 컴퓨터가 해독하기 편하게끔 미리 만들어진 프로그램들도 상당수 존재한다. 이런 편의성 혜택을 받을 수 있기에 다양한 약속된 문서를 통신에 사용하는 것이다.



참고:

https://www.w3schools.com/xml/xml_syntax.asp

[![img](https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fwww.w3schools.com%2Fimages%2Fw3schools_logo_436_2.png%22&type=ff120)](https://www.w3schools.com/xml/xml_syntax.asp)



<br>

<br>

#### 참고링크: [xml 파일이란? : 네이버 블로그 (naver.com)](https://m.blog.naver.com/rodpold/222753497408)

<br>