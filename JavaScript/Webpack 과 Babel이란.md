## 🛒 Webpack 과 Babel이란 무엇일까?

# ✔ webpack

> 웹팩은 여러개 파일을 하나로 합쳐주는 모듈 번들러이다. (오픈 소스 자바스크립트 모듈 번들러)

웹팩은 기본적으로 모듈을 지원하고 파일 분할 기능(원하는 코드만 따로 분리해서 하나의 파일로 압축이 가능하다), css loader기능, jsx변환 작업도 해준다.

여러개로 나눠진 자바스크립트 파일을 html이 실행할 수 있는 하나의 자바스크립트 파일로 합쳐준다!

왜 웹팩을 사용할까??
많은 파일들을 다운받아와야 해 네트워크 부하가 커지고 느려지고,
같은 이름의 변수나 함수로 충돌 가능성이 있다.
->해결 위해 번들러 등장

> 번들러를 사용하면 여러개 파일을 하나로 묶어주기 때문에 네트워크 접속의 부담을 줄여 더 빠른 서비스를 제공할 수 있다.

# ✔ Babel

대표적인 트랜스파일러로는 '바벨'이 있다.

> 트랜스파일링이란 특정 언어로 작성된 코드를 비슷한 다른 언어로 변환시키는 것이다. 이를 해주는 것이 트랜스파일러이다. (오픈 소스 자바스크립트 트랜스컴파일러)

트랜스파일링이 왜 필요할까?

> 모든 브라우저가 ES6의 기능(최신기능)을 제공하지 않기 때문에 ES5코드(구기능)으로 변환시키는 과정이 필요하기 때문이다.

### npm install dependency

적용하고자 하는 폴더에 webpack과 webpack-cli를 설치해준다.

```null
npm init
npm i react react-dom
npm i -D webpack webpack-cli  //-D는 개발환경에서만 쓰인다는 것
```

바벨설치

```javascript
npm i -D @babel/core @babel/preset-env @babel/preset-react babel-loader
```

babel-loader는 바벨이랑 웹팩을 연결해준다.
preset-env는 자동으로 옛날 브라우저들을 지원해준다.

## Webpack 사용예시

### WordRelay.jsx 파일

```javascript
const React = require('react');//npm에서 react 불러와주기
const {Component} = React;

class WordRelay extends Component {
    state = {
        text:'Hello, webpack',
    };
    render(){
        return <h1>{this.state.text}</h1>
    }
}

module.exports = WordRelay;
//쪼갠 컴포넌트를 외부에서도 사용 가능하도록 만들어줌
```

### client.jsx 파일

```js
const React = require('react');
const ReactDom = require('react-dom');

//필요한 것만 가져와
const WordRelay = require('./WordRelay');

ReactDom.render(<WordRelay/>,document.querySelector('#root'));
```

client.jsx파일에 WordRelay.jsx파일을 합쳐줌.

### webpack.config.js

```js
const path = require('path');

module.exports = {
    name: 'wordrelay-setting',
    mode: 'development', //실서비스에서는 production
    devtool: 'eval', //production일때는 hidden-source-map사용
    resolve:{
        extensions:['.js','.jsx'] //js나 jsx파일 확장자 있는지 찾는다.
    },

    //파일 합치기
    //두가지 파일을 합쳐서 app.js파일로 만들어 html이 실행할 수 있도록 만들어준다.
    
    entry: {
        app: ['./client'],
    }, //입력

    module: {
        rules: [{
            test: /\.jsx?/,
            loader:'babel-loader', 
            //js나jsx파일에 바벨로더를 적용해 최신문법이 옛날 브라우저에서도 돌아갈 수 있도록 해준다.
            options:{
                presets:['@babel/preset-env','@babel/preset-react'],
            },
        }],
    },

    output : {
        path: path.join(__dirname,'dist'),
        filename: 'app.js',
    }, //출력
}
```

> 결과 : 여러개의 파일을 합쳐 현재 폴더 내에 dist폴더가 생기고 그 안에 app.js라는 하나의 파일이 생성된다.

### webpack 속성들

- mode : 모드에 따라 번들링 최적화를 진행한다. (development/production)
- entry : 웹팩에서 웹 자원을 변환하는 데 필요한 진입점이자 자바스크립트 파일 경로. 번들링 시작점.
- module : 웹팩에서 사용하는 모듈에 대한 설정/ 웹팩 로더 설정. rules 로 loader를 설정한다.
- ouput : 웹팩을 돌리고 난 결과물의 파일 경로. 번들링 결과물 경로 및 이름을 지정한다.
- plugins : 기본적인 동작에 추가적인 기능을 제공한다. 확장 프로그램 같은 것.
- target : 웹팩에서 번들링 결과를 어떤 목표로하는지 설정한다. (web, webworker, es5, es2020, node0
- devtool : 소스맵 생성 관련 설정(source-map, inline-source-map 등)

> 전체적인 과정으로 entry에 있는 파일에 module적용하고 추가적으로 plugins사용해 output으로 출력한다.

### webpack build하기

```null
npx webpack
//or
npm run dev
```

### index.html

```html
<!-- 웹팩사용 -->
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>제목</title>
    </head>
    <body>
        <div id="root"></div>
        <script src="./dist/app.js"></script>
    </body>
</html>
```

여러개의 js파일이 아닌 app.js 하나의 파일에서 실행된다.

### 자동으로 build 해주는 방법

코드르 수정할때 마다 build를 수행해주지 않으면(수동으로 할 때) 에러가 날 수 있다.
이때 자동으로 build를 해주어 이를 해결할 수가 있다.

> 웹팩데브서버와 핫리로딩(webpack-dev-server, react-refresh, react-refresh-webpack-plugin)

```js
//리액트 리프레쉬 사용방법
//설치
npm i react-refresh @pmmmwh/react-refresh-webpack-plugin -D

npm i -D webpack-dev-server //개발용 서버 하나 필요
//pakage.json에서 명령어 변경
"scripts": {
    "dev" : "webpack serve --env development"
  },
//webpack.config.js
const path = require('path');
const RefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');//추가

//...
//plugins추가
module: {
        rules: [{
            test: /\.jsx?/,
            loader:'babel-loader', 
            options:{
                presets:[
                    ['@babel/preset-env',{
                        targets:{
                            browsers : ['> 1% in KR'],
                           
                        },
                    }],
                    '@babel/preset-react'
                ],
                plugins:[
                    '@babel/plugin-proposal-class-properties',
                    'react-refresh/babel',//추가됨!
                ],
            },
        }],
    },
    plugins:[
        new RefreshWebpackPlugin()
    ],//추가됨!
    output : {
        path: path.join(__dirname,'dist'), //__dirname은 현재폴더(lecture)
        filename: 'app.js',
        publicPath:'/dist',//추가, publicPath는 가상경로같은것
    },
    devServer : {
        publicPath:'/dist/',
        hot:true,
    },//추가
      
```

설정을 해주고 `npm run dev`를 실행하면 Project is running at http://localhost:8080/ 메세지가 뜨고 이제 매번 수동으로 빌드할 필요없이 웹팩 빌드가 자동으로 이뤄진다.



<br>

<br>

#### 참고링크: [Webpack 과 Babel이란 무엇일까? (velog.io)](https://velog.io/@dbsbest10/Webpack-과-Babel이란-무엇일까)

<br>