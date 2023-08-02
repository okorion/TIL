## ☘️ vsCode JS 함수 툴팁 추가하기

자바스크립트 작업을 할 때, 

함수에 주석을 달아서 문서화(Doc?)해두면,

**함수를 호출할 때 아래처럼 자동완성 툴팁이 노출**되어 아주 편하다.



![img](https://blog.kakaocdn.net/dn/A3ddl/btq4rdIHskf/RwEvNuEXkwYKlfz60tRoD0/img.png)



**즉, 함수의 파라미터 타입, 반환값에 대한 정보를 보면서 프로그래밍**할 수 있게 된다.

(작업 환경: VSCode 자바스크립트 개발)

------

## **# JS 함수의 문서화 주석 만드는 방법**

### **1. 함수 선언**

▶︎ 평소처럼 함수를 만들어준다.

▶︎ 여기서는 id, name을 파라미터로 받아서 반환하는 getInfo 함수를 선언했다.



![img](https://blog.kakaocdn.net/dn/sVMmD/btq4qzS0nx7/rrdbiHDqjdMHEq9Mifm6M0/img.png)



 

### **2. 주석 생성**

▶︎ 함수의 바로 윗부분에서  **/\**** 까지만 입력한다.

▶︎ 아래와 같은 자동완성이 노출되면 엔터를 쳐준다.



![img](https://blog.kakaocdn.net/dn/bjSj8e/btq4t5pCiTl/oBq6pmL28YrFlXwDBR2pGK/img.png)



 

### **3. 파라미터 타입**

▶︎ @param {*} 파라미터 형식의 주석이 자동완성 되면,

▶︎ 대괄호 { } 사이에 number, string 등의 파라미터의 타입을 입력해 준다.

▶︎ tab을 쳐주면 다음 입력 항목으로 커서가 이동한다.



![img](https://blog.kakaocdn.net/dn/3hTbE/btq4p7Cbk4u/cXZR316aH2BJ8llL5fpXqk/img.png)

![img](https://blog.kakaocdn.net/dn/bbb79q/btq4rzrr3BW/dl5oXadLpVk7MVNRIKN6o1/img.png)



 

### **4. 파라미터 의미**

▶︎ 파라미터의 뒷부분에는 **해당 파라미터가 무엇을 의미하는지** 입력해준다.

▶︎ 입력 완료 후 tab을 쳐주면서, 모든 파라미터에 대해 주석을 달아준다.



![img](https://blog.kakaocdn.net/dn/mDgIl/btq4p8HSNmv/ck6wP8T21ETI7gAgGrXvn1/img.png)

![img](https://blog.kakaocdn.net/dn/ehugxr/btq4wuvTHeN/82opkBoJxhBmU28HFRVxSK/img.png)



 

### **5. 반환값 의미**

▶︎ @returns 뒤에는 반환값의 의미에 대해 입력해준다.



![img](https://blog.kakaocdn.net/dn/6zCUg/btq4q2gldlm/TVnltKDsA1Y3zEkKC0cZb0/img.png)



 

### **6. 함수  설명**

▶︎ 리턴값 입력후 tab을 쳐주면, 커서가 맨위로 이동하는데,

▶︎ 함수 자체에 대한 설명을 입력해주면 끝난다.



![img](https://blog.kakaocdn.net/dn/baMhWJ/btq4rIhnIEA/JpiGxxXogaWzRbXsZteYh1/img.png)



 

### **7. 함수 호출**

▶︎ 이제 함수 호출 시, 아래와 같이 함수에 대한 설명이 툴팁으로 노출된다.



![img](https://blog.kakaocdn.net/dn/TvBNM/btq4tzLfk7g/oilit4SNkrTAOYG2U5ac0k/img.png)



 

▶︎ 또한 파라미터를입력할 때마다, 현재 입력 중인 파라미터가 무엇인지 표시되어 편하다.



![img](https://blog.kakaocdn.net/dn/bHCgej/btq4vQ6NPxx/KqhwJimNZioheW9JOpoSVK/img.png)



------

참고로 위와 같이 /** */ 주석 사이에 @(어노테이션) 달아 문서화하는 포맷을 Javadoc 양식이라고 한다.

<br>

<br>

#### 참고링크: [VS CODE: JS 함수 주석 문서화하는 방법(자동완성 툴팁 노출) (tistory.com)](https://curryyou.tistory.com/319)

<br>