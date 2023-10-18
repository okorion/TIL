## 🏗️ MyBatis란?

### **🧹 간단 정리**

1. **MyBatis를 사용하면 DB를 쉽게 다룰 수 있다**
   - 예시) preparedstatement처럼 **쿼리문을 복잡하게 입력하지 않고 실제 쿼리문과 유사하게 작성**할 수 있다.
   - preparedstatement : "UPDATE users SET name =?, email =? WHERE id =?"
   - MyBatis : UPDATE users SET name = #{name}, email = #{email} WHERE id = #{id}
2. MyBatis의 또 하나의 장점은 **동적 쿼리 작성이 가능**하다.
3. MyBatis 사용 방법순서 : 의존성 설정 -> DB 설정 -> MyBatis 설정 -> Mapper 인터페이스 작성 -> XML 작성 -> MyBatis 사용

 

아래글을 보고나면 이해가 훨씬 더 잘 될 것이다! **👀**

 

------

###  

### **🐣 MyBatis란?**

MyBatis는 자바 개발자들이 **데이터베이스를 쉽게 다룰 수 있도록 도와주는**

오픈 소스 ORM(Object-Relational Mapping) 프레임워크이다.

 

### 🧐 MyBatis의 사용 목적

MyBatis는 **데이터베이스 쿼리 <-> 프로그래밍 언어 코드를 분리**하여 **유지보수성과 생산성을 높이는 것**.

### 😮 MyBatis의 주요 장점

1. 유연성: **SQL 쿼리를 직접 작성할 수 있으므로 매우 유연**하다. 또한, **MyBatis는 동적 쿼리를 작성**할 수 있다.
2. 간결성: MyBatis는 SQL **쿼리와 프로그래밍 언어 코드를 분리하기 때문에 코드가 간결해져 유지보수에 용이**
3. 성능: MyBatis는 **캐시 기능을 제공하여 데이터베이스 연산 속도를 높일 수 있다**.
4. 다양한 데이터베이스 지원: MyBatis는 다양한 데이터베이스에 대한 지원을 제공합니다.

 

#### 👍 대표적인 장점 유연성(동적쿼리)

동적 쿼리란, **실행 시점에 조건에 따라 SQL 쿼리를 동적으로 생성하는 것**.

이는 데이터베이스의 **검색 조건이나 결괏값 등이 동적으로 변화할 때 유용하게 사용**된다.

 

**MyBatis에서는 동적 쿼리를 작성하기 위해**

**<if>, <choose>, <when>, <otherwise>, <foreach> 등의 태그를 사용할 수 있다.**





<br>

<br>

#### 참고링크: [[JAVA\] - MyBatis란?, 마이바티스란?(예제코드) 간단하고 쉽게 이해하기 (tistory.com)](https://ccomccomhan.tistory.com/130)

<br>