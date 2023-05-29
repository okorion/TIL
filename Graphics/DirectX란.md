![img](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Microsoft-DirectX-Logo-wordmark.svg/250px-Microsoft-DirectX-Logo-wordmark.svg.png)



# 1. 📹 DirectX란?

 혹시 Unity나 언리얼을 이용하여 게임을 하나 만들어 본 적 있는가? 필자는 슈팅 게임 예제를 모방하여 만들어 본 것이 고작이다...

 아무튼! 게임 엔진에서는 물체가 무슨 역할을 하는지(플레이어인지, 그저 환경 물체인지 등)을 결정하고, 그에 맞는 역할을 코딩할 수 있다.

 그러면 다른 질문을 해보겠다. 이러한 게임 엔진이 무엇을 기반으로 만들어졌는지 궁금했던 적이 있지 않는가? 않아도 괜찮다. 지금 여기서 말해줄 것이다. 이러한 게임 엔진, VRML, Java3D와 같은 **고수준 에디터 또는 API** 는 바로 **저수준 그래픽 API** 를 이용하여 만들어진 것이다. 그리고 이러한 저수준 그래픽 API에는 OpenGL, DirectX가 있다. 

 이 블로그에서는 그 중에서도 DirectX에 대해서 이야기 할 것이다.



 **Microsoft DirectX**(마이크로소프트 다이렉트엑스)는 [멀티미디어](https://ko.wikipedia.org/wiki/멀티미디어), 특히 [게임](https://ko.wikipedia.org/wiki/게임) [프로그래밍](https://ko.wikipedia.org/wiki/프로그래밍)에서 [마이크로소프트](https://ko.wikipedia.org/wiki/마이크로소프트) [플랫폼](https://ko.wikipedia.org/wiki/컴퓨팅_플랫폼)에서 작업을 위한 [API](https://ko.wikipedia.org/wiki/API)의 집합이다. 다이렉트엑스는 마이크로소프트 [윈도우](https://ko.wikipedia.org/wiki/마이크로소프트_윈도우), [세가](https://ko.wikipedia.org/wiki/세가), [드림캐스트](https://ko.wikipedia.org/wiki/드림캐스트), 마이크로소프트 [엑스박스](https://ko.wikipedia.org/wiki/엑스박스) 및 [엑스박스 360](https://ko.wikipedia.org/wiki/엑스박스_360)을 위한 [비디오 게임](https://ko.wikipedia.org/wiki/비디오_게임) 개발에 널리 쓰인다.(위키비디아 발췌)

 

![img](https://t1.daumcdn.net/cfile/tistory/2268704C5797694F36)

(Watch_Dogs 또한 DirectX를 이용하여 개발한 엔진으로 만들어진 게임 중 하나이다.)



 DirectX는 게임과 같은 응용 프로그램과 그래픽 하드웨어를 연결해주는 다리와도 같다. 따라서 사용자는 해당 그래픽 하드웨어가 DirectX 대응장치이기만 한다면, 하드웨어의 세부사항을 알 필요 없이 이 API를 이용하여 그래픽 하드웨어에 접근하고, 물체를 렌더링하는 등의 작업을 할 수 있다.

<br>

<br>

# 2. DX9 -> DX11

 현재 DirectX는 12 버전까지 나왔다. 하지만 이 블로그에서는 DirectX11을 다룰 생각이다. 이유는 12버전은 DirectX 숙련자를 대상으로 한 API이라, 접근성이 낮기 때문이다.(아마도)

 이전의 DirectX9 버전은  해당 API의 일부만 지원해도 되었다. 하지만 11로 넘어오면서 이제 그래픽 하드웨어는 DirectX의 모든 기능을 제고해야 한다는 엄격한 기준이 생겼다. 덕분에 DirectX의 특정한 기능을 이용할 때 더이상 기능 점검할 필요가 없어지게 되었다.

<br>

<br>

# 3. COM(Component Object Model)

 **컴포넌트 오브젝트 모델**은 [마이크로소프트](https://ko.wikipedia.org/wiki/마이크로소프트)가 개발한 소프트웨어 구성 요소들의 [응용 프로그램 이진 인터페이스](https://ko.wikipedia.org/wiki/응용_프로그램_이진_인터페이스)이다.(위키피디아 발췌)

 DirectX에서의 COM은 프로그래밍 언어의 독립성과 하위 호환성을 가능하게 하는 기술이라고 한다. COM은 인터페이스 형식으로 제공되며, 개발자는 COM 인터페이스로의 포인터를 특별한 함수나 다른 COM 인터페이스의 메서드를 이용하여 얻어야 한다.

 COM 객체는 new로 생성할 수 없다. 때문에, 해당 객체를 메모리에서 제거할 때에는 delete가 아니라 Release라는 메서드를 호출하여 삭제해야 한다. 이는 모든 COM 인터페이스가 IUnknown이라는 COM 인터페이스 기능을 상속받는데, 여기서 해당 메서드를 제공하기 때문이고, 이 객체들이 고유한 방식으로 메모리를 관리하기 때문이다.

<br>

<br>

# 4. Texture

 텍스처 하면 무엇이 떠오르는가? 보통 3D 물체를 감싸는 2차원 이미지를 떠올릴 것이다. 맞다. 이것도 텍스처의 일종이다. 이러한 이미지 형식의 텍스처는 2차원 배열 형식으로 제공되며, 각 원소에 대응하는 픽셀들의 색상 정보가 들어갈 수 있다. 하지만 텍스처는 단지 이것만 가리키는 말이 아니다. 예를 들어 법선 매핑이라고 하는 고급 기법에서는 각 원소가 색상 정보가 아닌 3차원 벡터를 담는다. 어떤 텍스처는 형식이 없는 데이터를 담아서, 이후 파이프라인에서 정의하여 사용하는 경우도 있다. 텍스쳐의 형식 또한 단지 배열 뿐만이 아닌, 밉맵 수준들이 존재하는 텍스처, 또는 GPU에서는 필터링이나 다중 표본화와 같은 연산에도 텍스처를 적용할 수도 있다.

DirectX에서는 특정한 형식을 따르는 자료를 텍스처로써 저장할 수 있다. 이러한 텍스처의 자료형들은 DXGI_FORMAT이라는 열거형으로 저장된다. 몇 가지를 살펴보자.

1. DXGI_FORMAT_R32G32B32_FLOAT : 각 원소는 32비트 부동소수점 성분 세 개로 이루어져 있다.
2. DXGI_FORMAT_R16G16B16A16_UNORM : 각 원소는 [0, 1] 구간으로 사상되는 16비트의 네 개의 부호 없는 정수 성분으로 이루어져 있다.
3. DXGI_FORMAT_R8G8B8A8_UNORM : 2번과 형식은 비슷하나, 각 요소당 8비트씩 제공된다는 것이 다른 점이다.

여기서 나오는 R, G, B는 색상을 나타낼 때 사용되는 그 RGB가 맞다. 뒤에 A가 나올 수도 있는데, 이것은 Alpha, 투명도를 나타낼 때 사용된다. 앞에서 언급했듯, 이러한 자료형에는 색상뿐만이 아닌 3차원 벡터도 담을 수 있고, 무형식 텍스처를 지정할 수도 있다. 무형식 텍스처 자료형은 다음과 같이 제공된다.

DXGI_FORMAT_R8G8B8A8_TYPELESS



<br>

<br>



#### 참고링크: [1. DirectX - DirectX란 무엇인가? :: I Like This Blog (tistory.com)](https://zerapix.tistory.com/entry/1-DirectX-DirectX란-무엇인가-1)

<br>