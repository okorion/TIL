#### 1. 🔑 외래키 (Foreign Key)란?

외래키는 두 테이블을 서로 연결하는 데 사용되는 키이다.

외래키가 포함된 테이블을 자식 테이블이라고 하고 외래키 값을 제공하는 테이블을 부모 테이블이라한다.

------

#### 2. 외래키 사용시 주의 사항

\1) 외래키 값은 **NULL**이거나 **부모 테이블의** **기본키 값**과 동일해야한다. (참조 무결성 제약조건)

\2) 부모 테이블의 기본키, 고유키를 외래키로 지정할 수 있다.

\3) 부모 테이블의 기본키, 고유키가 여러개의 컬럼으로 이루어져 있다면 부모가 가진 기본키, 고유키 컬럼을 원하는 개수만큼 묶어서 외래키로 지정할 수 있다. 

```
CREATE TABLE `parent` (
	`id1` INT(11) NOT NULL,
	`id2` INT(11) NOT NULL,
	`id3` INT(11) NOT NULL,
	`uk1` INT(11) NOT NULL,
	`uk2` INT(11) NOT NULL,
	`uk3` INT(11) NOT NULL,
	PRIMARY KEY (`id1`, `id2`, `id3`),
	UNIQUE KEY (`uk1`, `uk2`, `uk3`)
);

CREATE TABLE `child` (
	`id` INT(11) NOT NULL,
	`id1` INT(11) NOT NULL,
	`id2` INT(11) NOT NULL,
	`uk1` INT(11) NOT NULL,
	`uk2` INT(11) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`id1`, `id2`) REFERENCES `parent` (`id1`, `id2`),
	FOREIGN KEY (`uk1`, `uk2`) REFERENCES `parent` (`uk1`, `uk2`)
)
```

\4) 외래키로 지정할 두 테이블의 필드는 같은 데이터 타입이어야 한다.

~~

#### 4. 외래키 옵션

**1) On Delete**

 Cascade : 부모 데이터 삭제 시 자식 데이터도 삭제 

 Set null : 부모 데이터 삭제 시 자식 테이블의 참조 컬럼을 Null로 업데이트

 Set default : 부모 데이터 삭제 시 자식 테이블의 참조 컬럼을 Default 값으로 업데이트

 Restrict : 자식 테이블이 참조하고 있을 경우, 데이터 삭제 불가

 No Action : Restrict와 동일, 옵션을 지정하지 않았을 경우 자동으로 선택된다.


**2) On Update**

 Cascade : 부모 데이터 업데이트 시 자식 데이터도 업데이트 

 Set null : 부모 데이터 업데이트 시 자식 테이블의 참조 컬럼을 Null로 업데이트

 Set default : 부모 데이터 업데이트 시 자식 테이블의 참조 컬럼을 Default 값으로 업데이트

 Restrict : 자식 테이블이 참조하고 있을 경우, 업데이트 불가

 No Action : Restrict와 동일, 옵션을 지정하지 않았을 경우 자동으로 선택된다.

~~



출처: [[Mysql\] Foreign Key(외래키) (tistory.com)](https://bamdule.tistory.com/45)





**
외래 키 제약 - ON UPDATE, ON DELETE**

 

 FOREIGN KEY 제약 조건에 의해 참조되는 테이블의 데이터의 수정이나 삭제가 발생하면, 참조하고 있는 테이블의 데이터도 같이 영향을 받습니다. 이때 참조하고 있는 테이블의 동작은 다음 키워드를 사용하여 제약 조건에서 미리 설정을 할 수 있습니다.

 

| **제약**                | **설명**                                                | **비고**                              |
| ----------------------- | ------------------------------------------------------- | ------------------------------------- |
| **NO ACTION, RESTRICT** | 자식 테이블에 해당 외래키가 있을 때 수정/삭제 되지 않음 |                                       |
| **CASCADE**             | 자식 테이블의 해당 행도 수정/삭제                       |                                       |
| **SET NULL**            | 자식 테이블의 외래키를 NULL로                           | 자식 외래키가 NOT NULL일 시 설정 불가 |
| **SET DEFAULT**         | 자식 테이블의 외래키를 기본값으로                       | InnoDB 엔진에서 사용 불가             |



출처: [MySQL - 기본키(Primary Key) , 외래키 (Foreign Key) (tistory.com)](https://dding9code.tistory.com/78)