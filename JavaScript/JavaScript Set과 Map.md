# [JavaScript] 📦 Set 과 Map

# Set

- set 객체는 중복되지 않는 유일한 값들의 집합이다.
- set 객체는 다음과 같은 특징을 가진다.
  1. 동일한 값을 중복하여 포함할수 없다
  2. 요소 순서에 의미가 없다
  3. 인덱스로 요소에 접근할 수 없다.

이러한 set 객체는 수학적 집합을 구현하기위한 자료구조이다.
그래서 set을 통해 교집합, 합집합, 차집합, 여집합 등을 구현할 수 있다.

<br>

## 1.set객체의 생성

set객체는 set 생성자 함수로 생성한다. 인수를 전달하지 않으면 빈 set객체가 생성된다. set 생성자 함수는 **이터러블**을 인수로 받아 set객체를 생성한다!! 이때 이터러블의 중복된 값은 아래의 예시처럼 set객체에 요소로 저장되지 않는다.

```js
const set = new Set();
console.log(set); // Set(0) {}

const set1 = new Set([1, 2, 3, 3]);
console.log(set1); // Set(3) {1, 2, 3}

const set2 = new Set('hello');
console.log(set2); // Set(4) {"h", "e", "l", "o"}
```

그래서 set을 사용해서 배열에서 중복된 요소를 제거할수있다. (이런 방식이 유용하게 쓰일것같음)

```js
// 배열의 중복 요소 제거
const uniq = array => array.filter((v, i, self) => self.indexOf(v) === i);
console.log(uniq([2, 1, 2, 3, 4, 3, 4])); // [2, 1, 3, 4]

// Set을 사용한 배열의 중복 요소 제거
const uniq = array => [...new Set(array)];
console.log(uniq([2, 1, 2, 3, 4, 3, 4])); // [2, 1, 3, 4]
```

<br>

## 2. 요소 개수 확인

set 객체의 요소 개수를 확인할 때는 Set.prototype.size 프로퍼티를 사용한다.

> size 프로퍼티는 setter 함수없이 getter 함수만 존재하는 접근자 프로퍼티다. 그래서 size 프로퍼티에 숫자를 할당하여 set 객체의 요소개수를 변경할수 없다!

```js
const set = new Set([1, 2, 3]);

console.log(Object.getOwnPropertyDescriptor(Set.prototype, 'size'));
// {set: undefined, enumerable: false, configurable: true, get: ƒ}

set.size = 10; // 무시된다.
console.log(set.size); // 3
```

<br>

## 3. 요소 추가

set 객체에 요소를 추가할때는 Set.prototype.add 메서드를 사용하면 된다.
add 메서드는 새로운 요소가 추가된 Set 객체를 반환한다.

```js
const set = new Set();

set.add(1).add(2).add(2); // 이렇게도 사용가능한데 중복된 값은 무시된다.
console.log(set); // Set(2) {1, 2}
```

set 객체는 객체나 배열과 같이 자바스크립트의 모든 값을 요소로 저장할 수 있다.
(그런데 이렇게 쓰면 안좋을것 같긴하다. 값들이 점점 많아지면 값에 접근하거나 찾기가 힘들어질것 같음)

```js
const set = new Set();

set
  .add(1)
  .add('a')
  .add(true)
  .add(undefined)
  .add(null)
  .add({})
  .add([]);

console.log(set); // Set(7) {1, "a", true, undefined, null, {}, []}
```

<br>

## 4. 요소 존재 여부 확인

Set 객체에 특정 요소가 존재하는지 확인하려면 Set.prototype.has 메서드를 사용한다. has는 요소가 있는지 없는지에 따라 불리언값을 반환한다.

```js
const set = new Set([1, 2, 3]);

console.log(set.has(2)); // true
console.log(set.has(4)); // false
```

<br>

## 5. 요소 삭제

set 객체의 특정 요소를 삭제하려면 Set.prototype.delete 메서드를 사용한다. delete 메서드는 삭제 성공여부를 나타내는 불리언값을 반환한다.
delete 메서드에는 인덱스가 아니라 **삭제하려는 요소값을 인수로 전달해야한다.** set 객체는 인덱스를 갖지않기때문에!!

delete는 불리언값을 반환하기때문에 add처럼 여러개를 붙여서 사용할수 없다.(add는 객체를 리턴하기때문에 여러개를 동시에 사용가능함)

```js
const set = new Set([1, 2, 3]);

// 요소 2를 삭제한다.
set.delete(2);
console.log(set); // Set(2) {1, 3}

// 요소 1을 삭제한다.
set.delete(1);
console.log(set); // Set(1) {3}

const set = new Set([1, 2, 3]);

// delete는 불리언 값을 반환한다.
set.delete(1).delete(2); // TypeError: set.delete(...).delete is not a function
```

<br>

## 6. 요소 일괄 삭제

set 객체의 모든 요소를 일괄삭제하려면 Set.prototype.clear메서드를 사용하면 된다. clear는 언제나 undefined를 반환한다.

```js
const set = new Set([1, 2, 3]);

set.clear();
console.log(set); // Set(0) {}
```

<br>

## 7. 요소 순회

set객체의 요소를 순회하려면 Set.prototype.forEach메서드를 사용한다.
forEach메서드에 콜백함수를 인수로 넣어주게 되는데, 콜백함수는 3개의 인수를 전달받는다. (현재 순회중인 요소값, 현재 순회중인 요소값, 현재 순회중인 set 객체 자체)
첫번째와 두번째 인수가 같은 이유는 Array.prototype.forEach메서드와 인터페이스를 통일하기 위해서이다. (Array.prototype.forEach는 두번째 인수로 인덱스를 전달받지만, set은 순서에 의미가없기때문에 인덱스를 받지않는다!)

```js
const set = new Set([1, 2, 3]);

set.forEach((v, v2, set) => console.log(v, v2, set));
/*
1 1 Set(3) {1, 2, 3}
2 2 Set(3) {1, 2, 3}
3 3 Set(3) {1, 2, 3}
*/
```

<br>

★★★★★ 이부분은 좀 알면 유용하게 쓸수있을것같음!!
우선 set 객체는 이터러블이기 때문에 for ..of문으로 순회할수있고, 스프레드문법과, 배열 디스트럭처링의 대상이 될 수도 있다.

```js
const set = new Set([1, 2, 3]);

// Set 객체는 Set.prototype의 Symbol.iterator 메서드를 상속받는 이터러블이다.
console.log(Symbol.iterator in set); // true

// 이터러블인 Set 객체는 for...of 문으로 순회할 수 있다.
for (const value of set) {
  console.log(value); // 1 2 3
}

// 이터러블인 Set 객체는 스프레드 문법의 대상이 될 수 있다.
console.log([...set]); // [1, 2, 3]

// 이터러블인 Set 객체는 배열 디스트럭처링 할당의 대상이 될 수 있다.
const [a, ...rest] = [...set];
console.log(a, rest); // 1, [2, 3]
```

<br>

## 8. 집합 연산

set 객체는 교집합, 차집합, 합집합 등을 구현할수 있다.

#### 1) 교집합

intersection메서드 내의 this는 생성자 함수가 생성한 인스턴스를 가리킴!!

```js
Set.prototype.intersection = function (set) {
  const result = new Set();

  for (const value of set) {
    // 2개의 set의 요소가 공통되는 요소이면 교집합의 대상이다.
    if (this.has(value)) result.add(value);
  }

  return result;
};

// 이렇게도 가능하다...신기하구먼..
/*
Set.prototype.intersection = function (set) {
  return new Set([...this].filter(v => set.has(v)));
};
*/

const setA = new Set([1, 2, 3, 4]);
const setB = new Set([2, 4]);

// setA와 setB의 교집합
console.log(setA.intersection(setB)); // Set(2) {2, 4}
// setB와 setA의 교집합
console.log(setB.intersection(setA)); // Set(2) {2, 4}
```

<br>

#### 2) 합집합

합집합은 result를 인스턴스의 set으로 초기화 하고 result에 다른 집합을 합쳐주는데, set은 동일한 값을 가지지않으므로 값이 중복되지않게 합집합을 만들수 있다.

```js
Set.prototype.union = function (set) {
  // this(Set 객체)를 복사
  const result = new Set(this);

  for (const value of set) {
    // 합집합은 2개의 Set 객체의 모든 요소로 구성된 집합이다. 중복된 요소는 포함되지 않는다.
    result.add(value);
  }

  return result;
};

// 이렇게도 할수 있음...진짜간단행
/*
Set.prototype.union = function (set) {
  return new Set([...this, ...set]);
};
*/

const setA = new Set([1, 2, 3, 4]);
const setB = new Set([2, 4]);

// setA와 setB의 합집합
console.log(setA.union(setB)); // Set(4) {1, 2, 3, 4}
// setB와 setA의 합집합
console.log(setB.union(setA)); // Set(4) {2, 4, 1, 3}
```

<br>

#### 3) 차집합

차집합 A-B는 집합 A에는 존재하지만 B에는 존재하지 않는 요소로 구성된다.
여기서는 delete 메서드를 사용하면 된다!

```js
Set.prototype.difference = function (set) {
  // this(Set 객체)를 복사
  const result = new Set(this);

  for (const value of set) {
    result.delete(value);
  }

  return result;
};

// 이렇게도 할수있다..
/*
Set.prototype.difference = function (set) {
  return new Set([...this].filter(v => !set.has(v)));
};
*/


const setA = new Set([1, 2, 3, 4]);
const setB = new Set([2, 4]);

// setA에 대한 setB의 차집합
console.log(setA.difference(setB)); // Set(2) {1, 3}
// setB에 대한 setA의 차집합
console.log(setB.difference(setA)); // Set(0) {}
```

<br>

#### 4) 부분 집합과 상위 집합

집합 A가 집합 B에 포함되는 경우 집합 A는 B의 부분집합이며 집합 B는 A의 상위집합이다.

```js
// this가 subset의 상위 집합인지 확인한다.
Set.prototype.isSuperset = function (subset) {
  for (const value of subset) {
    // superset의 모든 요소가 subset의 모든 요소를 포함하는지 확인
    if (!this.has(value)) return false;
  }

  return true;
};

//이렇게도 가능하다.. 신기한 자바스크립트의 세계..
/*
Set.prototype.isSuperset = function (subset) {
  const supersetArr = [...this];
  return [...subset].every(v => supersetArr.includes(v));
};
*/

const setA = new Set([1, 2, 3, 4]);
const setB = new Set([2, 4]);

// setA가 setB의 상위 집합인지 확인한다.
console.log(setA.isSuperset(setB)); // true
// setB가 setA의 상위 집합인지 확인한다.
console.log(setB.isSuperset(setA)); // false
```

<br>

<br>

# Map

- map 객체는 키와 값의 쌍으로 이루어진 컬렉션이다.
- map객체는 객체와 유사하지만 차이가있는데
  1. 객체는 키로 사용할수 있는 값이 문자열 또는 심벌 값 이지만,
     map은 객체를 포함한 모든 값을 키로 사용할 수 있다.
  2. 객체는 이터러블이 아니지만 map은 이터러블이다.
  3. 객체는 요소의 개수를 length로, map은 size메서드로 확인할 수 있다.

<br>

## 1. Map 객체의 생성

Map 객체는 Map 생성자 함수로 생성한다. 인수를 전달하지않으면 빈 map객체가 생성된다. map 생성자 함수는 **이터러블**을 인수로 전달받아 map 객체를 생성한다. 이때 인수로 전달되는 이터러블은 **키와 값의 쌍으로 이루어진 요소**로 구성되야 한다.

```js
const map1 = new Map([['key1', 'value1'], ['key2', 'value2']]);
console.log(map1); // Map(2) {"key1" => "value1", "key2" => "value2"}

const map2 = new Map([1, 2]); // TypeError: Iterator value 1 is not an entry object
```

**★중복된 키★는 map 객체에 요소로 저장되지 않는다.**

```js
const map = new Map([['key1', 'value1'], ['key1', 'value2']]);
console.log(map); // Map(1) {"key1" => "value2"}
```

<br>

## 2. 요소 개수 확인

Map.prototype.size 프로퍼티를 사용한다!!(set과 비슷)

> size 프로퍼티는 setter 함수없이 getter 함수만 존재하는 접근자 프로퍼티다. 그래서 size 프로퍼티에 숫자를 할당하여 map 객체의 요소개수를 변경할수 없다!

```js
const map = new Map([['key1', 'value1'], ['key2', 'value2']]);

map.size = 10; // 무시된다.
console.log(map.size); // 2
```

<br>

## 3. 요소 추가

map 객체에 요소를 추가할때는 Map.ptorotype.set 메서드를 사용한다.
set 메서드는 새로운 요소가 추가된 Map객체를 반환한다. 그래서 set메서드를 연속적으로 호출할수 있다.

```js
const map = new Map();

map
  .set('key1', 'value1')
  .set('key2', 'value2');

console.log(map); // Map(2) {"key1" => "value1", "key2" => "value2"}
```

★★★★★객체와 달리 map객체의 key 타입에는 제한이 없다.

```js
const map = new Map();

const lee = { name: 'Lee' };
const kim = { name: 'Kim' };

// 객체도 키로 사용할 수 있다.
map
  .set(lee, 'developer')
  .set(kim, 'designer');

console.log(map);
// Map(2) { {name: "Lee"} => "developer", {name: "Kim"} => "designer" }
```

<br>

## 4.요소 취득

특정요소를 취득하려면 Map.prototype.get메서드를 사용한다.
get메서드의 인수로 키를 전달하면 Map 객체에서 인수로 전달한 키를 갖는 값을 반환한다. 전달한 키를 갖는 요소가 없다면 undefined를 반환한다.

```js
const map = new Map();

const lee = { name: 'Lee' };
const kim = { name: 'Kim' };

map
  .set(lee, 'developer')
  .set(kim, 'designer');

console.log(map.get(lee)); // developer
console.log(map.get('key')); // undefined
```

<br>

## 5. 요소 존재 여부 확인

특정 요소를 가지고 있는지 확인하려면 Map.ptorotype.has메서드를 사용한다. has 메서드는 불리언값을 반환한다!

```js
const lee = { name: 'Lee' };
const kim = { name: 'Kim' };

const map = new Map([[lee, 'developer'], [kim, 'designer']]);

console.log(map.has(lee)); // true
console.log(map.has('key')); // false
```

<br>

## 6 요소 삭제

특정 요소를 삭제하려면 Map.prototype.delete 메서드를 사용한다. delete 메서드는 삭제 성공여부를 나타내는 불리언값을 반환한다.
delete 메서드에는 **삭제하려는 키값을 인수로 전달해야한다.**

delete는 불리언값을 반환하기때문에 add처럼 여러개를 붙여서 사용할수 없다.(add는 객체를 리턴하기때문에 여러개를 동시에 사용가능함)

```js
const lee = { name: 'Lee' };
const kim = { name: 'Kim' };

const map = new Map([[lee, 'developer'], [kim, 'designer']]);

map.delete(kim);
console.log(map); // Map(1) { {name: "Lee"} => "developer" }
```

<br>

## 7. 요소 일괄 삭제

모든 요소를 일괄삭제하려면 Map.prototype.clear메서드를 사용하면 된다. clear는 언제나 undefined를 반환한다.

```js
const lee = { name: 'Lee' };
const kim = { name: 'Kim' };

const map = new Map([[lee, 'developer'], [kim, 'designer']]);

map.clear();
console.log(map); // Map(0) {}
```

<br>

## 8. 요소 순회

요소를 순회하려면 Map.prototype.forEach메서드를 사용한다.
forEach메서드에 콜백함수를 인수로 넣어주게 되는데, 콜백함수는 3개의 인수를 전달받는다. (현재 순회중인 value, 현재 순회중인 key, 현재 순회중인 map 객체 자체)
첫번째와 두번째 인수가 같은 이유는 Array.prototype.forEach메서드와 인터페이스를 통일하기 위해서이다.

```js
const lee = { name: 'Lee' };
const kim = { name: 'Kim' };

const map = new Map([[lee, 'developer'], [kim, 'designer']]);

map.forEach((v, k, map) => console.log(v, k, map));
/*
developer {name: "Lee"} Map(2) {
  {name: "Lee"} => "developer",
  {name: "Kim"} => "designer"
}
designer {name: "Kim"} Map(2) {
  {name: "Lee"} => "developer",
  {name: "Kim"} => "designer"
}
*/
```

map 객체는 이터러블이기 때문에 for ..of문으로 순회할수있고, 스프레드문법과, 배열 디스트럭처링의 대상이 될 수도 있다.

```js
const lee = { name: 'Lee' };
const kim = { name: 'Kim' };

const map = new Map([[lee, 'developer'], [kim, 'designer']]);

// Map 객체는 Map.prototype의 Symbol.iterator 메서드를 상속받는 이터러블이다.
console.log(Symbol.iterator in map); // true

// 이터러블인 Map 객체는 for...of 문으로 순회할 수 있다.
for (const entry of map) {
  console.log(entry); // [{name: "Lee"}, "developer"]  [{name: "Kim"}, "designer"]
}

// 이터러블인 Map 객체는 스프레드 문법의 대상이 될 수 있다.
console.log([...map]);
// [[{name: "Lee"}, "developer"], [{name: "Kim"}, "designer"]]

// 이터러블인 Map 객체는 배열 디스트럭처링 할당의 대상이 될 수 있다.
const [a, b] = map;
console.log(a, b); // [{name: "Lee"}, "developer"]  [{name: "Kim"}, "designer"]
```

------

map 객체는 이터러블이면서 동시에 이터레이터인 객체를 반환하는 메서드를 제공한다.

- Map.prototype.keys > map 객체에서 요소키를 값으로 갖는 이터러블이면서 동시에 이터레이터인 객체를 반환
- Map.prototype.values > map 객체에서 요소값을 값으로 갖는 이터러블이면서 동시에 이터레이터인 객체를 반환
- Map.prototype.entries > map 객체에서 요소키와 요소값을 값으로 갖는 이터러블이면서 동시에 이터레이터인 객체를 반환

```js
const lee = { name: 'Lee' };
const kim = { name: 'Kim' };

const map = new Map([[lee, 'developer'], [kim, 'designer']]);

// Map.prototype.keys는 Map 객체에서 요소키를 값으로 갖는 이터레이터를 반환한다.
for (const key of map.keys()) {
  console.log(key); // {name: "Lee"} {name: "Kim"}
}

// Map.prototype.values는 Map 객체에서 요소값을 값으로 갖는 이터레이터를 반환한다.
for (const value of map.values()) {
  console.log(value); // developer designer
}

// Map.prototype.entries는 Map 객체에서 요소키와 요소값을 값으로 갖는 이터레이터를 반환한다.
for (const entry of map.entries()) {
  console.log(entry); // [{name: "Lee"}, "developer"]  [{name: "Kim"}, "designer"]
}
```

<br>

> 모던 자바스크립트 Deep Dive를 읽고 작성한 글입니다.

<br>

<br>

#### 참고링크: [[JavaScript\] 37. Set 과 Map (velog.io)](https://velog.io/@dolarge/Java-Script-Set-과-Map)

<br>