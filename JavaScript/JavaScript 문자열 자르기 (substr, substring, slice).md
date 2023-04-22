### ✂ [JavaScript\] 문자열 자르기 (substr, substring, slice)



자바스크립트에서 문자열을 자르기 위해서는 substr(), substring(), slice() 함수를 사용하면 된다. **문자열을 뒤에서부터** 자르기 위해서는 slice() 함수를 사용하면 효율적이며 타 언어의 Right 함수와 비슷하다고 생각하면 된다. 세 가지의 함수 중 상황에 맞는 적절한 함수를 사용하면 된다.

<br>

```javascript
str.substr(start[, length])
str.substring(indexStart[, indexEnd])
str.slice(beginIndex[, endIndex])
```

<br>

위 세 가지 함수의 인수 중 대괄호([]) 부분은 생략이 가능하며, 생략할 경우 시작 위치부터 문자열 끝까지 자른다.

 <br>

<br>

#### substr 함수로 문자열 자르는 방법

```
var str = '자바스크립트';

var result1 = str.substr(0, 2);
// 결과 : "자바"

var result2 = str.substr(2, 4);
// 결과 : "스크립트"

var result3 = str.substr(2);
// 결과 : "스크립트"
```

 <br>

**substr("시작 위치", "길이")** 또는 ***\*substr("시작 위치")\****

substr() 함수는 시작 위치부터 해당 길이만큼 문자열을 자르는 아주 기본적인 함수이다. "길이" 부분을 생략하면 시작 위치부터 문자열 끝까지 자른다.



![img](https://blog.kakaocdn.net/dn/Eq6OS/btq6gc8CSgp/qeTqzpZ0CTvNrfrP1mT3V1/img.png)

<br>

 <br>

#### substring 함수로 문자열 자르는 방법

```
var str = '자바스크립트';

var result1 = str.substring(0, 2);
// 결과 : "자바"

var result2 = str.substring(2, 5);
// 결과 : "스크립"

var result3 = str.substring(2, 6);
// 결과 : "스크립트"

var result4 = str.substring(2);
// 결과 : "스크립트"
```

 <br>

**substring("시작 위치", "종료 위치")** 또는 **substring("시작 위치")**

substring() 함수는 시작 위치에서 종료 위치까지 문자열을 자른다. 주의할 점은 종료 위치의 **-1까지** 문자열을 자른다는 것이다.



![img](https://blog.kakaocdn.net/dn/xaJGe/btq6gct0iNA/RQYQuxkSkhn6SJSFZBbHkK/img.png)

<br>

**substring() 함수에서 음수(-) 사용 시 주의사항**

```
var str = '자바스크립트';

var result1 = str.substring(-4, 5); // str.substring(0, 5)
// 결과 : "자바스크립"

var result2 = str.substring(2, -1); // str.substring(0, 2)
// 결과 : "자바"
```

 <br>

substring() 함수에서 인자에 음수(-)를 대입하면 해당 값은 "0"으로 치환되며, 종료 위치에 음수(-) 또는 "0"인 경우 첫 번째 인수와 두 번째 인수가 뒤바뀐다는 것을 주의해야 한다. 

 <br>

 <br>

#### slice 함수로 문자열 자르는 방법 (뒤에서 부터 자르기)

```
var str = '자바스크립트';

var result1 = str.slice(0, 2);
// 결과 : "자바"

var result2 = str.slice(2, 6);
// 결과 : "스크립트"

var result3 = str.slice(2);
// 결과 : "스크립트"

/************************************/

var result4 = str.slice(-4);
// 결과 : "스크립트"

var result5 = str.slice(-4, 5);
// 결과 : "스크립"

var result6 = str.slice(2, -1);
// 결과 : "스크립"
```

 <br>

**slice("시작 위치", "종료 위치")** 또는 **slice("시작 위치")**

slice() 함수는 기본적인 사용법은 substring() 함수와 동일하며, 다른 점은 음수(-)를 자유롭게 사용할 수 있어서 뒤에서부터 문자열을 자를 때 유용하게 사용할 수 있다.



![img](https://blog.kakaocdn.net/dn/bIYje4/btq6huAW6Om/SP4kzXjk0uf1e5rcpkFD8K/img.png)

<br>

slice() 함수는 문자열을 뒤에서부터 자르는 **str.slice(-4)** 이 부분만 확실히 이해하면 될꺼같다. 문자열의 뒤에서 4번째 자리부터 끝까지 문자열을 자르라는 의미이다.

<br>

<br>

#### 참고링크: [[JavaScript\] 문자열 자르기 (substr, substring, slice) (tistory.com)](https://gent.tistory.com/414)

<br>