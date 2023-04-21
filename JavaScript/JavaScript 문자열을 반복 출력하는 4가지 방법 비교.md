### 🖨 문자열을 반복 출력하는 4가지 방법 비교

<br>

#### 🎞 Preview

```javascript
 /* 첫 번째 방법 - 문자열 누적 방식 */
temp = ''
for (let i = 0; i < n; i++) {
    temp += str    
}   console.log(temp)

/* 두 번째 방법 - process.stdout.write() 함수 사용 */
for (let i = 0; i < n; i++) {
    rl.output.write(str)
}

/* 세 번째 방법 - repeat() 메소드 사용 */    
console.log(str.repeat(n))        

/* 네 번째 방법 - Array.join() 메소드 사용 */    
console.log(Array(n + 1).join(str))
```

<br>

<br>

#### 🎏 각 방법의 장단점

1. **문자열 누적 방식**

   - 장점: for문을 사용하여 문자열을 누적시키기 때문에 구현이 쉽고 이해하기 쉬움.

   - 단점: 반복 횟수에 비례하여 문자열이 계속해서 누적되므로, 입력 값이 매우 큰 경우에는 메모리 부족으로 인해 성능이 저하될 수 있음.

   <br>

2. **`process.stdout.write()` 함수 사용**

   - 장점: process.stdout.write() 함수를 사용하여 출력하므로, 출력 결과를 줄바꿈하지 않기 때문에, 메모리 사용량을 줄일 수 있음.

   - 단점: 출력 결과를 줄바꿈하지 않기 때문에, 줄바꿈을 따로 처리해주어야 하며, process.stdout.write() 함수를 사용하는 것이 익숙하지 않은 경우 구현이 어려울 수 있음.

   <br>

3. **`repeat()` 메소드 사용**

   - 장점: repeat() 메소드를 사용하여 입력된 문자열을 반복해서 출력할 수 있으므로, 구현이 간단하고 이해하기 쉬움.

   - 단점: 입력된 문자열을 반복해서 출력하므로, 반복 횟수에 비례하여 메모리 사용량이 증가함.

   <br>

4. **`Array.join()` 메소드 사용**

   - 장점: Array.join() 메소드를 사용하여 입력된 문자열을 반복해서 출력할 수 있으므로, 구현이 간단하고 이해하기 쉬움.

   - 단점: 입력된 문자열을 반복해서 출력하므로, 반복 횟수에 비례하여 메모리 사용량이 증가함. 또한, Array 생성과 join() 메소드 호출 과정에서 오버헤드가 발생할 수 있음.

<br>

<br>

#### 🎐 문자열 반복 출력의 활용 예시

```javascript
/* 입력 */
string 5

/* 출력 */
stringstringstringstringstring


/* 활용 코드 */
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    str = input[0];
    n = Number(input[1]);
    
    /* 문자열 반복 출력 */

});
```

<br>

<br>

#### 💽 메모리 사용량 순서 (낮은 사용량에서 높은 사용량 순으로)

1. **`process.stdout.write()` 함수 사용**

   ```
   rl.output.write(str)
   ```

   - `write()` 메소드를 사용하여, 출력 버퍼에 문자열을 n번 쓴 후, 줄바꿈을 추가하지 않습니다. `repeat()` 메소드보다는 메모리 사용량이 더 적습니다.

     <br>

2. **`repeat()` 메소드 사용**

   ```
   console.log(str.repeat(n))
   ```

   - `repeat()` 메소드를 사용하여, 문자열을 n번 반복합니다. 메모리 사용량이 `process.stdout.write()` 함수보다는 조금 더 많습니다.

   <br>

3. **`Array.join()` 메소드 사용**

   ```
   console.log(Array(n + 1).join(str))
   ```

   - `Array(n+1)`을 생성하고, `join()` 메소드를 사용하여, 문자열 str을 n번 반복한 결과를 출력합니다.

   <br>

4. **문자열 누적 방식**

   ```
   temp += str
   ```

   - 반복문 내에서 빈 문자열 `temp`에 문자열 `str`을 더하여, 문자열을 n번 반복합니다. 다른 방법에 비해 약간 더 많은 메모리를 사용합니다.

<br>

<br>

> 입력 값이 작은 경우에는 구현이 쉬운 방법을 선택해도 문제 없지만, 입력 값이 매우 큰 경우에는 메모리 사용량을 줄이기 위해 `process.stdout.write()` 함수나 `repeat()` 메소드를 사용하는 것이 좋습니다.

<br>

<br>

👩‍💻 **with ChatGPT** 👩‍💻

#### 🔗 관련 프로그래머스 문제 링크: [문자열 반복해서 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/181950)

<br>