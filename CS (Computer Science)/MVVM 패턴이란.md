# 🐧 MVVM 패턴이란

**일반적인 MVVM 패턴**![img](https://blog.kakaocdn.net/dn/b5ZE36/btq2lqcQohU/ekNc9XgOcJcyqfEtMbltTk/img.png)

<br>

MVVM 패턴은 MVC 패턴에서 Controller를 빼고 ViewModel을 추가한 패턴입니다.

 <br>

**역할 및 동작 원리**

- View
  - iOS는 ViewController까지 View가 됩니다
  - 사용자가 보여지는 View를 생각하면 된다. 유저 인터랙션을 받는 역할, 인터랙션을 받을 시 ViewModel에게 명령을 내립니다.
- ViewModel
  - View를 표현하기 위해 만들어진 View를 위한 Model
  - View와는 Binding을 하여 연결후 View에게서 액션을 받고 또한 View를 업데이트합니다
  - ex) textView에 보여줄 내용을 담당하는 함수 등, View에서 변화가 일어나는 ViewController의 역할을 담당
- Model
  - 데이터, 비즈니스 로직, 서비스 클라이언트 등으로 구성
  - 실제적 데이터

 <br>

1. View에 입력이 들어오면 ViewModel에게 명령을 합니다
2. ViewModel은 필요한 데이터를 Model에게 요청합니다
3. Model은 ViewModel에게 요청된 데이터를 응답합니다
4. ViewModel은 응답 받은 데이터를 가공해서 저장합니다
5. View는 ViewModel과의 Data Binding으로 인해 자동으로 갱신됩니다

 <br>

 <br>

**MVVM 패턴의 장단점**

- 장점
  - View와 Model이 서로 전혀 알지 못하기에 독립성을 유지할 수 있습니다
  - 독립성을 유지하기 때문에 효율적인 유닛테스트가 가능합니다
  - View와 ViewModel을 바인딩하기 때문에 코드의 양이 줄어듭니다
  - View와 ViewModel의 관계는 N:1 관계입니다
  - 유닛테스트를 하기가 좋습니다. 그 이유는 ViewModel에는 UIKit 관련 코드가 없고 Controller와의 의존성도 없기 때문입니다
- 단점
  - 간단한 UI에서 오히려 ViewModel을 설계하는 어려움이 있을 수 있습니다
  - 데이터 바인딩이 필수적으로 요구됩니다
  - 복잡해질수록 Controller처럼 ViewModel이 빠르게 비대해집니다
  - 표준화된 틀이 존재하지 않아 사람마다 이해가 다릅니다

 <br>

 <br>

**Data Binding**

데이터 바인딩의 개념은 쉽게 말해 Model과 UI 요소 간의 싱크를 맞춰주는 것이라 할 수 있습니다.

이 패턴을 통해 View와 로직이 분리되어 있어도 한 쪽이 바뀌면 다른 쪽도 업데이트가 이루어져 데이터의 일관성을 유지할 수 있습니다.

iOS에서 데이터 바인딩을 하는 방법은 다음과 같습니다.

- KVO
- Delegation
- Functional Reactive Programming
- Property Observer

<br>

<br>

#### 참고링크: [MVVM 패턴 (tistory.com)](https://jhtop0419.tistory.com/21)

<br>

<br>

<br>

<br>

# MVVM 패턴이란? (개념 / 특징 / 장점)

 <br>

### **서론**

이번에는 마틴 파울러의 프레젠테이션 모델 디자인 패턴의 변형인 MVVM패턴에 대해 정리해보려한다. 바로 알아보도록 하자.

 <br>

------



![[Vue] MVVM 패턴이란? (개념 / 특징 / 장점) - undefined - 서론](https://blog.kakaocdn.net/dn/bS489b/btrzEAt6dMb/gqoX2Pb3VrjLdXt0pAVL61/img.png)

<br>

### **MVVM 패턴이란 ?**

------

MVVM[모델 - 뷰 - 뷰 모델(Model - View - viewModel)]은 아래와 같은 패턴을 말한다.

> 마크업 언어나 GUI 코드를 비지니스 로직 또는 백엔드 로직과 분리하여 개발하는 소프트웨어 아키텍처 패턴을 말한다.

이 정의를 다시 정리해보면 화면 앞단(프론트엔드)의 화면 동작과 관련된 로직과 화면 뒷단(백엔드)의 DB 데이터 처리 로직을 분리하여 더 깔끔하게 코드를 구성한다는 말을 뜻한다.

 

MVVM 패턴은 데이터를 가능한 순수한 응용 프로그램 모델에 가깝게 바인딩하는 데이터 바인딩과 프레임워크의 장점을 활용함과 동시에 MVC가 제공하는 기능 요소 개발의 분리라는 장점까지 해서, 이 둘을 다 얻어갈 수 있다.

 

이는 바인더, 뷰 모델, 그리고 어떤 비지니스 계층에 있는 데이터-검사 기능을 사용하여 들어오는 데이터를 검증한다.

 

결과적으로 모델과 프레임워크가 가능한 많은 작업을 수행하며, 뷰를 직접 조작하는 응용 프로그램 로직은 최소화하거나 아예 없애 버릴 수 있다는 특징이 있다.

------

 <br>

### **MVVM의 구성 요소**

------

#### **모델(Model)**

> 모델(Model)은 실제 상태 내용을 표현하는 도메인 모델을 참조하거나 내용을 표현하는 데이터 접근 계층을 참조한다.

 <br>

#### **뷰 (View)**

> 뷰(View)는 MVC와 MVP 패턴에서와 같이 뷰는 사용자가 화면에서 보는 것들에 대한 구조, 배치와 같이 외관에 해당한다. 
>
> 모델을 보이게 표현하고 사용자와 뷰의 상호 작용을 수신하여, 이에 대한 처리를 뷰와 뷰 모델의 연결을 정의하고 있는 데이터 바인딩(속성, 이벤트 콜백 함수 등)을 통하여 뷰 모델로 전달한다.

 <br>

#### **뷰 모델(View Model)**

> 뷰 모델(View Model)은 공용 속성과 공용 명령을 노출하는 뷰에 대한 추상화를 말한다.
>
> MVVM은 바인더(Binder)를 가지고 있는데, 이는 뷰 모델에 있는 뷰에 연결된 속성과 뷰 사이의 통신을 자동화한다. 뷰 모델은 모델에 있는 데이터의 상태라고 표현을 하기도 한다.

 

------

 <br>



![[Vue] MVVM 패턴이란? (개념 / 특징 / 장점) - undefined - MVVM의 구성 요소 - 뷰 모델(View Model)](https://blog.kakaocdn.net/dn/bNGfjI/btrzKtteE6W/FKaJiGxOh9Qlm2BRZX3rpk/img.png)https://012.vuejs.org/images/mvvm.png

<br>

### **MVVM 장점**

------

> 1. View가 Data를 실시간으로 관찰한다.
>
> Observable 패턴을 이용하기 때문에 DB를 관찰하고 자동으로 UI를 갱신해줄 수 있다.
>
> 2. 모듈화를 할 수 있다. (독립성 향상)
>
> UI, 비지니스 로직, DB가 기능별로 모듈화가 되어있어, 역할 별로 유닛테스트가 용이해진다.
>
> 3. LifeCycle로 부터 안전해진다.
>
> ViewModel을 통해 데이터를 참조하기 때문에 Activity | Fragment의 LifeCycle을 따르지 않는다.
>
> 4. 가상 돔(Virtual DOM)을 사용한다.
>
> 가상 돔을 활용하면 특정 돔 요소를 추가하거나 삭제하는 변경이 일어날 때 화면 전체를 다시 그리지 않고 프레임 워크에서 정의한 방식에 따라 화면을 갱신할 수 있다.
>
> 이에 따라 브라우저 입장에서는 성능 부하가 줄어들어 일반 렌더링 방식보다 보다 더 빠르게 그릴 수 있게된다.

<br>

<br>

<br>

### 참고링크: [[Vue\] MVVM 패턴이란? (개념 / 특징 / 장점) (tistory.com)](https://jeongkyun-it.tistory.com/136)

<br>

<br>

<br>

# 🎉 Vue의 MVVM 패턴 이해

<br>

> VUE는 MVVM 패턴을 이용합니다. 이중 VM(ViewModel)계층에 집중한 프레임워크입니다.
> 따라서 MVVM 패턴 및 MVC, MVP패턴을 간단히 알아보고 vue에서의 MVVM에 대하여 알아보도록 하겠습니다.

<br>

## MVVM 패턴

뷰가 특정 모델에 종속되지 않도록 모델(로직)을 분리한 패턴입니다.
간단히 뷰와 모델, 뷰모델을 분리하여 독립적인 개발을 할 수 있도록하여, 테스트, 유지 보수, 재사용성을 높인 패턴입니다.

<br>

### 구성요소

- 모델(Model) : 사용되는 데이터를 다루는 역할을 하며 비즈니스로직이 포함
- 뷰(ViewModel) : 말 그대로 보이는것, UI를 다루는 역할을 하며, 비즈니스로직이 아닌 UI로직(애니메이션)을 포함
- 뷰모델(View) : 뷰만을 위한 모델로 뷰가 사용하는 메서드,필드를 갖고 View에 상태 변화등을 알리며, 뷰가 사용할 수 있도록 데이터를 바인딩한다.

<br>

### 그렇다면 어떻게 VM과 V의 독립적이게 했을까?

**Command패턴**과 **Data Binding**을 통해 의존을 제거했습니다.
Command패턴은 객체의 메서드를 클래스로 캡슐화하는 패턴으로 A객체의 메서드를 B가 사용할 경우 A를 참조하는 의존성을 제거합니다.
(인터페이스를 통한 필수 구현 요소정의 -> 이를 구현한 기능 분리된 클래스(생성자로 객체를 받음) -> 객체 구현 => 사용! )
이는 뷰에서 필요한 메서드, 필드등을 모듈화하여 독립적으로 구현할 수 있도록 합니다.
Data Binding은 뜻 그대로 VIEW에서 사용할 데이터 및 뷰모델의 기능 등을 결합해주는 것입니다.

<br>

### 순서

ACTION --> V -(action 전달)-> VM -(데이터 요청, 데이터 변경 요청)-> M -(응답)-> VM -(Data Binding)-> V

<br>

<br>

<br>

### 참고링크: [VUE의 MVVM 패턴 이해 (velog.io)](https://velog.io/@sensecodevalue/VUE의-MVVM-패턴-이해와-MVC-MVP에대한-간단-설명)

<br>