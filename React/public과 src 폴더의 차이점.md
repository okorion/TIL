## 🌆 public과 src 폴더의 차이점

`npx create-react-app my-app`을 터미널에 입력하면 자동으로 public 폴더와 src 폴더가 생성된다.
각 폴더에 넣는 파일에 차이가 있는데!
두 폴더에 무슨 차이가 있을까?

<br>

### 📁 public : 앱이 컴파일될 때 사용하지 않는 모든 것

- 앱을 컴파일하는 데 필요하지 않은 요소들.
- 절대경로 사용이 가능해진다!
- import 해올 일이 있을 때, `../../`이렇게 상대경로로 써주지 않아도 되고, 그냥 파일명 써주면 가능하다!
- 정적파일을 담는 곳. 사용자가 직접 웹브라우저상으로 볼 수 있는 index.html같은 파일들, image 파일들이 담긴다.
- 경로를 동적으로 참조해야 할 때 퍼블릭 폴더를 쓴다
  (You have thousands of images and need to dynamically reference their paths. 상대경로로 쓰면 경로가 하나 바뀔 때마다 다 수정되기 때문에인가?)

<br>

### 📁 src : 앱이 컴파일 될 때 사용하는 모든 것

- 개발하면서 작업하는 파일 대부분을 넣는 폴더(index.js, 그 외 컴포넌트 같은 js파일, css파일 등)

예를 들어, 컴포넌트 안에서 사용하는 이미지는 src폴더에 있어야 하지만 파비콘과 같이 앱 밖에서 사용하는 이미지는 public 폴더에 있어야 한다.

<br>

<br>

#### 참고링크: [[React\] public폴더 src폴더 어디에 넣어야 되는걸까? / react에서 img불러오기 (velog.io)](https://velog.io/@daeun/React-public폴더-src폴더-어디에-넣어야-되는걸까)

<br>