## 🎰 indexOf, findIndex, find 차이점

![post-thumbnail](https://velog.velcdn.com/images/zwonlala/post/6352337d-bc73-4b1e-b3c9-e74aee6d90d6/JS2.png)

#### 이 문서는 [fastcampus 강의](https://www.fastcampus.co.kr/dev_online_react/) 를 듣고 정리한 문서입니다. 문제가 있을 경우 이곳으로 문의주세요! 😀

#### indexOf

`indexOf` 는 배열에서 원하는 특정 항목이 배열의 몇번째 원소인지 찾아 index를 리턴해주는 함수. (만약에 못찾으면 -1 리턴)

```javascript
const superheros = ['아이언맨', '캡틴 아메리카', '토르', '블랙팬서'];

const index = superheros.indexOf('아이언맨');
console.log(index); //0

const index = superheros.indexOf('토르');
console.log(index); //2

const index = superheros.indexOf('iron man');
console.log(index); //-1
```

#### findIndex

만약 위에서 처럼 찾고자하는 것이 boolean, 정수, 문자열... 이면 위와 같이 `indexOf` 함수를 사용해서 찾을 수 있음

하지만 **배열 안에 있는 값이 객체**이거나, 특정 값으로 찾는 것이 아니라 **특정 조건으로 찾는** 거면 `indexOf`으로 찾을 수 없음.

```javascript
const todos = [
	{
		id : 1,
		text : '자바스크립트 입문',
		done : true
	},
	{
		id : 2,
		text : '함수 배우기',
		done : true
	},	
	{
		id : 3,
		text : '객체와 배열 배우기',
		done : true
	},
	{
		id : 4,
		text : '배열 내장함수 배우기',
		done : false
	}
];
```

만약 위에 경우에서 id 값이 3인 객체를 찾고싶으면 위에서 사용한 `indexOf`를 사용할 수 없음

```javascript
//생략...
const index = todos.indexOf(3);
console.log(index); // -1
```

이럴때 사용하는 함수가 `findIndex` 함수이다.

`findIndex` 함수는 파라미터로 함수를 입력받아, 특정 조건을 확인해서 조건을 만족하면 만족하는 원소가 몇 번째인지 알려주는 함수이다.

```javascript
//생략...
const index = todos.findIndex(todo => todo.id === 3);
console.log(index); // 2
```

**배열 안의 값들이 객체**이거나, **특정 조건을 만족하는 원소의 index를 알아내야 하는 경우** `findIndex` 함수를 사용하면 된다.

#### find

만약에 **찾는 것이 index가 아니라 해당 원소나 객체**일 경우

```javascript
//생략...
const todo = todos.find(todo => todo.id === 3);
console.log(todo); // Object{id:3, text:"객체와 배열 배우기", done:true}
```

위와 같이 `find` 함수를 사용하면 된다.

만약 done이 false인 것을 찾고 싶으면

```javascript
//생략...
const todo = todos.find(todo => todo.done === false);
console.log(todo); // Object{id:4, text:"배열과 내장함수 배우기", done:false}
```

다음과 같이 사용하면 된다.

그리고 `indexOf`, `findIndex`, `find` 같은 경우에는 조건에 맞는 것 중 가장 먼저 찾은 멤버의 **index**/**값**을 리턴한다.



∴ 정리하면

위 세가지 함수는 **어떤 값을 찾고 싶을때**, **어디있는지 찾거나**, **그 값 자체**를 사용하고 싶을때 사용

`indexOf` : **특정 값이랑 일치하는 걸 찾을 때**

`findIndex` : **`findIndex`내부에 함수를 넣어줘서 특정 값의 조건으로 찾아서 그게 몇 번째 인지 알고싶을 때**

`find` : **`find` 내부에 함수를 넣어줘서 특정 값의 조건으로 찾아서 그 값 자체를 사용하고 싶을 때**

사용한다.

<br>

<br>

#### 참고링크: [배열 내장함수 (indexOf / findIndex / find) (velog.io)](https://velog.io/@zwonlala/배열-내장함수-indexOf-findIndex-find)

<br>