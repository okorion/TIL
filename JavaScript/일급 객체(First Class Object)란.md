## ♠️ 일급 객체(First Class Object)란?

> **일급 객체란 무엇인가?**

자바스크립트로 개발을 하다 보면 **일급 객체**와 **일급 함수**라는 말을 많이 듣는다.
**일급 객체란 뭘까?** 

<br>

![img](https://blog.kakaocdn.net/dn/bXXzVH/btrKwcg1tpY/GlQMFrHkfMkUfkmx3pQx2k/img.png)

<br>

###  **일급 객체(First Class Object)**

**일급 객체란** 다음과 같이 설명할 수 있다.

> **다른 객체들에 일반적으로 적용 가능한 연산을 모두 지원하는 객체를 가리킨다. 보통 함수에 매개변수로 넘기기, 수정하기, 변수에 대입하기와 같은 연산을 지원할 때 일급 객체라고 한다**. - 출처: 위키

설명이 어렵다면 일급 객체의 특징을 아래의 예시로 한번 보자

<br>

### **1. 변수(variable)에 담을 수 있다**

```
let mozzi = function() {
	return "HelloWorld";
}

console.log(mozzi());
```

변수 mozzi의 경우 HelloWorld가 출력된다.

<br>

### **2. 파라미터로 전달할 수 있다**

```
let mozzi = function(){
	let me = 10;
	return me;
}

let devlog = function(param){
	console.log(param);
}

devlog(mozzi());
```

mozzi를 호출하게 되면 10을 반환한다.
아래의 devlog에 파라미터로 mozzi를 넣어 10이 출력된다.

<br>

### **3. 함수의 반환 값으로 사용할 수 있다**

```
function mozzi(){
	return function(){
		console.log("HelloWorld");
    }
}

let test = mozzi();
test();
```

<br>

### **4. 동적으로 프로퍼티 생성이 가능하다**

```
function test(){
	console.log("HelloWorld");
}

test.me = "mozzi";
test.you = "developer";

console.log(test.me);
console.log(test.you);
```

출력은 mozzi와 developer가 출력된다.



<br>

## **일급 함수(First Class Function)란?**

**일급 함수**란 **함수를 일급 객체로 취급하는 것을** 말한다. 자바스크립트의 경우 **함수도 객체로 표현**하기 때문에 **일급 객체** 및 **일급 함수**라고 부른다. 

자바스크립트가 **일급 객체**이기 때문에 아래와 같은 것들을 할 수 있다.

> **콜백함수**
> **고차 함수(High-order function)**
> **클로저(Closure)**

<br>

<br>

#### 참고링크: [[JS\] 일급 객체(First Class Object), 일급함수(First Class Function)란? (tistory.com)](https://mozzi-devlog.tistory.com/11)

<br>