**IF 문법**

```mysql
IF(조건, '참', '거짓')
```

<br>

<br>

**예제**

****

**기본 예제**

```mysql
SELECT IF(10 > 5, '크다', '작다') AS result
```

<br>

![img](https://mblogthumb-phinf.pstatic.net/MjAxOTA3MjRfNyAg/MDAxNTYzOTQ1MTg4MjA0.NbQhW5JOf5srviBA6DANAM88JLhgSiznRmznHKFdBrkg.PSjrMdmPSYjhjiOj089jtF4Tm-6S1xzVYFhegRvjvL4g.PNG.rorean/Screen_Shot_2019-07-24_at_2.12.39_PM.png?type=w800)

<br>

<br>

**조금 심화 예제** 

![img](https://mblogthumb-phinf.pstatic.net/MjAxOTA3MjRfMjg3/MDAxNTYzOTQzNzk3NjUw.vrtn9fXZYniTXic0lxBFvvNCRWTrljK32cBofb2AWTgg.h9pqF4r5rQtuc9qUmK5nGiVq_a5v3zUdN-6bR03YtZ4g.PNG.rorean/Screen_Shot_2019-07-24_at_1.49.14_PM.png?type=w800)

테스트 데이터

테스터 테이터가 위와 같을 때 데이터를 변경해보자

<br>

```mysql
SELECT IF(required, '필수' '선택') AS '필수여부' FROM subject
```



required가 true 이면 '필수'로 false 이면 '선택' 으로 변경되어 나오게 IF 문을 사용했다.

![img](https://mblogthumb-phinf.pstatic.net/MjAxOTA3MjRfMjUy/MDAxNTYzOTQzODEyMTMw.oDVQHlfDVpETFdNeJrznf929YtT9Q7v1SD3tzwc4o04g.TwcgRHt40zmG03St3KFX1ae3WhRFfSEdYm4-IZK6jD8g.PNG.rorean/Screen_Shot_2019-07-24_at_1.49.01_PM.png?type=w800)

<br>

<br>

**중첩 예제**

****

지난번 CASE 문에서 했던 기본 예제를 IF문으로 바꿔보자.

[![img](https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fblogthumb.pstatic.net%2FMjAxOTA3MThfMzAw%2FMDAxNTYzNDMyNjczMzUx.S9lUXZzOJDCD872_nVewhsGRkGm8h0-baw-NEGvZQU0g.KbmLZaFLet5pjRGkkji0RL-uRs7faq4S8IZfBkpXws8g.PNG.rorean%2FScreen_Shot_2019-07-18_at_3.49.56_PM.png%3Ftype%3Dw2%22&type=ff120)](https://blog.naver.com/rorean/221589061047)[ **[mysql\] CASE문 사용하기**개발하면서 자주 사용하는 CASE문을 정리! 은근히 자주 사용한다. 아래 포스팅에서 정렬할 때 C...blog.naver.com](https://blog.naver.com/rorean/221589061047)

<br>

CASE문

```mysql
SELECT
	seq,
	CASE
    	WHEN (u.seq BETWEEN 1 AND 3) THEN 'A' 	
    	WHEN (u.seq BETWEEN 4 AND 6) THEN 'B'        
    	ELSE 'C'
    END AS case_result
FROM `user` u
```

<br>

IF문

```mysql
SELECT u.seq,
	IF(u.seq <= 3, 'A',	IF(u.seq <=6, 'B', 'C')) AS if_result 
FROM `user` u
```

<br>

![img](https://mblogthumb-phinf.pstatic.net/MjAxOTA3MjRfMTcz/MDAxNTYzOTQ1OTM1Nzgy.Lx6Zcme8RDE-GzYdSKHuQzVoIxusJcaotzfE-sm3ayUg.LX-X1rhm5pIJf3-A16Qxk0NKCxkkbZpx2nItookiWtUg.PNG.rorean/Screen_Shot_2019-07-24_at_2.25.21_PM.png?type=w800)

<br>

<br>

<br>

#### 참고링크: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=rorean&logNo=221594169204

<br>