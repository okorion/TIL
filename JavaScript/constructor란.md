# 🧀 constructor

**`constructor`** 메서드는 [클래스](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/class)의 인스턴스 객체를 생성하고 초기화하는 특별한 메서드입니다.

## [시도해보기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes/constructor#시도해보기)

<iframe class="interactive is-js-height" height="200" src="https://interactive-examples.mdn.mozilla.net/pages/js/classes-constructor.html" title="MDN Web Docs Interactive Example" loading="lazy" data-readystate="complete" style="box-sizing: border-box; border: 0px; max-width: 100%; width: 531.2px; background-color: var(--background-secondary); border-radius: var(--elem-radius); color: var(--text-primary); height: 513px; margin: 1rem 0px; padding: 0px;"></iframe>

## [구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes/constructor#구문)

```
constructor() { ... }
constructor(argument0) { ... }
constructor(argument0, argument1) { ... }
constructor(argument0, argument1, ... , argumentN) { ... }
```

Copy to Clipboard

## [설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes/constructor#설명)

`constructor`를 사용하면 다른 모든 메서드 호출보다 앞선 시점인, 인스턴스 객체를 초기화할 때 수행할 초기화 코드를 정의할 수 있습니다.

```
class Person {

  constructor(name) {
    this.name = name;
  }

  introduce() {
    console.log(`Hello, my name is ${this.name}`);
  }

}

const otto = new Person('Otto');

otto.introduce();
```

Copy to Clipboard

클래스에 생성자를 정의하지 않으면 기본 생성자를 사용합니다. 아무것도 상속하지 않는 기본 클래스일 때의 기본 생성자는 빈 메서드입니다.

```
constructor() {}
```

Copy to Clipboard

다른 클래스를 상속하는 경우, 기본 생성자는 자신의 매개변수를 부모 클래스의 생성자로 전달합니다.



참고링크: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes/constructor