## 🍨 TypeScript와 AST

## 🚍 1. Typescript와 AST

최근 아는 지인으로부터 typescript의 interface는 어떤 작동을 하느냐는 물음에 이것저것 찾아보다가 알게 된 내용을 정리해본다.

Javascript 코드는 Scanner에 의해 분해되어 가장 작은 의미론적 단위인 "Token" 의 모음이 된 후, Parser에 의해 AST로 변환된다.

![img](https://user-images.githubusercontent.com/58500558/167062763-975a9dca-eedf-474b-bc6c-3c484b53102a.png)

> AST란 자바스크립트 코드를 실행단위인 바이트코드로 변경시키기 위한 중간 자료 구조이다.

이 AST를 탐색하여 오류점이 있는지 확인하는 도구가 바로 ES lint이다.

![img](https://user-images.githubusercontent.com/58500558/167062970-a79c49eb-79a1-4f13-b01d-4afc6abe30f9.png)

> ESlint의 작업은 위에 보이는 traverse 단계에 해당한다.

traverse 단계가 끝마쳐지면, Babel이 주도되어 이루어지는 2단계를 겪는데 첫째로 Manipulate 과정에서는 예를들어 "debugger"나 주석과 같이 프로덕션 모드에서 사용되지 않을 코드들을 정돈하는 작업을 진행한다.

그리고 마지막으로 code generation 단계에서 plugin들을 통한 기존 코드를 호환에 맞게 변경하는 작업들 ( ex let => var ) 을 실행한 뒤, 이것을 바이트코드로 변경시켜 자바스크립트 엔진이 실행시킨다.

하지만, Typescript는 해당 과정이 조금 다르다.
타입스크립트는 자신의 구문분석을 위한 타입스크립트만의 AST를 만든다는 특징이 있다.

![img](https://user-images.githubusercontent.com/58500558/167064919-d7de0d2f-c73c-4809-a5c8-d60acbe389ea.png)

위에서 볼 수 있듯, typescript 패키지는 자신만의 AST를 형성해서 타입 검사기를 통해 타입을 체킹하고, 다시 JS파일을 만들어 기존의 javascript 파싱 과정을 이어나간다. 이 때 만들어지는 js 파일에는 당연히 typescript 와 관련된 타입구문들이 모두 제거된 상태이다.

즉, 다시말하자면 typescript의 타입은 첫 1~3단계에서 typescript AST를 만드는 동안 메모리를 점유하여 타입들을 등록하고 평가하는 과정을 거친다.

## 🚍 2. 타입스크립트의 장점

타입스크립트는 컴파일 시점에서 AST의 분석을 통해 타입을 정적으로 추론함으로 자바스크립트의 동적 타입 변환에 의한 에러로부터 보완될 수 있다는 장점이 존재한다.

예를들어,

```js
let num = 1 + [1] 
// 위의 내용은 자바스크립트에서는 압묵적 타입변환으로 인해 [1] => 1이 되어 '11' string 값이 되어버린다.
```

개발을 하면서 변수의 타입이 어떠한지 정해지지 않은 한, 런타임 시점에서 이런 암묵적인 변동으로 인한 에러는 언제나 마주칠 수 있다.

하지만 타입스크립트를 이용하면

```ts
let name : number = 1 + [1] 
// Operator '+' cannot be applied to types 'number' and 'number[]'
// 이렇게 컴파일 시점에서 짐작가능한 에러를 잡아준다
```

# 🚍 reference

[What is AST](https://www.youtube.com/watch?v=C06MohLG_3s)
[generate typescript AST](https://ts-ast-viewer.com/#code/JYOwLgpgTgZghgYwgAgHJwLYoN4ChkHJgCeADigFzIDKYUoA5gNy4C+QA)



<br>

<br>

#### 참고링크: [Typescript와 AST (velog.io)](https://velog.io/@chltjdrhd777/Typescript와-AST)

<br>