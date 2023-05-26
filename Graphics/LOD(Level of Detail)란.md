## 🎋 LOD(Level of Detail)란

## 1. LOD(Level Of Detail)

=> 3D Model의 복잡성

=> 가상 세계를 나타내는 데 사용되는 세부 정보의 양을 규제함으로써 복잡성과 성능을 향상시키는 방법

=> 실시간(Realtime) Rendering에서 속도를 빠르게 하기 위해 생긴 기술

=> Model이 Viewer로부터 멀어질 때 중요도 등 다른 지표에 따라 감소될 수 있음

=> 보통은 Graphic pipeline 단계에서 작업량을 줄여 효율성을 높이는데에 사용

=> 1976년 Clark라는 사람이 "Hierarchical Geometric Models for Visible Surface Algorithms" 논문에서 LOD를 처음 표면화

 



![img](https://blog.kakaocdn.net/dn/ehBoA2/btq4INwhABE/gYEj0T9JoD3F7CkPgEyTO1/img.png)

![img](https://blog.kakaocdn.net/dn/noGXA/btq4MBawK82/A3DZuf8D3y585vzFIe2kR1/img.png)



## 2. LOD Frameworks

=> 세부 수준 관리를 위한 기본 프레임워크

<br>

#### 2-1. Discrete LOD [속도중심]

=> LOD에 대한 기존의 접근 방식

=> 미리 Object의 다른 level의 Detail을 생성해두는 것

=> Runtime에 개체를 나타내도록 Level에 따라 선택

=> isotropic 혹은 view-independent LOD라고도 부름

=> 장점

  -> Decoupling Simplification 및 Rendering으로 프로그래밍 하는 가장 간단한 모델

  -> Rendering은 렌더링할 LOD를 선택하는데만 필요해서, 속도가 빠름

  -> LOD를 생성할 때 실시간 렌더링 제약 조건을 해결할 필요가 없음

  -> 최신 그래픽 H/W에 적합함(H/W에서 체계화되지 않은 삼각형보다 빠르게 렌더링)

=> 단점

  -> 기존에 저장을 해두어야 하기 때문에 Memory가 많이 필요함

  -> 갑작스런 단순화에(Drastic Simplification)에 적합하지 않음

​    [큰 물체를 세분화 하거나, 작은 물체를 조합하는 것들]

​    -> Terrain flyover

​    -> Volumetric isosurfaces

​    -> Super-detailed range scans



<br>

#### 2-2. Continuous LOD[성능중심]

=> 세부 디테일들을 인코딩하는 data 구조를 생성

=> 이후 runtime에 원하는 LOD를 위의 구조에서 추출

=> 장점

  -> 상대적으로 세분성이 좋음

  -> Discrete에 비해 정확하게 지정되어 필요 이상의 polygon은 사용되지 않음[Memory]

  -> Polygon count에 대한 resource 사용률이 향상됨

  -> 다각형 모델의 streaming이 가능(즉, 대형모델을 disk/network로 load해야하는 경우 연속적 loading이 가능)

  -> 연속적 LOD로 시각적 popping 방지

  -> 단일 객체가 여러 LOD에 걸쳐있을 수 있음(현재 view에 대한 최상의 표현 가능)

=> 단점

  -> 계산량이 많아 속도가 상대적으로 느리고 프로세서의 부하가 큼

  -> Device lock에 의한 병목현상 가능



![img](https://blog.kakaocdn.net/dn/cuTcDB/btq4Md8RhaL/XB583hW1dd5H3WQiA6fItK/img.png)discrete vs continuous



<br>

#### 2-3. View-dependent LOD[성능중심]

=> 물체의 주변 부분을 먼 부분보다 높은 해상도로 표시

=> 즉, 현재 뷰에 가장 적합한 LOD를 Dynamic하게 선택하여 continuous LOD를 확장

=> 주변 시각보다는 사용자가 보고 있는 곳을 더 자세히 보여주는 방식(보통은 중앙)

=> 장점

  -> polygon count에 대한 resource 사용률이 향상됨

  -> 지형과 같은 물리적으로 큰 물체를 나타내는 복잡한 모델을 획기적으로 간소화

  -> 수동 개입이나 분할을 위한 추가 처리 없이 interactive rendering이 가능함

=> 단점

  -> 계산량이 많아 속도가 느리고 프로세서의 부하가 큼



![img](https://blog.kakaocdn.net/dn/1aX0G/btq4MCtQF6l/j7W3vFHTMK6zeHp2kOs5xK/img.png)viewpoint vs otherside



<br>

#### 2-4 Hierarchical LOD[속도 + 성능]

[UE4 : [docs.unrealengine.com/ko/BuildingWorlds/HLOD/index.html](https://docs.unrealengine.com/ko/BuildingWorlds/HLOD/index.html)]

=> view-dependent로 대형 문제를 해결했다면 소형 객체는 Hierarchical LOD로 해결 가능

=> 객체를 assembly로 병합하여 조립을 단순화 하는것

=> 쉽게이야히가면, 다수의 Mesh를 원거리에서봤을 때 하나의 Static Mesh로 합치는 기법

=> Mesh 당 1 Draw call에서 합쳐진 Mesh당 1 Draw call로 줄여 성능 향상

  \+ Draw call : Scene에 있는 vertex를 그리기 위해 CPU가 GPU에게 보내는 요청[퍼포먼스에 큰 영향]



![img](https://blog.kakaocdn.net/dn/cvKzTB/btq4MfyUmmz/TlVW6jyQH1196v0uhd1nk0/img.jpg)



<br>

<br>

출처 : [courses.cs.duke.edu/spring15/cps124/classwork/10_terrain/LOD.pdf](https://courses.cs.duke.edu/spring15/cps124/classwork/10_terrain/LOD.pdf)

출처2 : [theswissbay.ch/pdf/Gentoomen%20Library/Game%20Development/Programming/Level%20of%20De](https://theswissbay.ch/pdf/Gentoomen Library/Game Development/Programming/Level of Detail for 3D Graphics.pdf)

<br>

<br>

#### 참고링크: [LOD - LOD(Level Of Detail) Frameworks - 메리군의 스터디 (tistory.com)](https://merry-nightmare.tistory.com/257)

<br>