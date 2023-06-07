## 🧆 JavaScript Class 활용법

### **😮 들어가기 전**

개발 N연차 동안 메인 언어를 자바스크립트를 사용하고 있다.

개발자 주니어 시절에는 내가 쓰는 코드가 올바른지 맞는지 모르고 일단 되게 하는데에 급급했다.

 

3년 차를 넘어가면서 주니어 시절 짠 내 코드를 유지보수 하기 시작하면서 중복제거의 중요성을 뼈저리게 느끼기 시작했다.

(사용자들은 이렇게 만들어달라고 했다가 사용 후 이게 생각보다 불편해니 바꿔달라는 경우가 매우 많았다.)

 

내가 작성한 돌아가기만 하는 코드는 사용자의 요구사항으로 작은 게 하나 바뀌어도

모든 페이지에 들어가서 검색 찾기로 해당 코드가 들어간 부분을 찾아서 수정하는 불편함을 감수해야 했다.

그래서 이후 공통 함수를 만들거나, 자주 쓰는 UI는 컴포넌트로 만들어 관리하기 시작했다.

 

이것만으로도 나는 이제 좀 내가 발전했다고 뿌듯하게 느끼고 있었다.

하지만, 내가 한 번 더 나아가기 위해서 배워야 할 다음 단계가 눈에 들어왔다. 클래스였다.

 

인터랙티브 디벨로퍼 김종민 님 유튜브 중 Javascirpt로 파도 모양을 만드는 재밌는 예제를 따라 해보려고 했는데

클래스를 이용하여 해당 코드를 만드셨다는 사실을 알게 되었다.

클래스를 전혀 모르던 내가 클래스를 공부해야겠다고 마음을 먹게 된 사건이다.

 <br>

[www.youtube.com/watch?v=LLfhY4eVwDY](https://www.youtube.com/watch?v=LLfhY4eVwDY)

<iframe src="https://www.youtube.com/embed/LLfhY4eVwDY" width="500" height="NaN" frameborder="" allowfullscreen="true" style="box-sizing: inherit; max-width: 100%; margin: 0px; top: 0px; left: 0px; width: 640px; height: 360px;"></iframe>

HTML5 Canvas Tutorial : 움직이는 웨이브 만들기 / Interactive Developer 김종민님 작품

 

 

 <br>

------

### **😎Javascript의 Class**

자바스크립트에서 클래스 사용은 ES6에서부터 지원을 하기 시작했다.

익스플로러에서는 해당 코드 사용이 불가능하나, 최신 브라우저를 이용할 경우 class를 지원한다.

 

Class를 사용하는 가장 큰 이유는 재사용성이다.

작은 사이트의 경우 잘 만든 Function하나로도 충분히 개발이 용이했다면 좀 더 복잡한 사이트를

만들게 될 경우 Class의 장점을 더 잘 알 수 있다고 한다.

 

일단 난 오늘은 클래스의 기본 문법을 공부해보기로 한다.

 

 <br>

 <br>

### **Class 기본 문법**

#### **Class 생성하기**

Javascript 내에서 Class를 생성하려면 간단하다.

class를 선언만 해준다면 class 객체를 바로 만들 수 있다.

 

```
class Person {

}

let kim = new Person();

console.log(kim);
```

 

<br>

![img](https://blog.kakaocdn.net/dn/tBZlv/btqRL2Fsdac/otQOcUFCSicMWEu1qmHfK1/img.png)console.log 결과

<br>

class로 만들어준 예시 Person이라는 이름의 객체가 생성된 걸 확인할 수 있다.

 

 

 

 <br>

 <br>

#### **Class 초기값 설정해주기**

Constructor(생성자)를 이용하면 class 객체의 초기 값을 설정해 줄 수 있다.

class 내부에서 Constructor는 한 개만 존재할 수 있으며, 2번 이상 사용 시 Syntax Error가 발생할 수 있다.

 

Constructor를 이용하여 Person 클래스에 초기 값을 설정해보도록 하자. 

```
class Person {
    constructor (name,age, city) {
        console.log('construtor');
        this.name = name;
        this.age = age;
        this.city = city;
    }
}

let kim = new Person('kim','24','seoul');

console.log(kim);
```

 

<br>

![img](https://blog.kakaocdn.net/dn/b6TfZY/btqRv9TMrRc/KP96yGI9wa1hVzd7aenxD1/img.png)console.log 결과화면

<br>

 

이처럼 Constructor는 새로운 클래스를 생성할 때 가장 처음 실행되면서 초기값을 설정해준다. 

 

 

 

 <br>

 <br>

#### **Class 메서드 사용하기**

class에서 설정한 초기값을 접근해 특정 기능을 하는 메서드를 만드는 것도 가능하다.

간단한 메서드를 하나 만들어보자.

 

class안에 function 형식으로 만들어준 뒤 해당 메서드를 호출하기만 하면 된다.

너무 당연하지만 내년에 해당 사람이 한 살 더 먹는다는 메서드를 class안에 정의한 뒤 호출해봤다.

```
class Person {
    constructor (name,age, city) {
        this.name = name;
        this.age = age;
        this.city = city;
    }
    //메서드생성
    nextYearAge() {
        return Number(this.age) + 1;
    }
}

let kim = new Person('kim','24','seoul');

console.log(kim.nextYearAge());
```

<br>

![img](https://blog.kakaocdn.net/dn/xk1kB/btqRCWF3Ltz/rZJq3wZ9HTpzJBs6aEYslK/img.png)console.log 결과

<br>

class는 javascript 상 객체의 형태이므로 생성된 class 객체에

class 밖에서 새로운 메서드를 넣는 것도 가능하다.

다음 예시를 보자.

 

```
class Person {
    constructor (name,age, city) {
        this.name = name;
        this.age = age;
        this.city = city;
    }
    //메서드생성
    nextYearAge() {
        return Number(this.age) + 1;
    }
}

let kim = new Person('kim','24','seoul');

kim.eat = function () {
    return 'apple'
}

console.log(kim.nextYearAge());
console.log(kim.eat());
```

 



 <br>

![img](https://blog.kakaocdn.net/dn/lKHst/btqRCWze8UW/LiRdheKOSi3vaZTnoWkDEK/img.png)console.log 결과

<br>

class밖에서 추가한 eat이라는 메서드도 정확히 작동한다.

하지만, 이렇게 밖에서 추가한 class는 추후 새로운 new Person class로 새로운 객체를 만들었을 때는

호출하여 사용할 수 없다

 

```
class Person {
    constructor (name,age, city) {
        this.name = name;
        this.age = age;
        this.city = city;
    }
    //메서드생성
    nextYearAge() {
        return Number(this.age) + 1;
    }
}

let kim = new Person('kim','24','seoul');

kim.eat = function () {
    return 'apple'
}

console.log('김씨 내년에는 몇살인가요 ?' + kim.nextYearAge());
console.log('김씨가 먹은건? ' + kim.eat());

let park = new Person('park', '31', 'busan');

console.log('박씨 내년에는 몇살인가요?' + park.nextYearAge());
console.log('박씨가 먹은건?' + park.eat())
```

 

 <br>

![img](https://blog.kakaocdn.net/dn/bWV9cm/btqRt5RLR5c/th5bd8de3qmlFl98rv3HK1/img.png)park class에서 eat 호출 시 실행되지 않음



 <br>

<br>

#### 참고링크: [[Javascript\] 자바스크립트에서 Class 사용하기-constructor, extends, super 사용법 (tistory.com)](https://ordinary-code.tistory.com/22)

<br>