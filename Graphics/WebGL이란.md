## 🧸 WebGL?

Web Graphics Library의 약자로 웹상에서 2D 및 3D 그래픽을 **렌더링**하기 위한 로우 레벨 JavaScript API이다.
**OpenGL** ES2.0을 기반으로 브라우저 엔진에 내장된 **HTML5 Canvas** 요소 위에 그려진다.

<br>

### 렌더링?

렌더링은 컴퓨터 프로그램을 사용하여 모델에서 미지를 생성하는 프로세스이다.

- 소프트웨어 렌더링: 모든 그래픽 계산을 CPU의 도움으로 수행한다.
- 하드웨어 렌더링: 모든 그래픽 계산을 GPU(그래픽 처리 장치)에 의해 수행한다.

WebGL은 클라이언트 사이트 렌더링을 통해 3D 장면을 렌더링하며, 이미지를 얻는데 필요한 모든 처리는 클라이언트의 그래픽 하드웨어를 사용해서 로컬에서 수행하게 된다.
WebGL은 웹브라우저에서 GPU를 사용하여 화면 렌더링 -> 빠르다

<br>

### OpenGL?

OpenGL이란 Open Graphics Library로, Graphics 프로그래밍을 위한 **API**이다.

- 프로그래밍 언어 간 플랫폼 간의 교차 응용 프로그래밍을 지원
- 약 250여개 가량의 함수 호출을 이용하여 단순한 기하도형에서부터 복잡한 삼차원 장면을 생성

<br>

<br>

## WebGL 장점

- 누구나 사용가능
- 렌더링 가속화를 지원하는 그래픽 하드웨어를 활용
- 별도의 플러그인이 필요 없으며, 웹 브라우저에 내장되어 실행
- OpenGL API에 대한 경험이 있다면 다루기 쉬움
- **자바스크립트 프로그래밍이 가능하다.** 자바스크립트는 자동 메모리 관리를 지원하기 때문에 메모리를 수동으로 할당할 필요도 없고 WebGL이 자바스크립트의 기능을 상속 받는다.
- 모바일 브라우저에서도 사용 가능 (모든 모바일 브라우저 의미X)

<br>

## WebGL 용어

- 정점(vertex) 3차원 개체의 가장자리의 결합을 형성하는 점이다.
  자바스크립트 배열을 사용하여, 정점을 수동으로 저장하고 정점 버퍼를 사용하여 WebGL 렌더링 파이프라인에 전달해야 한다.
- 인덱스(index) 정점을 식별하는 숫자 값. 인덱스를 이용하여 WebGL의 mesh를 그리는데 사용한다.
- 버퍼(buffer)는 데이터를 가지고 있는 WebGL의 메모리 영역이다. 다양한 버퍼가 존재
- 기하(geometry)
- 텍스처(texture)
- 프래그먼트(fragment)
- 타입드어레이(typed array)

<br>

### WebGL과 ThreeJS ?

ThreeJS와 같은 라이브러리를 사용하여 WebGL을 더 쉽게 3D렌더링을 할 수 있다.

<br>

[출처] https://code-masterjung.tistory.com/110
[출처] https://gofo-coding.tistory.com/entry/OpenGL

<br><br><br>

#### 참고링크: [WebGL이란? (velog.io)](https://velog.io/@0hyo/WebGL이란)

<br>