# MySQL - DIV 함수

이 함수는 주어진 숫자를 정수로 나눈 값을 반환하며 FLOOR() 함수와 비슷합니다. 그러나 bigINT 값으로 안전합니다. 부정확한 결과는 bigINT를 초과하는 정수가 아닌 연산수에 대해 발생할 수도 있습니다.

<br>

```
#ex.1)
 mysql> SELECT 5 DIV 2;
      -> 2

 mysql> SELECT 10.2 DIV 2;
      -> 5

 mysql> SELECT 8 DIV 2;
      -> 4

 mysql> SELECT 10 DIV 3;
      -> 3
```

<br>

<br>

<br>

#### 참고링크: [MYSQL - DIV 함수 (habonyphp.com)](https://www.habonyphp.com/2019/02/div.html)

<br>