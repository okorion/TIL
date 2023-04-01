# ▶MySQL 문자열 부분 가져오기 (LEFT, MID, RIGHT 함수)

<br>

## ▶설명

MySQL에서 문자열에 일부분을 가져오는 함수는 대표적으로 3가지가 존재합니다.

- LEFT : 문자에 왼쪽을 기준으로 일정 갯수를 가져오는 함수.
- MID : 문자에 지정한 시작 위치를 기준으로 일정 갯수를 가져오는 함수.
- RIGHT : 문자에 오른쪽을 기준으로 일정 갯수를 가져오는 함수.

*** 참고로 MID 함수는 SUBSTR과 SUBSTRING 함수의 동의어입니다.**

<br>

<br>

## ▶사용법

### LEFT

```
LEFT(문자, 가져올 갯수);
```

<br>

### MID

```
MID(문자, 시작 위치, 가져올 갯수);
-- 또는 SUBSTR(문자, 시작 위치, 가져올 갯수);
-- 또는 SUBSTRING(문자, 시작 위치, 가져올 갯수);
```

<br>

### RIGHT

```
RIGHT(문자, 가져올 갯수);
```

<br>

<br>

## ▶예제 쿼리 (Example Query)

### LEFT()

#### 쿼리

```
SELECT LEFT('abcdefg', 3);
```

<br>결과

abc

<br>

### MID()

#### 쿼리

```
SELECT MID('abcdefg', 2, 4);
-- SELECT SUBSTR('abcdefg', 2, 4);
-- SELECT SUBSTRING('abcdefg', 2, 4);
```

<br>

#### 결과

bcde

<br>

### RIGHT()

#### 쿼리

```
SELECT RIGHT('abcdefg', 3);
```

<br>

#### 결과

efg

<br>

<br>

<br>

### 참고링크: [[MySQL\] 문자열 부분 가져오기 (LEFT, MID, RIGHT 함수) :: 확장형 뇌 저장소 (tistory.com)](https://extbrain.tistory.com/62)

<br>