# 🏃 for문과 forEach문 차이

## **for문 예시**

```
const array = new Array(4);

for (let i = 0; i < array.length; i ++){
	// ...
}
```

<br>

## **forEach문 예시**

```
const array = new Array(5);

object.forEach(element => {
	// ...
})
```

<br>

## **차이점** 

#### **동기와 비동기** 

**for문**은 **동기 방식**이기 때문에 오류가 나면 오류가 난 위치 이후의 작업이 동작하지 않고 멈춰버린다. 

하지만 **forEach문**은 **비동기 방식**이기 때문에 멈추지 않고 동작한다. 

 <br>

#### **성능 차이**

**forEach 문은 " 향상된 for문 "** 이라고 칭하며, 가변적인 배열이나 리스트 크기를 구할 필요가 없어 

복잡한 반복문에 적합하며, 인덱스를 생성하여 접근하는 **for문보다 수행 속도가 빠르다.** 

 <br>

## **forEach문의 단점**

**1. 반복문 내에서 배열이나 리스트 값을 변경하거나 추가할 수 없다.** 

오직 읽기 전용으로 불러오기 때문에 데이터를 수정할 수 없다. 

 <br>

**2. 배열을 역순으로 탐색할 수 없다.** 

순서대로 정보를 가져오기 때문에 역순으로 가져올 방법이 없다. 

<br>

<br>

#### 참고자료: [[JavaScript\] for문과 forEach문 차이 (tistory.com)](https://bum-developer.tistory.com/entry/JavaScript-for문과-forEach문-차이)

<br>