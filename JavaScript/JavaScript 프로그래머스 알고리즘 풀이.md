### 🧸 JavaScript 프로그래머스 알고리즘 풀이

<br>

- **문자열 출력하기**

```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    console.log(str)
});
```

<br>

<br>

해당 코드는 Node.js에서 사용하는 `readline` 모듈을 이용하여 입력값을 받아와 처리하는 코드입니다.

<br>

1. `readline` 모듈을 불러옵니다.

   ```
   javascriptCopy code
   const readline = require('readline');
   ```

   <br>

2. `readline` 모듈의 `createInterface()` 함수를 사용하여 입력 스트림(`process.stdin`)과 출력 스트림(`process.stdout`)을 설정하고, `rl` 객체를 생성합니다.

   ```
   javascriptCopy codeconst rl = readline.createInterface({
       input: process.stdin,
       output: process.stdout
   });
   ```

   <br>

3. `input` 변수를 빈 배열(`[]`)로 초기화합니다.

   ```
   javascriptCopy code
   let input = [];
   ```

   <br>

4. `rl` 객체의 `on()` 함수를 사용하여 `line` 이벤트가 발생했을 때 처리할 콜백 함수를 등록합니다. 이 콜백 함수는 입력값을 배열 `input`에 저장합니다.

   ```
   javascriptCopy coderl.on('line', function (line) {
       input = [line];
   });
   ```

   <br>

5. `rl` 객체의 `on()` 함수를 사용하여 `close` 이벤트가 발생했을 때 처리할 콜백 함수를 등록합니다. 이 콜백 함수는 `input` 배열에서 첫 번째 원소(`input[0]`)를 `str` 변수에 저장합니다.

   ```
   javascriptCopy coderl.on('close',function(){
       str = input[0];
   });
   ```

   <br>

 위 코드는 입력값을 받아와 `str` 변수에 저장하는 부분이 누락되어 있기 때문에, 입력값을 이용하여 `str` 변수를 설정하는 부분을 추가해주어야 합니다. 예를 들어, 입력값에서 양쪽 공백을 제거한 후 `str` 변수에 할당할 수 있습니다. 이를 위해 다음과 같이 코드를 수정할 수 있습니다.

<br>

```
javascriptCopy codeconst readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    const str = input[0].trim(); // 입력값에서 양쪽 공백 제거 후 str 변수 할당
    console.log(str); // str 변수 출력
});
```

 위 코드는 `input` 배열에 입력값을 저장하고, `close` 이벤트에서 `input[0]`을 양쪽 공백을 제거한 후 `str` 변수에 할당합니다. 마지막으로 `console.log()` 함수를 사용하여 `str` 변수를 출력합니다.

<br>

<br>

![image-20230421161813890](../../../AppData/Roaming/Typora/typora-user-images/image-20230421161813890.png)

<br>

👩‍💻 **with ChatGPT** 👩‍💻

<br>