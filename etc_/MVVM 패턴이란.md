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