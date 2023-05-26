## 🥪 벌컨(Vulkan)이란

### 🛹 OpenGL의 한계

#### - 벌컨(Vulkan) 탄생 배경

 1992년 OpenGL 1.0이 세상에 출시되었다. 지금까지 OpenGL은 발전되고 있고 수 많은 어플리케이션이 OpenGL을 사용하고 있다. 하지만 CPU가 싱글코어 프로세서에서 멀티코어 프로세서로 발전하고 GPU가 Fixed Function Pipeline에서 Unified Pipeline으로 발전하면서 OpenGL은 한계에 부딪히고 있다.

<br>

 OpenGL은 State Machine의 구조를 가지고 있다. State Machine의 정의를 간단하게 설명하면 State를 변경하는 명령을 받기 전에는 현재의 State를 계속 유지하고 있다. 다시 말해 사용자는 렌더링을 위해 OpenGL의 State Machine을 조작하고 그리는 명령을 보내면 OpenGL은 해당 메모리에 렌더링 결과를 출력하게 된다.

// Framebuffer의 클리어 색상값을 설정 glClearColor(1.0f, 1.0f, 1.0f, 1.0f); // framebuffer0 설정 후 설정된 색으로 클리어 glBindFramebuffer(GL_FRAMEBUFFER, framebuffer0); glClear(GL_COLOR_BUFFER_BIT); // framebuffer0 설정 후 설정된 색으로 클리어 glBindFramebuffer(GL_FRAMEBUFFER, framebuffer1); glClear(GL_COLOR_BUFFER_BIT); // framebuffer0 설정 후 설정된 색으로 클리어 glBindFramebuffer(GL_FRAMEBUFFER, framebuffer2); glClear(GL_COLOR_BUFFER_BIT);

 위의 코드를 실행하면 모든 프레임버퍼의 색상이 흰색으로 클리어 되어있다. 이처럼 State가 변경되기전까지 유지되는것을 State Macine이라고 한다. 이 구조는 싱글코어 프로세서에서는 별 문제가 없었지만 멀티코어 프로세서에서 문제가 되기 시작했다. OpenGL의 State Machine이 쓰레드에 안전하지 않기 때문에 다른 쓰레드에서 State를 변경하면 또 다른 쓰레드에서 State를 접근할때 동기화 문제가 발생하게 된다. 그러므로 OpenGL을 사용할 경우 멀티코어 프로세서를 사용하지 못하는 한계가 발생한다.

<br>

 지금은 GPU라는 용어가 굉장히 자주쓰이지만 예전엔 지금의 GPU를 그래픽 카드라고 불렀다. 과거에는 GPU가 주로 렌더링을 위해서만 쓰였다. 하지만 그래픽 카드가 대용량 계산에 이점이 있다는것을 발견하고 그래픽 카드는 대용량 계선을 위해서도 발전하게 되었다. 이때 Cuda, OpenCL과 같은 Compute API를 출시되었다. 다시 말해 오직 그래픽을 위해 구현되어있던 Fixed Function GPU에서 대용량 계산도 지원하기 위한 Unified Shader GPU으로 하드웨어가 변경 되었다.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Unified_shader_model.svg/1200px-Unified_shader_model.svg.png)

  위 그림을 보면 연속적인 하드웨어의 실행에서 하나의 하드웨어롤 반복적으로 사용하도록 변경되었다. 쉽게 설명해 엄청난 성능의 쉐이더 엔진이 도입되면서 그래픽 처리를 위해 구현되어 있던 하드웨어가 사라지고 해당 기능이 쉐이더로 작성된 것이다. OpenGL은 Fixed Function GPU를 동작시키기 위해 만들어진 API이기 때문에 Unified Shader GPU를 잘 반영하지 못하고 있다. 이러한 점은 최신 GPU를 효율적으로 사용하지 못하는 한계가 발생한다.

<br>

 또한 OpenGL은 너무 추상화되어 있기 때문에 드라이버 벤더(NVIDIA, AMD, Qualcomm, ARM, Imagination)에 따라 구현방식 많이 다르다. 그로 인해 동일한 코드일지라도 동작이 다르고 결과가 달라질 수 있다. 최적화의 방식도 드라이버 벤더마다 굉장히 달라질 수 있다. 최악의 경우 특정 최적화가 NVIDIA에서는 빠르나 AMD에서는 느릴 수 있다. 추상적인 개념을 지원하고 모든 어플리케이션에서의 안정성도 확보해야하기 때문에 드라이버 코드가 굉장히 복잡하고 무겁다. 이로인해 많은 CPU자원을 요구하고 이는 성능에 문제가 된다.

<br>

 물론 앞에서 말한 한계점을 OpenGL Extension을 사용하면 해결할 수 있다. 그러나 벤더마다 지원하는 Extension이 다르고 어플리케이션을 벤더별로 구현하는것은 유지보수가 굉장히 힘들어지기 때문에 잘 사용되지 않는다. MS, Apple에선 이러한 한계점을 오래전부터 잘 알고 있었기 때문에  OpenGL을 공식적으로 지원하고 있지 않다. MS는 DirectX로 Apple은 Metal로 OpenGL을 대체하고 있다. 

<br>

<br>

### 🚗 Vulkan의 탄생

 앞에서 언급한 한계점을 해결하기 위해 수 많은 회사들이 Khronos에 모여 표준화를 진행하였다. 본격적인 시작은 AMD가 Mantle를 Khronos에 기부하면서 시작되었다. Mantle은 AMD에 의해 개발되었으며 AMD의 Radeon 카드를 효율적으로 다루기 위해 설계된 API이다. Mantle은 최초의 저 수준 API이며 Mantle을 사용한 게임 및 벤치마크에서 성능이 크게 향상되었다. Mantle의 영향을 받아 MS의 DirectX 12, Apple의 Metal이 출시 되었다. Khronos는 Mantle을 기반으로 Vulkan을 설계했으며 Windows, Linux, Mac, Android, iOS와 같은 다른 운영 체제에서 사용할 수 있다. 아래 동영상은 AMD 설명하는 Vulkan에 대한 동영상이다.

<iframe width="480" height="270" src="https://www.youtube.com/embed/qZLzz3OOl3A?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; top: 0px; left: 0px; width: 693px; height: 389.812px;"></iframe>

Vulkan과 OpenGL의 차이점

  Vulkan과 OpenGL의 가장 큰 차이점은 Vulkan은 저수준의 API이고 OpenGL은 고수준의 API이다. 쉽게 말해 OpenGL은 API가 호출되면 올바른 방법으로 API가 호출되었고 매개 변수들이 잘 전달되었는지 확인한다. 만약 오류가 있다면 개발자에게 피드백을 준다. 한마디로 말해 개발자가 사용하기 쉽고 해야하는 많은 일들이 드라이버 내에서 이뤄진다. 이러한 이유로 OpenGL은 벤더마다 구현방식에 차이가 크고 실제 동작방식이 다르다. 반면 Vulkan은 저수준의 API이다. 즉 개발자가 반드시 API를 올바르게 호출해야하고 올바른 매개 변수를 전달해야 한다. 그렇지 않으면 OpenGL과 달리 어플리케이션이 죽거나 심지어 커널 패닉이 발생할 수 있다.

![img](https://www.xda-developers.com/wp-content/uploads/2016/02/VulkanChart1-1024x523.jpg)

 위의 그림에서 분홍색으로 칠해진 영역이 드라이버에 해당하는 영역이다. OpenGL이 Vulkan에 비해 크기가 굉장히 크다. 이 말은 OpenGL이 많은 처리를 해주고 있다는 말을 의미하고 Vulkan보다 더 CPU 사용량이 더 많다는 의미이다. 저수준의 API를 사용한다는 의미는 개발자가 대부분의 일을 처리해야한다는 말과 같다. 엄격한 프로그래밍을 해야하고 API의 사용 규칙을 반드시 준수해야하고 더 많은 코드를 작성해야한다. 즉 개발자가 그래픽스, 컴퓨트 파이프라인에 대해서 이해를 하고 있어야 하고 각각의 파이프라인을 올바르게 사용하는 방법을 알고 있어야 한다. 이렇게 보면 Vulkan은 사용하기 어렵고 불편한것 처럼 보여서 OpenGL이 더 좋아 보인다. 하지만 Vulkan을 사용함으로써 더 많은것을 할 수 있다.

<br>

 먼저 멀티코어 프로세스의 힘을 최대한 사용할 수 있다. Vulkan은 OpenGL과 달리 State Machine의 구조가 아니다. 즉 여러 쓰레드에서 동시에 Vulkan을 사용해도 문제가 되지 않는다. 물론 Vulkan의 CommandBuffer를 여러 쓰레드에서 접근해선 안된다. 멀티코어 프로세스를 이용해서 렌더링 커맨드를 동시에 기록할 수 있고. 리소스의 복사도 여러 쓰레드에서 동시에 수행할 수 있다. 아래 동영상은 멀티코어 프로세스를 사용한 Vulkan의 이점에 대해 잘 보여준다.

<iframe width="480" height="270" src="https://www.youtube.com/embed/P_I8an8jXuM?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; top: 0px; left: 0px; width: 693px; height: 389.812px;"></iframe>

  Vulkan은 OpenGL에 비해 굉장히 명시적이다. 리소스 할당이 개발자가 원하는 시점에 반드시 생성되고 해제되며 리소스의 생명주기를 관여하지 않는다. 하지만 OpenGL은 개발자가 요청하더라도 리소스 생성을 하지 않을 수 있다.

GLuint buffer; glGenBuffers(1, &buffer); glBindBuffer(GL_ARRAY_BUFFER, buffer); glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

 위의 코드는 OpenGL에서 버퍼를 생성하고 데이터를 업로드 하는 방법이다. 하지만 해당 버퍼가 실제 사용될지 안될지 알 수 없기 때문에 OpenGL에선 실제 버퍼를 생성하지 않고 생성에 필요한 정보들만 유지하고 있을 수 있다. 물론 이러한 동작은 벤더마다 다르다.

VkBufferCreateInfo create_info; create_info.sType = VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO; create_info.size = sizeof(vertices); // 추가적인 버퍼 설정들... vkCreateBuffer(device, &create_info, nullptr, &buffer);

 Vulkan은 OpenGL과 달리 위의 코드처럼 버퍼를 생성하면 바로 버퍼가 생성된다. 이와 같은 명시적인 동작방식으로 인해 여러 벤더일지라도 동일한 동작 방식을 기대할 수 있고 성능도 향상시킬 수 있다.

<br>

<br>

#### 참고링크: [Vulkan이란? : 네이버 블로그 (naver.com)](https://blog.naver.com/dmatrix/221808847792)

<br>