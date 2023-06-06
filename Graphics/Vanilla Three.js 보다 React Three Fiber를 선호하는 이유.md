## 🧀 Vanilla Three.js 보다 React Three Fiber를 선호하는 이유

만약 당신의 제품이 React를 기반으로 하고 있고, 그 제품에 Three.js를 쓸 생각이라면 자신 있게 React Three Fiber(이하 r3f)를 추천한다. React Fiber에 대한 깊은 이야기는 아니고, 오로지 생산성과 안정성에 대한 이야기가 될 것이다. r3f는 Poimandres라는 크리에이터 그룹이 운영하고 있는 라이브러리다. r3f는 React에서 Three.js를 간편하게 활용할 수 있도록 다양한 API들을 제공하며, 나의 프론트엔드 3D 작업 효율을 눈에 띄게 끌어올려 준 고마운 라이브러리 되겠다. 무엇이 얼마나 좋아졌는지, 아래의 4가지 꼭지로 설명해볼까 한다.

1. 코드 작성이 간편하며, 가독성도 높다.
2. 필요로 하게 되는 대부분의 기능들이 이미 작성되어 있다.
3. 메모리 관리로 골치 아플 일이 없다.
4. 제한 없이 확장할 수 있다.

<br>

## 코드 작성이 간편하며, 가독성도 높다.

Three.js로 제품을 만들어본 사람들은 충분히 공감할만한 이야기인데, 생각보다 첫 번째 정육면체를 만드는 일이 쉽지 않다. 씬(Scene)에 정육면체 형태의 메시(Mesh)를 추가하더라도, 적절한 조명(Light)과 카메라(Camera)를 셋팅하지 않거나, 리사이즈 로직을 적절한 곳에 추가하지 않으면, 화면이 부서지는 일이 빈번하게 일어난다. 게다가 코드의 양도 적지 않아, 피로도가 급격하게 올라간다

```
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const ambientLight = new THREE.AmbientLight( 0xFFFFFF );
scene.add( ambientLight );

const pointLight = new THREE.PointLight( 0xFFFFFF, 1, 100 );
pointLight.position.set( 10, 10, 10 );
scene.add( pointLight );

const geometry = new THREE.BoxGeometry( 1, 1, 1 );
const material = new THREE.MeshStandardMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );

renderer.render( scene, camera );
```

그러나, r3f는 다르다. 커스텀 태그와 컴포넌트로 구성되기 때문에, 작성이 간편하며 구조를 파악하기도 쉽다. React에 익숙한 개발자라면 초반 학습 비용이 매우 적어 거침없이 3D 그래픽을 만들 수 있다.

```
import {Canvas} from '@react-three/fiber';

function MyRenderer(){
    return (
        <Canvas>
            <ambientLight />
            <pointLight position={[10, 10, 10]} />
            <mesh position={[0,0,0]}>
                <boxGeometry args={[1,1,1]} />
                <meshStandardMaterial color={0x00ff00} />
            </mesh>
        </Canvas>
    )
}
```

조건에 따라 엘리먼트를 동적으로 추가하거나 삭제하는 일도 간편하게 수행할 수 있다. 또한, 기본적인 raycaster 코드가 이미 구현되어 있어, 마치 DOM을 다루듯이 3D 요소들을 핸들링할 수도 있다.

<br>

## 필요로 하게 되는 대부분의 기능들이 이미 작성되어 있다.

Poimandres는 @react-three/drei와 @react-three/postprocessing이라는 라이브러리들을 별도로 제공하고 있다.

첫 번째 라이브러리인 drei는 r3f에 물려서 쓸 수 있는 헬퍼 콜랙션이다. drei는 화면 구성부터 메모리 관리에 이르기까지 거의 대부분의 기능들을 미리 구현하여 제공하고 있다. 3D 요소의 바운더리를 한 줄로 계산해내거나, 카메라나 줌 설정을 동적으로 핸들링하는 생산성 기능은 물론이고, BVH와 같은 최적화 기능까지 쓰기 좋게 제공한다.

두 번째 라이브러리인 postprocessing은 말 그대로 화면의 후처리를 담당한다. 가볍게 사진 필터를 떠올리면 된다. postprocessing은 SSAO와 같이 볼륨감을 강조해주는 알고리즘도 손쉽게 적용할 수 있도록 제공하고 있는데, 이를 활용하면 빛과 그림자만으로는 부족한 3D의 입체감을 단시간에 크게 향상시킬 수 있다.

![SSAO example\n적용 전: 왼쪽 / 적용 후: 오른쪽](https://www.mornhee.works/_next/image?url=https%3A%2F%2Ffirebasestorage.googleapis.com%2Fv0%2Fb%2Fblog-mornhee.appspot.com%2Fo%2FPFTbCu0YCsfKNmydmoV1%252Fssao.png%3Falt%3Dmedia%26token%3Dd3404ec4-9cf3-4dcc-9e38-ba91b27f8f76&w=2048&q=75)©learnopengl.com

<br>

## 메모리 관리로 골치 아플 일이 없다.

Three.js는 WebGL을 기반으로 하는 3D 그래픽 라이브러리다. 단순히 javascript의 메모리 관리 방식을 생각하며 작업하는 경우, 어느 순간부터 맥북이 뜨겁게 달아오르거나, 브라우져가 꺼지는 문제에 봉착하게 될 것이다. 특히 React 컴포넌트 안에서 Three.js를 사용하는 경우, 컴포넌트가 umount되더라도 GPU에 쌓인 버퍼 데이터들은 그대로 유지되기 때문에, 리렌더링이 일어날 때마다 메모리를 무한정 할당하는 일까지 일어난다. 이를 방지하기 위해서는 GPU를 차지하고 있는 버퍼 데이터들을 직접 제거해줄 필요가 있는데, 간혹 깜빡하거나 놓치는 경우가 있다. 메모리 누수의 시작인게다. 그러나 다행히 r3f의 각 엘리먼트는 unmount될 때마다 자동으로 메모리를 비워주는 로직을 포함하고 있다. 덕분에 특수한 경우가 아닌 이상, 이에 대해 신경 쓸 필요가 없다. react-native를 사용할 때 네이티브 코드에 대한 관리 포인트가 줄어드는 것과 마찬가지라고 생각하면 된다.

<br>

## 제한 없이 확장할 수 있다.

r3f를 이용해 기능을 잘 구현해두더라도, 추후 더 많은 기능과 미세한 핸들링이 필요해졌을 때, 모든 것을 새로 짜야하는 것이 아닐까 하는 노파심이 들 것이다. 이는 javascript 라이브러리를 2차적으로 랩핑한 React 라이브러리를 채택했을 때 자주 일어나는 일이다. 나 역시 비슷한 상황을 경험한 적이 있어서, 처음엔 의심 가득한 시선으로 r3f를 바라보았다. 하지만 그럴 필요가 없었다. r3f는 순수한 Three.js로 작성한 코드도 사용할 수 있도록 기능을 열어두고 있다.

```
const pureThreeJsGeometry = new THREE.BufferGeometry( ... );
return (
    <mesh>
        <primitive attach="geometry" object={pureThreeJsGeometry} />
        <meshStandardMaterial color={0xff3300} />
    </mesh>
)
```

Three.js는 빠른 속도로 변화하고 있고, r3f 역시 그에 대해 민첩하게 대응하고 있다. 업데이트 시 다른 패키지들보다 많은 주의가 필요하긴 해도, 제공하는 장점이 분명한 만큼 r3f의 채택을 적극적으로 권해본다. Three.js의 기초적인 사용법만 숙지하고 있다면 망설일 필요가 없다. 지금 바로 만들어보자.

<br>

<br>

#### 참고링크: [Vanilla Three.js 보다 React Three Fiber를 선호하는 이유 (mornhee.works)](https://www.mornhee.works/blog/post/three-js-vs-react-three-fiber)

<br>

