## 👋 드로우 콜(Draw call)이란

드로우 콜이란 CPU가 GPU에게 오브젝트를 그리라고 명령하는 것을 의미한다.

 <br>

#### CPU가 GPU에게 오브젝트를 그리라고 명령하는 과정

Data는 Data 저장 장치에 저장된다.(HDD, SSD 등) CPU에도 CPU Memory가 있고 GPU에도 GPU Memory가 있다. (모바일에서는 물리적으로 나눠지지 않고 논리적으로 나눠서 사용한다.)

GPU는 CPU에 의해서 처리되고 GPU가 Mesh를 렌더링 할 때 지오메트리 데이터를 읽어오는 공간이 바로 GPU Memory이다. 따라서 Mesh를 그리기 위해서는 GPU Memory에 Mesh 관련 정보가 있어야 한다.

 <br>



![img](https://blog.kakaocdn.net/dn/SZmes/btrHdHFgVnf/kYys502bRkukrKuAJQJJ9K/img.png)

<br>

위의 그림처럼 저장장치에 있는 데이터를 복사하여 CPU Memory에 데이터를 올린다. 하지만 GPU는 CPU Memory에 접근할 수 없기 때문에 GPU Memory에 데이터를 다시 복사한다. 이 과정을 거쳐 GPU Memory에는 메쉬 정보가 저장된다.

또한 GPU는 결국 그려야하는 상태 정보를 담는 테이블이 있는데 이 테이블을 렌더 상태 테이블이라고 한다. 렌더 상태 테이블에는 버텍스, 메쉬, 쉐이더 등의 상태 정보가 담겨 있다.

이 상태 정보를 CPU는 GPU에게 전달하고 GPU는 렌더 상태 정보를 저장한다. 마지막으로 CPU는 GPU에게 그리라고 명령하는데 이를 DP Call이라고 한다.

 <br>

또한 CPU는 GPU에게 바로 명령을 하지 않고 Command 버퍼라는 곳에 명령 버퍼를 저장한다. 그러면 GPU는 할 일을 처리한 후에 Command 버퍼에서 명령을 순차적으로 가져가서 수행한다. (이때 FIFO 구조로 데이터를 불러온다)

<br>

<br>

#### 참고링크: [드로우 콜(Draw call)과 배칭(Batching) 간단 정리 (tistory.com)](https://jeonhw.tistory.com/28)

<br>