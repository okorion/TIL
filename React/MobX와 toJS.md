## 🏃‍♂️ MobX와 toJS



Mobx에서 observable을 이용해 만들어진 배열은 유사 배열 이기 때문에 실제 배열처럼 전환 하려면

toJS() 메소드를 사용해야 한다.

- 일반 자바스크립트 객체로 변환 -> toJS()

 

 <br>

**toJS() 사용 전**

Proxy {0: Proxy, 1: Proxy, 2: Proxy, 3: Proxy, 4: Proxy, 5: Proxy, 6: Proxy, 7: Proxy, 8: Proxy, 9: Proxy, Symbol(mobx administration): ObservableArrayAdministration}



![img](https://blog.kakaocdn.net/dn/nqkfX/btqISuKiXXb/lk4t0Mf1HunS6ljLYJoHuk/img.png)



 <br>

**toJS() 사용 후**



![img](https://blog.kakaocdn.net/dn/b1jLdx/btqILLNnyX3/ZJ8O082KALjrqvsCXVb9yk/img.png)



 <br>

 <br>

#### 참고링크: [[React\] Mobx와 toJS (tistory.com)](https://bbangaro.tistory.com/6)

 <br>