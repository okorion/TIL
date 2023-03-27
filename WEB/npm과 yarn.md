# npm

![img](https://velog.velcdn.com/images%2Fkysung95%2Fpost%2Fd4342f5a-309d-4a44-8b88-3e3561681133%2Fnpm.png)

> **NPM(Node Package Manager)**은 자바스크립트 언어를 위한 패키지 관리자로, Node.js의 기본 패키지 관리자입니다. 전세계적으로 가장 많은 이들이 사용하고 있는 패키지 관리 툴이죠. 이러한 관리 툴을 이용하여 Node.js로 만들어진 모듈을 웹에서 받아서 쉽게 설치하고 관리해주는 프로그램으로 개발자 입장에서는 단 몇 줄의 command로 기존 공개된 모듈들을 설치하고 활용할 수 있습니다. (Java에서 maven과 비슷한 역할을 한다고 볼 수 있습니다.) 또한 그렇게 설치된 모듈들이 업데이트되었는지를 체크해주는 등 JavaScript로 진행하는 프로젝트를 굉장히 편하게 진행할 수 있도록 도움을 줍니다. command-line client인 npm과 온라인 데이터베이스인 npm registry로 이루어져 있으며, **일반적으로 command-line client를 npm이라고 생각하는데, 실제로 npm에는 npm registry까지 포함되어 있습니다.**

이러한 npm이 없었을 때에는 필요로 하는 기능을 추가하기 위해서 직접 작성하거나 github를 통해 다운로드하여 사용해야 했습니다. 이러한 불편을 해소하기 위해 나타났으며, Node.js를 설치하기만 하면(기본적으로 npm은 Node.js 내에 내장되어 있습니다) 명령어 한 줄로 기능의 추가가 가능합니다.

<br>

### npm 명령어

npm을 사용하기 위해서는 몇가지 명령어를 알아둘 필요가 있는데, 프론트엔드 개발을 위해서 사용하는 npm 명령어는 대표적으로 아래와 같습니다.

- **npm init** : package.json 생성
- **npm install** : package.json 파일 및 해당 종속성에 나열된 모든 모듈을 설치
- **npm install package_name@버전** : 특정 패키지의 특정 버전 설치
- **npm install 주소** : 특정 저장소 내 패키지 설치. 주로 github을 이와 같이 설치합니다.
- **npm install package_name -g** : 옵션. 글로벌로 설치. 로컬의 다른 프로젝트도 이 패키지를 사용 가능하게 됩니다.
- **npm uninstall** : 패키지 삭제 명령어입니다.
- **npm update** : 설치한 패키지들을 업데이트해줍니다.
- **npm dedupe** : 중복 설치된 패키지들을 정리해주는 명령어입니다.

<br>

#### 🙄 package.json이란?

package.json은 프로젝트 정보와 의존성(dependencies)을 관리하는 문서입니다.
우리가 어떤 패키지(오픈소스)를 사용하는지, 어떤 버전을 사용하는지 등을 기록함으로써 어느 곳에서도 동일한 개발 환경을 구축할 수 있게 해줍니다.

```null
// package.json
{
  "name": "yongseong",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.11.4",
    "@testing-library/react": "^11.1.0",
    "@testing-library/user-event": "^12.1.10",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3",
    "web-vitals": "^1.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

<br>

<br>

# yarn

![img](https://velog.velcdn.com/images%2Fkysung95%2Fpost%2F5e1a3b57-a4da-4d97-ab19-6fa1494d46eb%2Fyarn.png)

*그렇다면 이렇게 편리한 NPM이 있는데 yarn이라는 것은 왜 만들어지게 된 것일까요?*

> **yarn**은 페이스북에서 만든 자바스크립트 패키지 매니저입니다. npm과 같은 기능을 수행하죠. 그렇지만 사실 npm과 yarn에 대해 공부해보지 않아도 어느정도 프로젝트 경험이 있으신 분들은 yarn이 조금 더 가볍다는 느낌을 받아보셨을거라 생각해요. 그 이유는 yarn의 탄생 배경에 있습니다.
> yarn은 기본적으로 npm의 단점을 느꼈기에 이를 향상시키기 위해 만들어진 매니저 툴인데, 여기서 말하는 npm의 단점으로는 **속도(performance), 안정성(stability), 보안성(security)** 등이 있습니다.

<br>

**속도(perfomance)**

yarn은 다운받은 패키지 데이터를 캐시(cache)에 저장하여, 중복된 데이터는 다운로드하지않고, 캐시에 저장된 파일을 활용함으로써 이론적으로 npm에 비해 패키지 설치속도가 매우 빠릅니다. 또한 여러개의 **패키지를 설치할 때 병렬로 처리하기 때문에 performance와 speed가 증가** 됩니다. (npm은 순차적)

**안정성(stability)/보안성(security)**

npm은 패키지가 설치될 때 자동으로 코드와 의존성을 실행할 수 있도록 허용했습니다. 이 특징은 편리한 기능이지만 안정성을 위협할 수 있습니다. 특히나 보장된 정책 없이 등록한 패키지가 존재할 수 있다는 점에서 더욱 위험도가 높습니다.
반면 **yarn은 yarn.lock이나 package.json으로 부터 설치만 하며, yarn.lock은 모든 디바이스에 같은 패키지를 설치하는 것을 보장하기 때문에 버전의 차이로 인해 생기는 버그를 방지해줄 수 있습니다.**

<br>

### yarn 명령어

- **yarn init** : package.json 생성
- **yarn or yarn install** : package.json 파일 및 해당 종속성에 나열된 모든 모듈을 설치
- **yarn add package_name@버전** : 특정 패키지의 특정 버전 설치
- **yarn add 주소** : 특정 저장소 내 패키지 설치. 주로 github을 이와 같이 설치합니다.
- **yarn global add package_name** : 옵션. 글로벌로 설치. 로컬의 다른 프로젝트도 이 패키지를 사용 가능하게 됩니다.
- **yarn remove** : 패키지 삭제 명령어입니다.
- **yarn upgrade** : 설치한 패키지들을 업데이트해줍니다.
- **npm dedupe** : 중복 설치된 패키지들을 정리해주는 명령어입니다.

<br>

<br>

# npm? yarn? 무엇을 사용할까?

> 결론부터 말씀드리면 **'각자에게 편한 것을 사용하는 것이 가장 좋지만 만약 둘다 사용해보지 않은 상황이라면 npm을 사용해보는 것을 추천한다.'** 입니다.

제가 yarn을 설명드릴 때 yarn이 npm에 비해 향상된 것들에 대해 말씀드렸는데요. **사실 2016,2017년 이때 기준으로는 yarn이 가시적으로 npm보다 속도나 안정성이 뛰어났습니다. 그렇지만 npm 또한 몇년간 발전을 거듭하며 단점을 많이 보완했기 때문에 현재 npm/yarn의 performance와 stability 차이는 그리 크지 않다고 봐도 무방합니다.(약간 yarn이 우세하긴 합니다.)**
다만 언급한 것처럼 yarn의 병렬적 패키지 설치로 인한 가벼움, 또한 버전의 차이로 인한 버그 방지 등의 기능은 yarn이 npm보다 더 좋은 툴이라고 설명하기 충분한 점이라고 생각합니다.
그렇지만 npm 역시 분명한 장점이 존재합니다. 그것은 사용자 수와 접근성입니다. 아무리 yarn이 좋다고 한들, 원조는 이길 수 없는 법, perfomance 상으로 확연히 yarn에게 뒤쳐지던 때에도 npm은 굳건히 packaged manager 들 중 가장 사용자를 많이 보유하고 있었습니다. 현재도 마찬가지로 가장 많은 사용자를 보유하고 있으며 우수한 접근성이 이러한 현상을 야기한 것으로 보입니다. yarn의 경우는 brew나 npm을 통해 한번 더 설치를 해줘야하는 불편함이 존재하기 때문입니다.

> 각자의 장단점이 뚜렷하고 실질적인 성능에서는 yarn이 근소하게 앞서고 있지만 처음 사용해보시는 분들에게 npm을 추천드리는 이유는 일단 **npm을 직접 사용해보아야 yarn의 필요성에 대해 판가름을 할 수 있다고 생각하기 때문입니다.** 대다수 yarn을 사용하기 시작하신 분들을 보면 npm을 통해 프로젝트를 진행하다가 package들 간의 버전 문제로 인해 에러를 겪어본 경우가 많습니다.
> 필자 본인은 **npm을 사용해봄으로서 직접 이러한 것에 부딪혀보고 yarn이라는 것이 왜 만들어졌는지, 혹은 npm만으로도 충분한 관리가 가능한지 아닌지 그러한 점들에 대해 깊게 생각해볼 수 있고, 이는 개발자 본인에게 좋은 경험이 될 것이라고 생각합니다.**

감사합니다.

<br>

<br>

참고링크: [[개발상식\] npm과 yarn (velog.io)](https://velog.io/@kysung95/개발상식-npm과-yarn)