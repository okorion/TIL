## 🔭 OpenGL이란?

 **1.1 OpenGL 이란?**

**OpenGL**(**Open** **G**raphics **L**ibrary)은 1992년 실리콘 그래픽스사에서 만든 2차원 및 3차원 그래픽스 표준 API 규격으로, 프로그래밍 언어 간 플랫폼 간의 교차 응용 프로그래밍을 지원한다. 

이 API는 약 250여개 가량의 함수 호출을 이용하여 단순한 기하도형에서부터 복잡한 삼차원 장면을 생성할 수 있다.



OpenGL의 동작은 Vertices를 Pixels로 변환하는 과정을 지원합니다.



여기서 vertex와 pixel의 차이점에 대해서 알아보겠습니다.

\* Vertex

도형을 구성하는 하나의 점

\* Pixel

모든 렌더링 연산이 끝난 후 모니터에 보이는 하나의 점



차이점에 대해서 이해가 가시나요? 

앞으로 정리하면서 Vertex -> Pixel 의 변환과정에 대해 하나 하나 알아보겠습니다.

<br>

 **1.2 Image Formation**

<br>

이미지의 구성에 대해 정리하겠습니다.

이미지는 어떠한 요소들로 구성될까요? 



![img](https://t1.daumcdn.net/cfile/tistory/270EF43957FF88AC09)



위 사진을 보면서 하나 하나 살펴보겠습니다.



이미지는 크게 3가지로 구성되어 있습니다. 그림에서도 3가지가 존재하죠 ^^



\- Object

\- Viewer

\- Light Source(s)

<br>

이 3가지 형태가 있어야 우리가 OpenGL을 통해 객체를 볼 수 있습니다.

<br>

Object는 객체입니다. 사물이 될 수도 있고, 사람이 될수도 있습니다. 우리 눈에 보이는 특정한 객체라고 생각하시면 될 것 같습니다.

Viewer는 현실에서의 우리 눈이라고 생각하세요. 물론 컴퓨터에서는 특정 위치, 방향에 Viewer가 존재하겠죠? 앞으로 Viewer는 Camera에 빗대어서 자주 언급하겠습니다.

Light Source(s)는 광원입니다. 태양 또는 형광등 정도로 생각하시면 되겠어요. 그래서 다양한 형태로 존재할 수 있기에 복수로 표시했습니다.

<br>

차후에 광원의 여러 종류에 대해 배울 예정입니다. 서로 다른 다양한 형태의 광원이 존재하기 때문이죠 ! (흔히 공연장에서 보는 Spot Light , 태양과 같은 전역 Light Source 등등....)

<br>

위 3가지가 존재한다면 이미지를 구성할 수 있습니다. 하지만 현실적으로 구현하기 위해 한 가지 요소가 더 필요합니다.

![img](https://t1.daumcdn.net/cfile/tistory/2120073857FF8ADF24)         ![img](https://t1.daumcdn.net/cfile/tistory/252CFC3457FF8AE728)



위 2개의 사진을 보면 마지막 추가적인 요소가 무엇인지 알겠나요?

바로 **Attributes (materials)** 입니다.

현실적인 그래픽 이미지 구현을 위해서는 위 요소가 필수적입니다.

재질에 따라 빛이 반사하는 정도, 표면의 거침 등 많은 것들에 차이가 있기 때문입니다.

<br>

그래서 OpenGL에서 Image Formation 요소는 위 4가지로 정리할 수 있습니다.

<br>

 **1.3 Graphics Pipeline**

<br>

위에서 언급했던 Vertex -> Pixel 변환 과정에 대해 간략히 알아보겠습니다.

이를 Graphics Pipeline이라고 합니다.

과정은 아래와 같습니다.



![img](https://t1.daumcdn.net/cfile/tistory/217ED53F57FF8BEE21)



Vertex가 입장하여 여러 과정을 거쳐 Pixels로 재탄생합니다.

파이프라인 구조로 처리하기 때문에 이 순서가 중요합니다. 기억해두시면 좋습니다~

오늘은 대략적인 역할과 순서에 대해서만 익히겠습니다.

<br>

\- Vertex Processor

이 과정에서는 좌표 체계를 변환합니다. 즉 3D객체를 2D형태인 모니터 화면에 띄우기 위해 좌표를 변환시키는 작업을 합니다.

모든 변환은 행렬변환을 통한 계산으로 이루어 집니다.

<br>

\- Primitive Assembler and Clipper

이 과정에서는 먼저 Primitive Assembler을 거칩니다. Vertex Processor를 통과한 각 좌표 정보를 바탕으로 Line, Polygon, Curve, Suface 등 어떻게 표현할 지 결정되고 이러한 정보를 바탕으로 vertex가 수집되는 단계입니다.

<br>

이후 Clipper과정은 쉽게 이해할 수 있습니다. Viewer, 즉 Camera에 보이는 부분은 유지하고, 보이지 않는 부분은 버리는 작업을 합니다.

![img](https://t1.daumcdn.net/cfile/tistory/233F133A57FF8E4F05)



COP가 현재 Viewer의 위치입니다.

그림에서 볼 수 있듯이 Front clipping plane과 Back clipping plane을 설정하여 그 사이 범위인 View volume 밖에 있는 객체는 처리하지 않고 잘라냅니다.

현실 세계에서 카메라가 전체 세계를 볼 수 없듯이, 그래픽스 환경에서의 Viewer도 전체의 한 부분만 볼 수 있기에 설정하는 것이죠.

<br>

\- Rasterizer

이전 단계 까지를 거치며, 제거되지 않은 점들에게는 color가 할당됩니다. Rasterizer은 각 객체의 color와 depth 정보를 부여하여 실제 화면이 보이게끔 합니다.

<br>

\- Fragment Processor

이 과정에서는 최종적으로 보여지는 객체에 대한 정보를 구현합니다.

각 Pixel에 대해 복합적인 정보를 계산하여 최종적으로 결정합니다.

ex) 물체가 파란색, 조명이 빨간색 -> 보라색으로 계산

또한 조명의 위치, 물체의 위치, 표면의 Normal vector 등을 바탕으로 실제 우리가 확인 할 수 있는 객체를 화면에 표시하기 전 최종적으로 처리하는 단계입니다.

앞으로 기본적인 객체 정보 이외에 vertex shader와 fragment shader를 활용하여 객체를 더욱 사실적으로 구현하는 것에 대해 공부하겠습니다.

<br>

 **1.4 마무리**



간단하게 OpenGL에 대해 알아보고 기본적인 Pipeline 구조에 대해 정리 해 보았습니다.

첫 포스팅인 만큼 OpenGL이라는 것에 대해 대략적으로 파악하는 시간이 되었길 바랍니다.

다음 포스팅은 앞으로 사용할 OpenGL의 특징 및 버전 확인, 설치 등등에 대해 확인하겠습니다.

질문이 있으시면 코멘트 주세요!

혹시 잘못된 정보가 있더라도 코멘트 주세요!

긴 글 읽어 주셔서 감사합니다. 모두 그래픽스에 대해 함께 공부하여 익숙해졌으면 좋겠네요!

<br>

------



**참고**

\- **Wiki : https://ko.wikipedia.org/wiki/OpenGL**

**- E. Angel and D. Shreiner: Interactive Computer Graphics 6E © Addison-Wesley 2012**



<br>

<br>

#### 참고링크: [[OpenGL-1\] OpenGL이란 (tistory.com)](https://zamezzz.tistory.com/13)

<br>

추가- [The OpenGLR Graphics System: A Specification (Version 3.3 (Core Profile) - March 11, 2010)]([OpenGL 3.3 (Core Profile) - March 11, 2010 (khronos.org)](https://registry.khronos.org/OpenGL/specs/gl/glspec33.core.pdf))