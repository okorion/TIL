#### 1. SQL 용어 및 개념

 아래의 보기에서 각 문항의 설명에 맞는 용어를 고르시오.

> 기본 키, 테이블, 스키마, 레코드, 컬럼

1) 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술한 것 - 스키마
2) 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합 - 테이블
3) 고유한 데이터 형식이 지정되는 열 - 컬럼
4) 단일 구조 데이터 항목을 가리키는 행 - 레코드
5) 각 행의 고유 값 - 기본 키



#### 2. SQL 문법

 아래의 보기 (1) ~ (4) 중에서, DML이 아닌 것을 고르시오.  # DML : 테이블이나 관계의 구조를 생성하는데 사용

> (1) CREATE
>
> (2) UPDATE
>
> (3) DELETE
>
> (4) SELECT

=> (1) CREATE는 DDL(Data Definition Language)이다.  # DDL : 테이블에 데이터 검색, 삽입, 수정, 삭제하는 데 사용



#### 3. Relational DBMS

 RDBMS의 개념적 정의와 이를 기반으로 한 DB-Engine의 종류 세가지 이상 작성하시오. 

=> 관계형 데이터베이스 관리 시스템(relational database management system, RDBMS)은 IBM 산호세 연구소의 에드거 F. 커드가 도입한 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템이다.
=> Oracle, MySQL, Microsoft SQL Server

#### 4. INSERT INTO

 다음과 같은 스키마를 가지는 테이블이 있을 때, 아래의 보기 (1) ~ (4) 중 틀린 문장을 고르시오.

```sql
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);
```

> (1) INSERT INTO classmates (name, age, address) VALUES('홍길동', 20, 'seoul');
>
> (2) INSERT INTO classmates VALUES('홍길동', 20, 'seoul');
>
> (3) INSERT INTO classmates VALUES (address='seoul', age=20, name='홍길동');
>
> (4) INSERT INTO classmates (address, age, name) VALUES ('seoul', 20, '홍길동');

=> (3)


#### 5. 와일드카드 문자

 SQL에서 사용 가능한 와일드카드 문자인 %와 _을 비교하여 작성하시오.

 * % : 0 개 이상의 문자를 대체
 * _ : 단일 문자에 대한 대체