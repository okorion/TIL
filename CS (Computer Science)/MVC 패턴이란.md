# MVC

**MVC** (모델-뷰-컨트롤러) 는 사용자 인터페이스, 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴입니다. 소프트웨어의 비즈니스 로직과 화면을 구분하는데 중점을 두고 있습니다. 이러한 "관심사 분리" 는 더나은 업무의 분리와 향상된 관리를 제공합니다. MVC 에 기반을 둔 몇 가지 다른 디자인 패턴으로 MVVM (모델-뷰-뷰모델), MVP (모델-뷰-프리젠터), MVW (모델-뷰-왓에버) 가 있습니다.

MVC 소프트웨어 디자인 패턴의 세 가지 부분은 다음과 같이 설명할 수 있습니다.

1. 모델: 데이터와 비즈니스 로직을 관리합니다.
2. 뷰: 레이아웃과 화면을 처리합니다.
3. 컨트롤러: 명령을 모델과 뷰 부분으로 라우팅합니다.

<br>

## [모델 뷰 컨트롤러 예시](https://developer.mozilla.org/ko/docs/Glossary/MVC#모델_뷰_컨트롤러_예시)

간단한 쇼핑 리스트 앱이 있다고 상상해봅시다. 우리가 원하는 것은 이번 주에 사야할 각 항목의 이름, 개수, 가격의 목록입니다. MVC 를 사용해 이 기능의 일부를 구현하는 방법을 아래에서 설명할 것입니다.

![Diagram to show the different parts of the mvc architecture.](https://developer.mozilla.org/en-US/docs/Glossary/MVC/model-view-controller-light-blue.png)

<br>

### [모델](https://developer.mozilla.org/ko/docs/Glossary/MVC#모델)

모델은 앱이 포함해야할 데이터가 무엇인지를 정의합니다. 데이터의 상태가 변경되면 모델을 일반적으로 뷰에게 알리며(따라서 필요한대로 화면을 변경할 수 있습니다) 가끔 컨트롤러에게 알리기도 합니다(업데이트된 뷰를 제거하기 위해 다른 로직이 필요한 경우).

다시 쇼핑 리스트 앱으로 돌아가서, 모델은 리스트 항목이 포함해야 하는 데이터 — 품목, 가격, 등. — 와 이미 존재하는 리스트 항목이 무엇인지를 지정합니다.

<br>

### [뷰](https://developer.mozilla.org/ko/docs/Glossary/MVC#뷰)

뷰는 앱의 데이터를 보여주는 방식을 정의합니다.

쇼핑 리스트 앱에서, 뷰는 항목이 사용자에게 보여지는 방식을 정의하며, 표시할 데이터를 모델로부터 받습니다.

<br>

### [컨트롤러](https://developer.mozilla.org/ko/docs/Glossary/MVC#컨트롤러)

컨트롤러는 앱의 사용자로부터의 입력에 대한 응답으로 모델 및/또는 뷰를 업데이트하는 로직을 포함합니다.

예를 들어보면, 쇼핑 리스트는 항목을 추가하거나 제거할 수 있게 해주는 입력 폼과 버튼을 갖습니다. 이러한 액션들은 모델이 업데이트되는 것이므로 입력이 컨트롤러에게 전송되고, 모델을 적당하게 처리한다음, 업데이트된 데이터를 뷰로 전송합니다.

단순히 데이터를 다른 형태로 나타내기 위해 뷰를 업데이트하고 싶을 수도 있습니다(예를 들면, 항목을 알파벳순서로 정렬한다거나, 가격이 낮은 순서 또는 높은 순서로 정렬). 이런 경우에 컨트롤러는 모델을 업데이트할 필요 없이 바로 처리할 수 있습니다.

<br>

## [웹에서의 MVC](https://developer.mozilla.org/ko/docs/Glossary/MVC#웹에서의_mvc)

웹 개발자로써, 여러분이 이 패턴을 이전에 의식적으로 사용한 적이 없더라도 아마 상당히 친숙할것입니다. 여러분의 데이터 모델은 아마 어떤 종류의 데이터베이스에 포함되어있었을 것입니다(MySQL 과 같은 전통적인 서버 사이드 데이터베이스, 또는 [IndexedDB](https://developer.mozilla.org/ko/docs/Web/API/IndexedDB_API) 같은 클라이언트 사이드 솔루션). 여러분의 앱의 제어 코드는 아마 HTML/JavaScript 로 작성되었을 것이고, 사용자 인터페이스는 HTML/CSS 등 여러분이 선호하는 것들로 작성되었을 것입니다. 이는 MVC 와 아주 유사하게 들리지만, MVC 는 이러한 컴포넌트들이 더 엄격한 패턴을 따르도록합니다.

웹의 초창기에, MVC 구조는 클라이언트가 폼이나 링크를 통해 업데이트를 요청하거나 업데이트된 뷰를 받아 다시 브라우저에 표시하기 위해 대부분 서버 사이드에서 구현되었습니다. 반면, 요즘에는, 클라이언트 사이드 데이터 저장소의 출현과 필요에 따라 페이지의 일부만 업데이트를 허용하는 XMLHttpRequest 를 포함해 더 많은 로직이 클라이언트 사이드에 추가되었습니다.

[AngularJS](http://en.wikipedia.org/wiki/AngularJS) 및 [Ember.js](http://en.wikipedia.org/wiki/Ember.js) 와 같은 웹 프레임워크들은 약간씩은 방식이 다르지만, 모두 MVC 구조를 구현합니다.

<br>

<br>

<br>

### 참고링크: [MVC - MDN Web Docs 용어 사전: 웹 용어 정의 | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Glossary/MVC#더_알아보기)

<br>

<br>

<br>



![img](https://blog.kakaocdn.net/dn/YDAei/btrjYhat7fs/q7ETFhxgEw42C4dcT1uFZK/img.png)

<br>

## **🚀**

**이번 포스팅은 개발자 면접에서 자주 나오는 질문 중의 하나인 "MVC패턴"에 대한 내용입니다.
MVC패턴의 의미와 사용해야 하는 이유, 사용 예시 등등에 대해 알아보겠습니다.**

 <br>

## **💡 MVC 패턴이란?**

MVC란 **M**odel-**V**iew-**C**ontroller의 약자로 애플리케이션을 세 가지 역할로 구분한 개발 방법론입니다. 아래의 그림처럼 사용자가 Controller를 조작하면 Controller는 Model을 통해 데이터를 가져오고 그 데이터를 바탕으로 View를 통해 시각적 표현을 제어하여 사용자에게 전달하게 됩니다.

이러한 패턴을 성공적으로 사용하면, 사용자 인터페이스로부터 비즈니스 로직을 분리하여 애플리케이션의 시작적 요소나 그 이면에서 실행되는 비즈니스 로직을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있게 됩니다.

<br>

![img](https://blog.kakaocdn.net/dn/bDpdks/btrjV9EuRJ3/egwkkBELr5i0oYOv4t9Qy1/img.png)

<br>

#### **✔️ 위의 개념을 WEB에 적용 시!**

1. **사용자가 웹사이트에 접속 (Users)**
2. **Controller는 사용자가 요청한 웹페이지를 서비스하기 위해서 모델을 호출 (Manipulates)**
3. **Model은 데이터베이스나 파일과 같은 데이터 소스를 제어한 후 그 결과를 Return**
4. **Controller는 Model이 리턴한 결과를 View에 반영 (Updates)**
5. **데이터가 반영된 View는 사용자에게 보여짐 (Sees)**

####  <br>

 <br>

## **🌈MVC패턴 방식** 

MVC 패턴에는 모델 1 방식과 모델 2 방식이 있는데

- **모델 1 방식: JSP에서 출력과 로직을 전부 처리**
- **모델 2 방식: JSP에서 출력만 처리**

로 분류할 수 있습니다.

#### **📌 Model 1**

<br>

![img](https://blog.kakaocdn.net/dn/w08Lw/btrlbKqhWKO/qUYnM7xziHIQUE28L6WBZ1/img.png)



모델 1 방식은 Controller 영역에 View 영역을 같이 구현하는 방식이며, 사용자의 요청을 JSP가 전부 처리합니다. 요청을 받은 JSP는 JavaBean Service Class를 사용하여 웹브라우저 사용자가 요청한 작업을 처리하고 그 결과를 출력합니다.

 <br>

#### **📌 Model 2**

<br>

![img](https://blog.kakaocdn.net/dn/bGZKd4/btrleqFoykC/kXkFFucLJdHJ4hNvfcmav0/img.png)



모델 2 방식은 웹브라우저 사용자의 요청을 서블릿이 받고 서블릿은 해당 요청으로 View로 보여줄 것인지 Model로 보낼 것인지를 판단하여 전송합니다. 또한 모델 2 방식의 경우 HTML 소스와 JAVA소스를 분리해놓았기 때문에 모델 1 방식에 비해 확장시키기도 쉽고 유지보수 또한 쉽습니다.

 <br>

#### **👀 Model 1 vs Model 2**

|          | **Model 1**                                                  | **Model 2**                                                  |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **장점** | **빠르고 쉽게 개발 가능**                                    | **디자이너와 개발자의 분업이 가능하며 유지보수 및 확장이 쉬움** |
| **단점** | **JSP파일이 너무 비대해지며 Controller와 View가 혼재하므로 향후 유지보수에 어려움** | **설계가 어려우며 개발 난이도가 높음**                       |

**>> Model 1 방식으로 웹서비스를 개발하는 사례는 백엔드와 프론트엔드의 역할 분담이 모호해져 협업이 쉽지 않으며 실제 서비스들 중에서 거의 없다고 봐도 무방합니다.** 

##  <br>

 <br>

## **📲 모델 (Model)**

데이터를 가진 객체를 모델이라고 지칭합니다. 데이터는 내부의 상태에 대한 정보를 가질 수도 있고, 모델을 표현하는 이름 속성으로 가질 수 있습니다. 모델의 상태에 변화가 있을 때 컨트롤러와 뷰에 이를 통보합니다. 이와 같은 통보를 통해 뷰는 최신의 결과를 보여줄 수 있고, 컨트롤러는 모델의 변화에 따른 적용 가능한 명령을 추가, 제거, 수정할 수 있습니다.

**모델의 규칙**

- 사용자가 편집하길 원하는 모든 데이터를 가지고 있어야만 함
- 뷰나 컨트롤러에 대해서 어떠한 정보도 알지 말아야 함
- 변경이 일어나면, 변경 통지에 대한 처리방법을 구현해야 함

 <br>

## **🖥️ 뷰 (View)**

View는 클라이언트 측 기술은 HTML/CSS/Javascript들을 모아둔 컨테이너입니다. 사용자가 볼 결과물을 생성하기 위해 모델로부터 정보를 얻어옵니다.

**뷰의 규칙**

- 모델이 가지고 있는 정보를 따로 저장해서는 안됨
- 모델이나 컨트롤러와 같이 다른 구성 요소를 몰라야 함
- 변경이 일어나면, 변경 통지에 대한 처리방법을 구현해야 함

 <br>

## **🕹️ 컨트롤러 (Controller)**

사용자가 접근한 URL에 따라 사용자의 요청사항을 파악한 후에 그 요청에 맞는 데이터를 Model을 의뢰하고, 데이터를 View에 반영해서 사용자에게 알려줍니다.

모델에 명령을 보냄으로써 뷰의 상태를 변경할 수 있음 => (워드에서 문서 편집)
컨트롤러가 관련된 모델에 명령을 보냄으로써 뷰의 표시 방법을 바꿀 수 있음 => (문서를 스크롤하는 것)

**컨트롤러의 규칙**

- 모델이냐 뷰에 대해서 알고 있어야 함
- 모델이나 뷰의 변경을 모니터링해야 함

 <br>

 <br>

## **👨🏻‍💻 MVC 패턴을 사용해야 하는 이유**

- **비즈니스 로직과 UI로직을 분리하여 유지보수를 독립적으로 수행가능**
- **Model과 View가 다른 컴포넌트들에 종속되지 않아 애플리케이션의 확장성, 유연성에 유리함**
- **중복 코딩의 문제점 제거**

 <br>

 <br>

## 😰 **MVC 패턴의 한계**

MVC패턴에서 View는 Controller에 연결되어 화면을 구성하는 단위 요소이므로 다수의 View를 가질 수 있습니다. 그리고 Model은 Controller를 통해서 View와 연결되지만, Controller에 의해서 하나의 View에 연결될 수 있는 Model도 여러 개가 될 수 있어 View와 Model이 서로 의존성을 띄게 됩니다. 즉, Controller에 다수의 Model과 View가 복잡하게 연결되어 있는 상황이 발생할 수 도 있습니다.

 <br>

 <br>

## **🌏 MVC 패턴의 예시**



![img](https://blog.kakaocdn.net/dn/VZu2t/btrjT0hfu2x/2SFCsQTQKvK4kYoKAlCiM1/img.png)![img](https://blog.kakaocdn.net/dn/qXrTU/btrjVB2CV3Z/GGCiG94Q8KE5uUwOlfm4E0/img.png)![img](https://blog.kakaocdn.net/dn/d5a232/btrjR625JIq/yAS9zNGahmr04DKpuIC4yk/img.png)![img](https://blog.kakaocdn.net/dn/cpk1Hp/btrjVWepndR/vVcF5cK28uiCdrAOiofjK0/img.png)

<br>

**Google의 Angular JS, PHP의 CODEIGNITER, Python의 django, Facebook의 React 등등**

 <br>

 <br>

## 📗 **MVC 패턴 요약**

**Model - 백그라운드에서 동작하는 비즈니스 로직(데이터) 처리**

**View - 정보를 화면으로 보여주는 역할.**

**Controller - 사용자의 입력 처리와 흐름 제어 담당. 화면과 Model과 View를 연결시켜주는 역할**

<br>

<br>

<br>

> 뷰(View)로 입력을 받고, 모델(Model) 처리한 뒤에 컨트롤러(Controller)가 백 통신하여 뷰로 보여주는게 아님.
> => 컨트롤러(Controller)에서 데이터를 입력 받고, 모델(Model) 처리한 뒤에, 뷰(View)로.

<br>

### 참고링크: [[개발상식\] MVC 패턴이란? (Model-View-Controller) :: 코딩 공부 일지 (tistory.com)](https://cocoon1787.tistory.com/733)

<br>