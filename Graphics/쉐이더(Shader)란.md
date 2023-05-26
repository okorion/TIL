## 🖼️ 쉐이더(Shader)란

책 '유니티 쉐이더 스타트업' 을 보고 공부했습니다.

인터넷 '포프의 쉐이더 입문강좌' 를 참고했습니다. ( https://kblog.popekim.com/2011/11/01-part-1.html )

 

<br>

> 정의

책에서는 이렇게 정의를 내립니다.

'3D 컴퓨터 그래픽에서 최종적으로 화면에 출력하는 픽셀의 색을 정해주는 함수'

 

'포프의 쉐이더 입문 강좌'에서도 비슷하게 정의를 내립니다.

'화면에 출력할 픽셀의 위치와 색상을 계산하는 함수'

 

> 조금 더 쉬운 정의

Shader란, shade + er 입니다.

 

'색의 농담, 색조, 명암 효과를 주다' 라는 shade의 뜻에 -er을 혼합하여,

shader는 색의 농담, 색조, 명암 효과를 주는 주체 라는 뜻을 가집니다.

 

> 렌더링 파이프라인을 간략하게

쉐이더가 하는 일을 알려면, 쉐이더가 쓰이는 곳을 알아봅시다.

 

<br>

Rendering Pipeline, 렌더링 순서입니다.

일반적인 렌더링 파이프라인의 큰 틀은, 밑의 과정과 같이 이루어져있습니다.

 

**1. 오브젝트 데이터 받아오기**

**2. 정점 쉐이더 (Vertex Shader)**

 \+ 요즘 핫한 테셀레이션이 여기 중간에서 실행. (여기서도 다양한 쉐이더가 있음.)

**3. 래스터라이져 (Rasterizer)**

**4. 픽셀 쉐이더 (Pixel Shader), 프레그먼트 쉐이더 (Fragment Shader)**

 

------

 

하나씩 설명을 넣겠습니다.

 

<br>

**1. 오브젝트 데이터 받아오기**

그래픽 카드는 Vertex로 이루어진 물체의 데이터 값을 받아옵니다.

Vertex는 인덱스 넘버, 포지션, 노멀, 컬러 등의 정보를 가지고 있습니다.

그래픽 카드에서는 정보들을 이용해 버텍스들을 잇고, 삼각형 면을 생성하게 됩니다.



![img](https://blog.kakaocdn.net/dn/btX3Jb/btq0ED4qg3X/nIuj4PXalmUwqyiiEjI6h0/img.png)점 하나하나를 받아 옴.



 

<br>

**2. 정점 쉐이더 (Vertex Shader)**

주된 임무는 각 정점의 공간을 변환하는 것입니다.

3D 물체를 구성하는 정점의 수만큼 실행됩니다.

 

<br>

1) 로컬 좌표계 상태입니다.

자신이 (0, 0, 0) 의 위치값(중심값)을 가집니다.



![img](https://blog.kakaocdn.net/dn/9UMhC/btq0A3v01Mg/IjIZkkB41t20iuqp9xBehK/img.png)



 

<br>

2) 월드 좌표계를 곱합니다

월드의 중심이 (0, 0, 0) 이고, 다른 물체는 여기서 얼마나 떨어져있는가를 표현합니다.



![img](https://blog.kakaocdn.net/dn/b0LEoK/btq0A3isKKK/PBrs99CvEJcpK2s5C9k4M1/img.png)



 

<br>

3) 카메라 행렬을 곱합니다.

카메라의 중심이 (0, 0, 0) 이고 다른 물체들이 여기서 얼마나 떨어져있는가를 표현합니다.



![img](https://blog.kakaocdn.net/dn/HLZz0/btq0AG17ShW/81JR2zNV4rwsMTfkwaOuVK/img.png)



 

<br>

4) 프로젝션 행렬을 곱합니다.

원근감을 부여해줍니다. 먼 곳은 좁혀진 것처럼 버텍스 위치를 조정해줍니다.



![img](https://blog.kakaocdn.net/dn/b6COVA/btq0AHfEhtX/dHohbOvuNTxAe6GkTUimEK/img.png)



<br>

**3. 레스터라이져**

3D 오브젝트가 2D모니터에 보이도록 픽셀이 됩니다.

레스터라이져는 하드웨어 장치입니다.

 

주된 임무는 3D오브젝트가 2D모니터 상에서 어디 픽셀에 찍힐 지를 계산합니다.

픽셀 수 만큼 실행됩니다. (화면 해상도만큼.)



![img](https://blog.kakaocdn.net/dn/bnVM6k/btq0zunNLkc/HJSBsl6M0Rwtk4d3lZbQK1/img.png)![img](https://blog.kakaocdn.net/dn/eczpB9/btq0BDqjZTd/aWuH1Yus3G8vutDCyPwoWk/img.png)



<br>

**4. 픽셀 쉐이더 / 프레그먼트 쉐이더 (Pixel/Fragment Shader)**

모니터까지 넘어온 3D 그래픽 데이터가 본격적으로 픽셀로 찍히게 됩니다.

 

이 픽셀은 파란색으로 칠해야지!!

이 픽셀은 그림자를 받으니 파란색이지만 좀 어둡게 칠해야지!! 요런 느낌입니다.



![img](https://blog.kakaocdn.net/dn/XHWNC/btq0z0fHVkM/RAtOK4CNwf4mGbJOHwJdj0/img.png)





<br>

렌더링 파이프라인 과정은 여기 정리해보았습니다.

[2019/11/28 - [게임 엔진/[Unity\] Engine] - [Unity] Rendering Pipeline 정리 3 (과정

<br>

<br>

#### 참고링크: [[Shader\] 쉐이더(Shader)란? — 민규야 개발하자 (tistory.com)](https://mingyu0403.tistory.com/110)

<br>