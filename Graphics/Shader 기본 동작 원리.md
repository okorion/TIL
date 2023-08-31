# 🪐 Shader기본 동작 원리

01.쉐이더 기본동작 원리

![Imagem de capa](https://gasbebe.github.io/images/bg.jpg)

# 3D Graphics Rendering Pipeline

![pipeline](https://gasbebe.github.io/images/pipeline.png)

기본적인 렌더링 파이프라인 (조금 씩 GPU마다 다를수있습니다) 동작원리

------

# Shader

**쉐이더란 화면에 출력할 픽셀의 위치와 색상을 계산하는 함수**

**쉐이더는 픽셀의 농담, 색조, 명암을 결정한다.**

# Vertex Shader(정점 쉐이더)

![vertex-shader-anim](https://gasbebe.github.io/images/vertex-shader-anim.gif)

Vertex Shader 는 3D 모델의 각 버텍스에서 실행되는 프로그램입니다. 많은 경우 버텍스 셰이더는 특별히 흥미로운 동작을 하지는 않습니다. 여기서는 버텍스 위치를 오브젝트 공간에서 이른바 “클립 공간”으로 변환하기만 합니다. GPU 가 오브젝트를 화면에 래스터화하기 위해 클립 공간을 사용합니다. 프래그먼트 셰이더에서 텍스처를 샘플링하기 위해 필요로 합니다.

**출처 : webglfundamentals.org**

------

# Rasterizer(레스터라이저)

래스터라이저는 뷰에 없는 기본 요소를 잘라내고, PS(픽셀 셰이더) 단계에 대해 기본 요소를 준비하고, 픽셀 셰이더를 호출하는 방법을 결정합니다.

화면에 출력할수 있게 이미지화 하는 단계

정점의 위치를 계산을 통해 삼각형들을 픽셀로 레스터라이징하는 한다.

레스터라이징 부분은 GPU 내부에서 자체 구현돼 프로그래밍할 수 없어 볼 수 없다.

------

# Fragment Shader(프래그멘트 쉐이더)

![fragmentAnim](https://gasbebe.github.io/images/fragmentAnim.gif)

Fragment Shader는 오브젝트가 화면에서 차지하고 있는 모든 픽셀마다 실행되는 프로그램이며 보통 각 픽셀의 컬러를 계산하고 출력하기 위해 사용됩니다. 화면에는 보통 수백만 개의 픽셀이 있으며 프래그먼트 셰이더는 이 모든 픽셀에 대해 실행됩니다! 프래그먼트 셰이더를 최적화하는 것은 전반적인 게임 성능에 있어 매우 중요한 부분입니다.

**출처 : webglfundamentals.org**

------

# Geometry Shader(지오메트리 쉐이더)

Geometry Shader는 GPU상에서 동적으로 프리미티브(Primitive 메쉬를 구성하는 기본 도형 : ex 삼각형)의 변환, 생성, 삭제 등이 가능한 프로그래머블 쉐이더 중 하나입니다.

GPU상에서 메쉬를 좀 더 자유롭게 변환처리를 할 수 있도록 DX10이나 OpenGL3.2부터 추가된 기능이 Geometry Shader입니다. OpenGL에서는 Primitive Shader라고 부르기도 합니다

- 렌더링 파이프라인
  - 렌더링 파이프라인 상에서는 Vertex Shader 다음, Fragment Shader나 래스터라이즈 처리전에 위치합니다. 즉 Fragment Shader안에서는 Geometry Shader에서 동적으로 생성한 정점과 Vertex Shader에 전달된 원래의 정점을 구별하지 않고 처리합니다.

------

기본적인 기능 : 색깔 바꾸기, 텍스쳐링, 색상합성, 버텍스 컬러, 버텍스 애니메이션, 프레넬, 노이즈맵

텍스쳐 uv, 스케일링, 맵핑 위치 바꾸기, 텍스쳐 마스킹, 렌더 텍스쳐, 그림자,

------

# Semantic(시멘틱)

시멘틱이란 어떤 데이터를 받을지 정하는 문자열이다.

##### Vertex Shader Semantic

| 입력            | 종류                             | 타입   |
| --------------- | -------------------------------- | ------ |
| BINORMAL[n]     | Binormal(종법선)                 | float4 |
| BLENDINDICES[n] | Blend indices                    | uint   |
| BLENDWEIGHT[n]  | Blend weights                    | float  |
| COLOR[n]        | Diffuse and specular color       | float4 |
| NORMAL[n]       | Normal Vector(법선)              | float4 |
| POSITION[n]     | Vertex position in object space. | float4 |
| POSITIONT       | Transformed vertex position.     | float4 |
| PSIZE[n]        | Point size                       | float  |
| TANGENT[n]      | Tangent(접선)                    | float4 |

| 출력          | 종류                                                         | 타입   |
| ------------- | ------------------------------------------------------------ | ------ |
| COLOR[n]      | Diffuse or specular color                                    | float4 |
| FOG           | Vertex fog                                                   | float  |
| POSITION[n]   | Position of a vertex in homogenous space. Compute position in screen-space by dividing (x,y,z) by w. Every vertex shader must write out a parameter with this semantic. | float4 |
| PSIZE         | Point size                                                   | float  |
| TESSFACTOR[n] | Tessellation factor                                          | float  |
| TEXCOORD[n]   | Texture coordinates                                          | float4 |

##### Pixel Shader Semantics

| 입력        | 종류                                                         | 타입   |
| ----------- | ------------------------------------------------------------ | ------ |
| COLOR[n]    | Diffuse or specular color.                                   | float4 |
| TEXCOORD[n] | Texture coordinates                                          | float4 |
| VFACE       | Floating-point scalar that indicates a back-facing primitive. A negative value faces backwards, while a positive value faces the camera. | float  |
| VPOS        | The pixel location (x,y) in screen space. To convert a Direct3D 9 shader (that uses this semantic) to a Direct3D 10 and later shader, see | float2 |

| 출력     | 종류         | 타입   |
| -------- | ------------ | ------ |
| COLOR[n] | Output Color | float4 |
| DEPTH[n] | Output depth | float  |

VFACE : 렌더링된 면이 앞면인지 뒷면인지 판별

## System Value Semantic

SV_ 접두사가 붙은 시멘틱, System Value DX10의 새로운 기능 입니다

일반적이 예로는 래스터 라이저 단계에서 해석되는 SV_POSITION이 있습니다. 시스템 값은 파이프 라인의 다른 부분에서도 유효합니다.

SV_Position은 출력뿐만 아니라 정점 셰이더에 대한 입력으로 지정할 수 있습니다.

픽셀 쉐이더는 SV_Depth 및 SV_Target 시스템 값 의미로 매개 변수에 쓸 수 있습니다.

다른 시스템 값 (SV_VertexID, SV_InstanceID, SV_IsFrontFace)은 특정 값을 해석 할 수있는 파이프 라인의 첫 번째 활성 셰이더에만 입력 할 수 있습니다. 그 후에 셰이더 함수는 그 값을 후속 단계로 전달해야합니다.

SV_Depth : 깊이, SV_Position : 위치, SV_Target : 색깔

##### Mapping to Direct3D 9 Semantics

| Direct3D 10 Semantic | Direct3D 9 Semantic |
| -------------------- | ------------------- |
| SV_Depth             | 깊이                |
| SV_Position          | 위치                |
| SV_Target            | 색상                |

```
float4 psMainD3D9( float4 screenSpace : VPOS ) : COLOR
{
  // code here  DX9 version
}
     
float4 psMainD3D10( float4 screenSpace : SV_Position ) : COLOR
{
  // code here DX10 version
}
```

[마이크로소프트 세이더 시멘틱](https://docs.microsoft.com/ko-kr/windows/desktop/direct3dhlsl/dx-graphics-hlsl-semantics#vertex-shader-semantics)

심화 내용

# Base Rendering PipeLine

------

![deeppipeline.PNG](https://github.com/Gasbebe/Practice/blob/master/Image/shader/deeppipeline.PNG?raw=true)

프로그램이 실행일 될때. 사용한 리소스를 저장장치에서 불러와 램에 저장

cpu에서 렌더링상태와 메쉬들을 커맨드버퍼에 Queue함

![cpu2gpu.png](https://github.com/Gasbebe/Practice/blob/master/Image/shader/cpu2gpu.png?raw=true)

![cpu2gpu2.png](https://github.com/Gasbebe/Practice/blob/master/Image/shader/cpu2gpu2.png?raw=true)

gpu는 커맨드 버퍼에 있는 메쉬, 렌더링상태 명령을 순차적으로 실행, shader에 정의되어 있다.

gpu처리방식은 만드는 회사마다 command queue의 처리방식은 다를수 있다.

------

# GPU작동방식

[vulkan work](https://www.reddit.com/r/vulkan/comments/2xvhp3/potential_bottleneck_in_single_command_buffers/)

[modern gpu work](https://traxnet.wordpress.com/2011/07/18/understanding-modern-gpus-2/)

[dx gpu work](https://docs.microsoft.com/en-us/windows/desktop/direct3d9/state-blocks-save-and-restore-state)

```
#pragma vertex vert
#pragma fragment frag
#pragma multi_complie_fog //안개 효과 동작
```

# Post Processing

후처리 효과는 기본적으로 이미지 효과 셰이더다. 이미지 효과 셰이더는 현재 화면의 매 픽셀마다 적용된다.

화면이 아닌 별도의 버퍼에 렌더링한다고 가정하는 것을 유니티에서는 렌더러 텍스처라도 한다.

- 물리 기반 셰이딩에서는 후처리 효과의 가장 중요한 사용처는 톤 매핑이다.

#### 후처리 효과 설정

- Scene Camera
- Camera Component
- excute shader

```
[RequireComponent (typeof(Camera))]
[ExecuteInEditMode]

public Shader cuShader;
private Metarial metarial;

void Start(){
    
}

void Update(){
    if(GetComponent<Camera>().enabled)
        return;
}
//객체 공간의 방향을 취해 월드 공간에서의 방향 값으로 변환 해준다.
float3 UnityObjectToWorldDir(in float3 dir) 

//객체 공간의 노멀을 취해 월드 공간에서의 노멀 값으로 변환해준다. 빛을 계산하는데 유용
float3 UnityObjectToWorldNormal(in float3 norm)
    
//월드 공간에서의 정점 위치를 취해 월드 공간에서의 뷰의 방향을 반환한다. 빛을 계산하는 유용
float3 UnityWorldSpaceViewDir(in float3 worldPos)
    
//월드 공간에서의 정점 위치를 취해 월드 공간에서의 빛의 방향을 반환한다 빛을 계산하느데 유용
float3 UnityWorldSpaceLightDir(in float3 worldPos)
    
```