## 🥄 자바스크립트 AOP 맛보기

## AOP(Aspect Oriented Programming)가 뭔데?

자바스크립트 개발 이야기에서 AOP는 생소한 주제이다. 보통 AOP 개념을 설명할 때 대표적으로 **Cross-cutting Concern** 이라는 말을 한다. 직역하자면 **횡단 관심사** 라고할 수 있겠으나, 조금 더 쉽게 얘기하자면 *"로그를 남겨야 할 곳은 여기, 저기, 그리고 또 저기가 되겠군"*, *"사용자 입력을 받는 이~러한 부분들에서는 유효성을 검증해야 해"* 라고 표현할 수 있는 **공통된 관심사** 정도로 표현할 수 있겠다.

## 아래의 예제를 먼저 살펴보자

```js
class BookCollection {
    ...
    getByISBN(isbn) {
        return this.get({
            isbn: isbn
        }).then(book => book.name)
            .catch(error => null);
    }
    ...
}
```

AOP가 적용될 수 있는 사례를 살펴보기 위해 `BookCollection`에서 `Book`을 가져오는 예제를 적어놓았다. ISBN으로 책 이름을 가져오는 간단한 코드이다. 그러면 이제 이 코드에 로그를 추가해보면 아래처럼 될 것이다.

```js
class BookCollection {
    ...
    getNameByISBN(isbn) {
        return this.get({
            isbn: isbn
        }).then(book => {
                Logger.info(`Retrieving book ${isbn} - ${book.name} has been succeed`);
                return book.name;
            })
            .catch(error => {
                Logger.error(`Retrieving book ${isbn} has been failed. ${JSON.stringify(error)}`);
                return null;
            });
    }
    ...
}
```

개발자의 할 일은 이렇게 간단히 끝날 리 없다. 여기에 더해서 캐시, 유효값 검증 등을 더 추가해보면 코드는 어떤 모양이 될까? `then().then().then()` 이 몇개 더 추가될 것 같다. 이런 식으로 점점 길어지는 코드를 보고 있자면, 나는 오로지 책 정보 하나를 가져오고 싶었을 뿐인데 배보다 배꼽이 커진 상태는 이미 한참 전이다. 이제는 클래스의 이름이 BookCollection이 맞는지도 의문이 들기 시작한다. 밥 삼촌은 한 클래스에서 하나씩만 신경 쓰라고 했는데 이래도 되는 걸까. 모양이 전혀 마음에 들지 않으니 이번에는 클래스를 나눠서 보기 좋게 바꿔보자.

```js
class BookCollection extends Collection {
    ...
    getNameByISBN(isbn) {
        return this.get({
            isbn: isbn
        }, {
            cache: true,
            onSuccess: 'name'
            onFail: null,
            log: {
                message: 'Retrieving Book {} - {} has been succeed',
                params: ['isbn', 'name'],
                level: 'info'
            },
            ...
        });
    }
    ...
}
```

이것이 정말 나아진 것일까. 물론 우리는 위의 예제보다 더 나은 해결 방법을 찾을 수도 있겠지만, 결국에는 긴 이름의 클래스, 복잡한 상속관계 혹은 가독성이 조금 더 나아진 정도로 만족해야 할 것이다.

## AOP를 쓰면 조금 나아지나

아래의 코드는 [aspect.js](https://github.com/mgechev/aspect.js)라는 라이브러리에서 사용하는 문법을 따라 작성했다. 아마도 자바 개발자들에게 더 익숙한 모양이라 생각한다. 생소해 보이는 분들이라도 직관적으로 *"아! BookCollection.getNameByISBN 호출 이후에 로그를 남기려는 것이로군!"* 하고 유추할 수 있으면 된다. 이 글의 목적은 해당 라이브러리의 소개에 있지 않으므로 이런 식으로 분리할 수 있다는 것만 이해하고 넘어가자.

```js
class LoggerAspect {
    ...
    @afterMethod({
        methodNamePattern: /^getNameByISBN$/,
        classNamePattern: /^BookCollection$/
    })
    afterGetNameByISBN(meta) {
        let result = meta.method.result;
        Logger.info(`Retrieving ${result.isbn} - ${result.name} has been succeed`);
    }
    ...
}

@Wove
class BookCollection {
    ...
    getNameByISBN(id, article) {
        return this.get({
            isbn: isbn
        }, {
            cache: true,
            onSuccess: 'name'
            onFail: null
        });
    }
    ...
}
```

한결 나아 보이지 않는가? `BookCollection`은 데이터를 가져오는데 집중하고 있고, 로그는 완벽히 분리된 클래스에서 수행하고 있다.
그러면 이번에는 `CacheAspect`도 추가해보자.

```js
class CacheAspect {
    ...
    @beforeMethod({
        methodNamePattern: /^get.*/,
        classNamePattern: /^[Book|User]Collection$/
    })
    beforeGet(meta, args) {
        let key = `${meta.name}:${args.join()}`;
        let method = meta.method;
        method.proceed = true;
        if (this.cache.hasOwnProperty(key)) {
            method.result = this.cache[key];
            method.proceed = false;
        }
    }
    ...
}

@Wove
class BookCollection {
    ...
    getNameByISBN(id, article) {
        return this.get({
            isbn: isbn
        }, {
            onSuccess: 'name'
            onFail: null
        });
    }
    ...
}
```

오! `BookCollection`에 역할과 무관한 코드가 줄어들었고, 본연의 역할이 뚜렷이 보인다. 이런 식으로 Aspect를 늘려가면 된다. 그리고 Aspect가 얼마나 많이 늘어나든 `BookCollection`에는 자신의 역할을 위한 코드만이 존재하게 될 것이다. 더불어 위에서 이름 패턴을 `/^get.*/`식으로 주어 여러 클래스와 메소드들에 적용될 수 있음을 주시하자. `Collection`클래스들이 혹은 공통된 동작을 수행하고 싶은 더 많은 클래스들이 존재한다 하더라도, 코드 한줄 늘이지 않고 모두 적용 시켜줄 수 있다. 이를 처음에 설명한 개념대로 다시 얘기하자면 `Collection`클래스들의 **Cross-cutting Concern** 에 해당하는 로깅, 캐싱 등을 분리했다 하겠다. 이쯤에서, 이런 식으로 정말 작동될 수 있는 코드인지 의심이 된다면 [aspect.js](https://github.com/mgechev/aspect.js)에 가서 예제를 따라 해봐도 좋겠다. [Babel](https://babeljs.io/)과 [Decorator plugin](https://github.com/loganfsmyth/babel-plugin-transform-decorators-legacy)도 잊지말고 챙겨가자.

## 하지만 Decorators라니!

Decorators는 ES7 표준으로 준비 중이다. 이미 위의 예제를 보면서 불평했겠지만, 해당 라이브러리는 아직 표준이 정해지지 않은 Decorators에 의존하고 있다([TC39 Notes, July 28 2016](https://esdiscuss.org/notes/2016-07-28), [Implement new decorator proposal when finalized](https://github.com/babel/babel/issues/2645)). [Babel Legacy Decorator plugin](https://github.com/loganfsmyth/babel-plugin-transform-decorators-legacy)을 사용해서 예제를 따라 해 볼 수는 있으나, 실제 프로젝트에 적용할 용감한 사람은 없으리라 믿는다. 물론 [aspect.js](https://github.com/mgechev/aspect.js)이외에 바로 사용할 수 있는 라이브러리들이 보이긴 했지만, 설명이 용이하고, 개념을 충실히 구현한 것으로 찾다보니 aspect.js가 선택되었다. 지금 바로 무언가에 적용해 보고 싶다면 [meld](https://github.com/cujojs/meld)나 다른 라이브러리들을 찾아 볼 수도 있다. 물론 meld를 포함한 다른 라이브러리들도 있다. 다만 이번에 AOP 자바스크립트 라이브러리들을 찾아보며 생각보다 많지 않은 옵션에 약간 실망한 것도 사실이다.

## 직접 짜볼까?

이 짧은 글로 모든 것을 설명하기는 힘드니 Proxy + Decorator가 어떻게 AOP가 될 수 있는지 짧막히 힌트가 될 코드만 적어본다. 먼저 맨 앞에서 AOP가 Proxy의 연관주제라고 했던 것을 기억하는가? 아래는 `AOP Advice`(실제 동작될 코드)가 작동하는 방식을 Proxy를 활용하여 흉내내는 코드이다. Proxy와 Class는 현시점에서 최신 브라우저에서 구현되어있으므로 아래 그대로 복사 붙여넣기 해봐도 잘 동작한다.(또 다른 힌트를 주자면 IE는 안된다.)

```javascript
...
function Logger(target, pattern) {
    return new Proxy(target, {
        get: function(obj, prop) {
            var value, name;
            if (!Reflect.has(obj, prop)) {
                return;
            }
            name = target.name || target.constructor.name;
            value = Reflect.get(obj, prop);
            if (typeof value === 'function') {
                value = function() {
                    let result = Reflect.apply(obj[prop], obj, arguments);
                    if (pattern.exec(prop)) {
                        console.log(`Function ${prop} retrieved result ${JSON.stringify(result)}`);
                    }
                    return result;
                }.bind(obj);
            }
            return value;
        }
    });
}

class BookCollection {
    getNameByISBN(isbn) {
        return {
            isbn: isbn,
            name: 'Proxy + Decorators = AOP'
        };
    }
}
BookCollection.prototype = Logger(BookCollection.prototype, /^get.*/);
console.log(new BookCollection().getNameByISBN('sdaf'));
// Function getNameByISBN retrieved result {"isbn":"some-isbn","name":"Proxy + Decorator = AOP"}
// Object {isbn: "some-isbn", name: "Proxy + Decorator = AOP"}
```

위의 코드는 `BookCollection`프로토타입에 Proxy를 만들어 주어진 패턴의 함수가 실행될 경우에만 로그를 같이 실행하는 동작을 한다. [지난 주 Proxy주제의 위클리](https://github.com/nhnent/fe.javascript/wiki/March-6---March-10,-2017)를 읽고 온 독자라면 충분히 이해할 수 있을 것이라 본다. 그럼 이제 Decorators를 사용해서 Logger를 묶어보는 방식으로 코드를 바꿔보자.

```js
function wove(pattern) {
    return function (target) {
        target.prototype = Logger(target.prototype, pattern);
    };
}


@wove(/^get.*/)
class BookCollection {
    getNameByISBN(isbn) {
        return {
            isbn: isbn,
            name: 'Proxy + Decorators = AOP'
        };
    }
}

console.log(new BookCollection().getNameByISBN('sdaf'));
// Function getNameByISBN retrieved result {"isbn":"some-isbn","name":"Proxy + Decorator = AOP"}
// Object {isbn: "some-isbn", name: "Proxy + Decorator = AOP"}
```

`@wove` Decorators에 당황하지 말자. 위의 `@wove`는 아래의 코드와 완벽히 동일한 코드이다.

```js
wove(/^get.*/)(BookCollection);
```

조금 더 Descriptors에 대해 이해하고 싶다면 [Decorators](https://medium.com/google-developers/exploring-es7-decorators-76ecb65fb841#.yn607pj7t), [Decorators and functions](https://rreverser.com/ecmascript-decorators-and-functions/)
를 읽어보자. Decorators는 Stage2 Draft단계이며, 현재의 표준에도 이견이 이어지고 있는만큼 추후 바뀔 여지가 있다는 것을 감안하고 보자. 물론 aspect.js가 제공하는 방법은 위의 코드보다 훨씬 더 복잡하다. 그러나 여기까지의 원리를 이해한다면 AOP를 소개하며 소개했던 코드가 어떤식으로 동작하게 되는지 상상해보는데는 충분하리라 본다.

## 마치며

자바 세상에서 AOP를 표현하는 단어로 **Black Magic** 이라는 말이 있다. 제임스 고슬링은 [eWeek과의 인터뷰](https://www.eweek.com/it-management/suns-gosling-new-java-flavors-brewing?page=3)에서 "위험한", "문제덩어리", 그리고 ["설명서 없이 전기톱을 쥐여주는 짓"](https://www.eweek.com/development/you-down-with-aop)이라고 말한 바 있다. 이는 OOP로 꼼꼼하게 짜인 자바 세상의 대원칙을 무시하고 AOP코드들이 싹둑 잘라 들어오는(말 그대로 Cross-cutting하는)것 처럼 보였기 때문이리라 생각한다. 그렇다면 자바스크립트의 AOP역시 **흑마법**같은 존재가 될까? 가만히 생각해보면 우리는 거창하게 AOP라는 말을 쓰지 않아도, AspectJ같은 도구가 없어도, 이미 더 무지막지한 레이저 블레이를 휘두를 수도 있다. 이미 짜인 코드에 Aspect를 적용하기 위해 AspectJ가 해야 하는 일을 생각해보면 아래의 자바스크립트 코드는 참 쉽고 자연스럽다.(이러면 안된다고 생각 할지라도)

```js
let originalFunction = Collection.prototype.getNameByISBN;
Collection.prototype.getNameByISBN = function () {
    let result = originalFunction.apply(this, arguments);
    Logger.info(`Retrieving ${result.isbn} - ${result.name} has been succeed`);
    return result;
};
```

자바스크립트는 ES6, ES7 표준의 방향이나 Typescript의 인기 등 점차 우리에게 익숙한 도구인 OOP대로 구현할 수 있도록 모양새를 갖춰가고 있다. 그에 따라 자연스럽게 이를 보완해줄 수 있는 AOP에 도구도 더 나아지고 이에 대한 얘기도 더 나오게 되지 않을까 생각해본다. 이번에는 Proxy복습겸, AOP복습겸 자바스크립트 라이브러리 둘러보는 정도로 마무리를 한다. 이 글은 소개 정도에서 마치므로, 이 주제에 대해 가지고 있는 생각이 있다면 의견을 나누어 주면 좋겠다. 필자도 조금 더 고민해보고 다른 생각이 들면 다시 생각을 공유해 보기로 하겠다.

## 참고글

- AOP in Javascript
  - [Aspect-Oriented Programming in JavaScript](https://blog.mgechev.com/2015/07/29/aspect-oriented-programming-javascript-aop-js/)
  - [OOP Is Not Your Hammer](https://software.intel.com/en-us/html5/hub/blogs/oop-is-not-your-hammer/)
  - [Intro to Aspect Oriented Programming](https://know.cujojs.com/tutorials/aop/intro-to-aspect-oriented-programming)
- ECMAScript Proxy
  - [Proxy](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
- ECMAScript Decorators
  - [TC39 Notes, July 28 2016](https://esdiscuss.org/notes/2016-07-28)
  - [Decorators](https://medium.com/google-developers/exploring-es7-decorators-76ecb65fb841#.yn607pj7t)
  - [Decorators and functions](https://rreverser.com/ecmascript-decorators-and-functions/)
- Babel
  - [Implement new decorator proposal when finalized](https://github.com/babel/babel/issues/2645)
- Interviews with "fathers" of languages about AOP
  - [eWeek - You Down with AOP?](https://www.eweek.com/development/you-down-with-aop)
  - [Suns Gosling - The dangers of aspect-oriented programming](https://www.eweek.com/it-management/suns-gosling-new-java-flavors-brewing?page=3)
- Libraries
  - [aspect.js](https://github.com/mgechev/aspect.js)
  - [meld](https://github.com/cujojs/meld)
  - [aspect-js](https://www.npmjs.com/package/aspect-js)
  - [kaop](https://github.com/k1r0s/kaop)

![AOP.png](https://image.toast.com/aaaadh/alpha/2017/techblog/AOP.png)



<br>

<br>

#### 참고링크: [자바스크립트 AOP 맛보기 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/109)

<br>