### [**Gradle 이란?**](https://kdhyo98.tistory.com/87#Gradle%--%EC%-D%B-%EB%-E%--%-F)

> https://github.com/gradle/gradle
>
> [Gradle](https://gradle.org/) 은 빌드 자동화 및 다국어 개발 지원에 중점을 둔 빌드 도구입니다.
> 모든 플랫폼에서 소프트웨어를 Building, Testing, publishing, deploying 하는 경우
> Gradle 은 코드 컴파일 및 패키징에서 웹 사이트 게시에 이르기까지
> 전체 개발 수명 주기를 지원할 수 있는 유연한 모델을 제공합니다.
>
> Gradle은 Java, Scala, Android, Kotlin, C/C++ 및 Groovy를 비롯한 여러 언어 및 플랫폼에서
> 빌드 자동화를 지원하도록 설계되었으며 Eclipse, IntelliJ 및 Jenkins를 비롯한
> 개발 도구 및 지속적 통합 서버와 긴밀하게 통합됩니다.

 

### [**빌드도구 란?**](https://kdhyo98.tistory.com/87#%EB%B-%-C%EB%--%-C%EB%-F%--%EA%B-%AC%--%EB%-E%--%-F)

소스코드를 어플리케이션으로 만들어주려면 다양한 작업(컴파일, 테스트, 배포)들을 진행해야 합니다.

빌드도구는 코드에서 어플리케이션으로 만드는 일련의 작업들을 자동화하여

**실행 가능한 어플리케이션으로 만들어주는 도구**입니다.

 

자바의 빌드 도구로서는 Ant, Maven, Gradle이 존재하고

초기에는 Ant를 많이 사용했지만, 최근에는 Maven과 Gradle을 주로 사용하고 있습니다.

 

### [**Maven과 Gradle**](https://kdhyo98.tistory.com/87#Maven%EA%B-%BC%--Gradle)

#### [**Maven 특징**](https://kdhyo98.tistory.com/87#Maven%--%ED%-A%B-%EC%A-%--)

\- Apache Ant 대안으로 만들어진 Apache 라이센스로 배포되는 오픈 소스 소프트웨어

\- 자바용 프로젝트 관리 도구

\- xml을 이용한 빌드 시스템

\- 직접 연결한 라이브러리들과 라이브러리들이 엮여있는 다른 라이브러리들까지 연동되어 관리

 

#### [**Gradle 특징**](https://kdhyo98.tistory.com/87#Gradle%--%ED%-A%B-%EC%A-%--)

\- 오픈소스 기반의 빌드 자동화 시스템

\- JVM 기반의 빌드도구로 기존의 Ant, Maven을 보완

\- Android OS의 빌드 도구로 채택

\- Maven을 사용할 수 있는 변환 기능 컨벤션 프레임워크

\- Maven과 Ivy 레파지토리 지원

\- 멀티 프로젝트의 빌드를 지원하기 위해 설계

\- Groovy, Kotlin 문법 사용

 

Maven이 먼저나온 만큼 아직까지 사용하는 곳이 많긴하나 Gradle이 나온지도 10년이 되었습니다. (2022 기준)

 

둘다 사용해본 개인적인 생각으로는

Gradle을 선택하는 게 더 좋다고 생각하고, 그 이유는 아래와 같습니다.

> \- xml로 관리되는 메이븐에 비해 짧고 간결한 문법
> \- Java 용인 Maven에 비해 C/C++ 등 다른 언어에서도 사용가능한 범용성
> \- 최소 2배에서 빌드 캐시를 사용하는 대규모 빌드의 경우 100배 정도의 성능차이 ([링크](https://gradle.org/maven-vs-gradle/))

------

### [**Groovy Gradle, Kotlin Gradle**](https://kdhyo98.tistory.com/87#Groovy%--Gradle%-C%--Kotlin%--Gradle)

#### [**기존 Groovy 에서 Kotlin 으로 변경하는 이유로는 뭐가 있을까요?**](https://kdhyo98.tistory.com/87#%EA%B-%B-%EC%A-%B-%--Groovy%--%EC%--%--%EC%--%-C%--Kotlin%--%EC%-C%BC%EB%A-%-C%--%EB%B-%--%EA%B-%BD%ED%--%--%EB%-A%--%--%EC%-D%B-%EC%-C%A-%EB%A-%-C%EB%-A%--%--%EB%AD%--%EA%B-%--%--%EC%-E%--%EC%-D%--%EA%B-%-C%EC%-A%--%-F)

\- IDE 와의 뛰어난 호환성으로 코드 자동완성 기능

\- 오류코드 강조

\- 빠른 문서보기 가능

\- 리팩터링

\- Groovy와는 다른 코드스타일 제약

\- Kotlin을 사용하는 프로젝트 경우 언어 통일 가능

 



![img](https://blog.kakaocdn.net/dn/qVFHj/btrDOzdlT9P/B9Si7vDxeoSzY7Y3kZxChK/img.png)Groovy Gradle

![img](https://blog.kakaocdn.net/dn/bqM4v0/btrDMzxCENi/9HbRHdWyOC0pq01m6WeJPK/img.png)kotlin Gradle



직접 적용했을 때 느껴본 큰 장점은 위 사진과 동일한 내용입니다.

 

혼자 진행하지 않는 이상 여러 사람들과 협업하여 진행하는 프로젝트는

약간의 강제성이 있어야 수월하게, 일관성있게 작성할 수 있다고 생각합니다.

 

그런 측면에서 Kotlin Gradle의 경우 **("") 구문만 사용하도록 강제**하는 부분과,

**IDE의 지원으로 오류를 강조**해주는 부분이 마음에 들었습니다.

 

하지만, 모든 IDE에서 똑같이 제공하진 않ㅇ며 **Intellij, Android Studio**를 사용해야 합니다.

|                             | **빌드 가져오기** | **구문 강조** | **시맨틱 편집기** |
| --------------------------- | ----------------- | ------------- | ----------------- |
| **Intellij IDEA**           | ✔                 | ✔             | ✔                 |
| **Android Studio**          | ✔                 | ✔             | ✔                 |
| **Eclipse IDE**             | ✔                 | ✔             | ❌                 |
| **CLion**                   | ✔                 | ✔             | ❌                 |
| **Apache NetBeans**         | ✔                 | ✔             | ❌                 |
| **Visual Studio Code(LSP)** | ✔                 | ✔             | ❌                 |
| **Visual Studio**           | ✔                 | ❌             | ❌                 |

 

출처: [[Java\] Gradle, Groovy Gradle, Kotlin Gradle — 일단은 내 이야기 (tistory.com)](https://kdhyo98.tistory.com/87#%EB%B-%-C%EB%--%-C%EB%-F%--%EA%B-%AC%--%EB%-E%--%-F)