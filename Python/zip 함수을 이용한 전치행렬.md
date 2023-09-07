### 🏡 Zip 함수란?

<br>

`zip(*iterable)`은 동일한 개수로 이루어진 자료형을 묶어주는 역활을 하는 함수이다.
만약 서로 다른 길이의 자료형이 들어오는 경우에는 길이가 짧은 쪽 까지만 묶어준다.

> *iterable 은 반복 가능한 자료형 여러개를 입력할 수 있다는 의미이다.

<br>

💡코드 예시
![img](https://velog.velcdn.com/images/skkumin/post/beffe0db-33c8-4e67-9ecd-69bf16e349b1/image.png)

<br>

`mylist`를 `*`로 unpacking 해주게 되면 `[1, 2, 3]`, `[4, 5, 6]`, `[7, 8, 9]` 3개의 iterable한 자료형이 된다.
zip은 이 자료형을 index끼리 묶어 반환하게 된다.

<br>

<br>

<br>

#### 참고링크: [[Python\] Zip을 활용하여 전치행렬 만들기 (velog.io)](https://velog.io/@skkumin/Python-Zip을-활용하여-전치행렬-만들기)

<br>