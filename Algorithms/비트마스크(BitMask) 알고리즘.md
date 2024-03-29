## 🎭 비트마스크(BitMask) 알고리즘이란?

<br>

#### **[목차]**

*1. 비트마스크(BitMask)란?*

*2. 비트마스크의 장점*

*3. 비트 연산자*

*4. 비트마스크를 이용한 집합 구현*

 

 <br>

\* 종만북에 잘 설명되어 있어 기본적으로 종만북의 설명을 따릅니다. 

 <br>

 <br>

###  1. 비트마스크(BitMask)란?

\- 비트마스크(BitMask)는 이진수를 사용하는 컴퓨터의 연산 방식을 이용하여, **정수의 이진수 표현을 자료 구조로 쓰는 기법**을 말한다. 

 <br>

\- 이진수는 0 또는 1을 이용하므로 하나의 비트(bit)가 표현할 수 있는 경우는 두 가지이다. 

 <br>

\- 보통 어떤 비트가 1이면 "켜져 있다"라고 말하며, 0이면 "꺼져 있다"라고 말한다. 

 <br>

 <br>

###  2. 비트마스크의 장점

 <br>

비트마스크는 크게 어려운 개념이 아니며, 이 개념을 알고 있다면 매우 유용한 경우가 꽤나 있다. 비트마스크의 장점들은 다음과 같다.

 <br>

**1. 수행 시간이 빠르다.** 

비트마스크 연산은 bit 연산이기 때문에 **O(1)**에 구현되는 것이 많다. 따라서 다른 자료구조를 이용하는 것보다 훨씬 빠르게 동작하게 된다. 

다만, 비트마스크를 이용하는 경우에는 비트의 개수만큼 원소를 다룰 수 있기 때문에 연산 횟수가 적은 경우에는 속도에 큰 차이가 없지만, 연산 횟수가 늘어날수록 차이가 매우 커지게 된다. 

 <br>

**2. 코드가 짧다.**

다양한 집합 연산들을 비트연산자로 한 줄로 작성할 수 있기 때문에 반복문, 조건문 등을 이용한 코드보다 훨씬 간결한 코드를 작성할 수 있다.

 <br>

**3. 메모리 사용량이 더 적다.**

개인적으로, 비트마스크를 이용하는 가장 큰 이유라고 생각한다.

간단한 예시로, bit가 10개인 경우에는 각 bit당 두 가지 경우를 가지기 때문에 210210가지의 경우를 10bit 이진수 하나로 표현이 가능하다. 

이처럼 하나의 정수로 매우 많은 경우의 수를 표현할 수 있기 때문에 메모리 측면에서 효율적이며, 더 많은 데이터를 미리 계산해서 저장해 둘 수 있는 장점이 있다. (*DP에 매우 유용하다*)

 <br>

 <br>

###  3. 비트 연산자

 <br>

비트마스크를 이용하기 위해서, 정수 변수를 비트 별로 조작할 수 있는 비트연산자를 사용한다. 두 정수 변수 또는 하나의 정수 변수를 이용하여 새로운 값을 만들어 내는 것이 목적이다. 

 <br>

**1. AND 연산**

두 정수 변수 a와 b를 통해서 c를 생성한다고 가정하면, a와 b를 한 bit씩 비교하면서 해당 비트가 **둘 다 켜져 있는 경우**에만 c의 해당 비트를 켠다.

C에서 제공하는 연산자 기호는 ' & '이다.

(ex. c = a & b)

 <br>

**2. OR 연산**

AND 연산과 같은 방식으로, 해당 비트가 **둘 중 하나라도 켜져 있는 경우**에 c의 해당 비트를 켠다.

C에서 제공하는 연산자 기호는 ' | (shift + \) ' 이다.

(ex. c = a | b)

 <br>

**3. XOR 연산**

마찬가지로 같은 방식이며, 해당 비트가 **둘 중 하나만 켜져 있는 경우**에 c의 해당 비트를 켠다.

C에서 제공하는 연산자 기호는 ' ^ ' 이다.

(ex. c = a ^ b)

 <br>

**4. NOT 연산**

정수 하나를 입력받아서 **켜져 있는 비트는 끄고, 꺼져 있는 비트는 켠 결과**를 반환한다.

C에서 제공하는 연산자 기호는 ' ~ ' 이다.

(ex. c = ~a)

 <br>

**5. 시프트(shift) 연산**

시프트 연산자는 정수 a의 **비트들을 왼쪽 또는 오른쪽으로 원하는 만큼 움직인다**. 움직이고 나서 빈자리는 0으로 채워지게 된다. 예를 들어 13 (1101)을 오른쪽으로 1bit 움직인다고 하면, 6 (0110)이 되는 것이다. 

C에서 제공하는 연산자 기호는 ' << ' 또는 ' >> ' 이다.

(ex. c = (a << 1) ) 

 <br>

아래는 실제 예시이다. 

 <br>



![img](https://blog.kakaocdn.net/dn/bBhDth/btqKWWFVcCx/SUJe1KjrZmPrFVrqf6BJgK/img.png)

![img](https://blog.kakaocdn.net/dn/exXN9k/btqKSWzTbb2/z8Far3MF4PoPaoUPSktnkk/img.png)

<br>

단, 비트 연산자를 이용할 때에는 주의해야 할 점이 있다.

첫 번째로, **C에서 비트 연산자들의 우선순위는 비교 연산자보다 낮다.** 따라서 원하는 답이 나오지 않을 가능성이 있다.

예를 들어서 c = (6 & 4 == 4) 라고 한다면, 4 == 4가 먼저 계산되어 1(true)을 반환하고, 따라서 c에는 6 & 1의 값이 할당되게 된다. 

따라서 비트 연산자를 이용할 때에는 항상 연산자마다 괄호를 씌워주는 것이 바람직하다. 

 <br>

두 번째로는, **오버플로우(Overflow) 문제이다.** 

250250 을 구하기 위해서 1<<50 으로 표현한다면, C에서는 1은 32bit 상수 취급하기 때문에 50번 왼쪽으로 shift하게 되면 overflow가 발생하게 된다. 따라서 1LL로 표현을 해주어야 한다. 

 <br>

이처럼 비트 연산자를 사용하는 경우엔 실수할 가능성이 매우 높기 때문에 주의해서 사용해야 한다. 

 <br>

 <br>

 <br>

###  4. 비트마스크를 이용한 집합 구현

 <br>

**비트마스크를 이용한 집합 구현**은 가장 대표적이고, 중요한 사례이다. "하나의 bit가 하나의 원소"를 의미하게 된다. 

bit가 켜져 있으면 해당 원소가 집합에 포함되어 있다는 의미이고, 꺼져 있으면 포함되어 있지 않다는 의미이다. 

따라서 N비트 정수 변수라면 N개의 원소를 갖는 집합의 부분집합들을 모두 표현할 수 있게 된다. 

원래는 N개의 boolean 원소를 갖는 배열을 선언해야 했지만, 비트마스크를 이용하면 정수 하나로 표현이 가능하기 때문에 사용하는 메모리의 크기가 많이 줄어드는 장점이 있다. 

이제 비트연산자를 통해서 집합을 어떻게 효율적으로 다룰 수 있는지 알아보자.

 <br>

우선, A라는 변수를 집합이라고 가정하고, 집합의 총원소의 개수를 10개라고 가정하겠다. (0번째 ~ 9번째 원소)

 <br>

| **연산**                       | **사용 예시**                                                |
| ------------------------------ | ------------------------------------------------------------ |
| **공집합과 꽉 찬 집합 구하기** | A = 0; / A = (1 << 10) - 1;                                  |
| **원소 추가**                  | A \|= (1 << k);                                              |
| **원소 삭제**                  | A &= ~(1 << k);                                              |
| **원소의 포함 여부 확인**      | if(A & (1 << k))                                             |
| **원소의 토글(toggle)**        | A ^= (1 << k);                                               |
| **두 집합에 대해서 연산**      | A \| B    → A와 B의 합집합 A & B   → A와 B의 교집합 A & (~B) → A에서 B를 뺀 차집합 A ^ B   → A와 B중 하나에만 포함된 원소들의 집합 |
| **집합의 크기 구하기**         | int bitCount(int A){  if(A == 0) return 0;  return A%2 + bitCount(A / 2); }  [내장 명령어] gcc/g++ → __builtin_popcount(A)  visual C++ → __popcnt(A) Java → Integer.bitCount(A) |
| **최소 원소 찾기**             | int first = A & (-A);                                        |
| **최소 원소 지우기**           | A &= (A - 1);                                                |
| **모든 부분 집합 순회하기**    | for (int subset = A ; subset ; subset = ((subset - 1) & A)){ } |

 <br>

**1) 공집합과 꽉 찬 집합 구하기**

\- 기본적으로 공집합은 bit가 모두 꺼진 상황이기 때문에 상수 0이 공집합을 표현한다. 

반대로 꽉 찬 집합은 bit가 모두 켜진 상황이기 때문에 1111111111(2) 의 값을 가져야 하는데, 이는 (1<<10) - 1 과 동일하다. 1<<10은 10000000000(2) 이므로 1을 빼면 10개의 bit가 모두 켜진 수를 얻을 수 있다.

 <br>

 <br>

**2) 원소 추가**

\- A 집합에 특정 원소를 추가하는 방법이다. 원소에 해당하는 bit만 켜야 하기 때문에 해당 bit를 항상 1로 만드는 연산이 필요하다. 따라서 **OR 연산**을 이용한다. 

이미 A에 원소가 포함되어 있는 경우에는 아무런 변화가 없게 된다. 

 <br>

 <br>

**3) 원소 삭제**

\- A 집합에 포함된 특정 원소를 삭제하는 방법이다. 원소에 해당하는 bit가 꺼져야 하기 때문에 해당 bit를 항상 0으로 만드는 연산이 필요하다. 

따라서 A -= (1<<k); 로 작성하면 된다. 하지만 이 경우는 A에 반드시 k번째 원소가 포함되어 있는 경우에만 가능하다. 만약 포함되어 있지 않은 경우에는 다른 원소의 포함 여부까지 바꿔버리기 때문이다. 

그러므로 A에 k번째 원소의 포함 여부와 상관없이 해당 bit를 끄기 위해서는 **AND연산**을 이용해야 한다. 

 <br>

1<<k는 k번째 bit만 켜진 상태이며, 여기에 NOT을 씌우면 k번째 bit만 꺼진 상태가 된다. 

그러므로 AND 연산을 적용하면 k번째 bit만 0이 되고 나머지 bit는 변함이 없다. 

 <br>

<br>

**4) 원소의 포함 여부 확인**

\- A 집합에 특정 원소가 포함되어 있는지 확인하는 방법이다. k번째 원소가 포함되어 있는지 확인하고 싶다면, k번째 bit가 켜져 있는지만 확인하면 된다. 

 <br>

 <br>

**5) 원소의 토글**

\- A 집합에 해당 원소가 빠져있는 경우에는 추가하고, 들어있는 경우에는 삭제하는 방법이다. **XOR 연산**을 이용한다.

 <br>

 <br>

**6) 두 집합에 대해 연산하기**

 \- 두 집합을 A와 B라고 한다면 비트연산자들을 통해서 A와 B의 교집합, 합집합, 차집합 등을 구할 수 있다. 

 <br>

 <br>

**7) 집합의 크기 구하기**

\- 집합에 포함된 원소의 크기를 구한다면 A에서 켜진 bit의 수를 구하면 될 것이다. 직접 모든 비트를 확인하면서 개수를 체크할 수도 있고, 내장 명령어를 이용할 수도 있다. 

<br>

<br>

**8) 최소 원소 찾기**

\- 집합에 포함된 가장 작은 원소 (index가 가장 작은 원소)를 찾는 방법이다. 켜져 있는 bit 중에서 가장 오른쪽에 있는 bit를 찾는 것이다. 비트마스크 뿐만 아니라 펜윅 트리 (Fenwick Tree)에서도 사용되는 기법이다. 

컴퓨터는 2의 보수를 이용하여 음수를 표현하기 때문에 -A를 표현하기 위해서 ~A + 1을 이용한다. 

A에서 가장 오른쪽에 켜진 bit의 인덱스를 k라고 한다면, k보다 오른쪽에 있는 모든 bit는 0이다. 

따라서 NOT 연산을 적용한 ~A는 k번째 bit는 0이고, 오른쪽의 모든 bit는 1이 된다. 

여기서 ~A에 1을 더해주게 되면 k번째보다 오른쪽에 있는 bit는 모두 0이 되고, k번째 bit는 1이 된다. k번째 bit보다 왼쪽에 있는 bit는 아무런 변화가 없다. 

따라서 -A와 A를 AND 시키면 k번째 bit만 켜진 상태로 남게 된다. 

<br>

<br>

**9) 최소 원소 지우기**

\- 가장 오른쪽에 켜져 있는 bit를 지우고 싶다면 A-1과 AND시키면 된다. A에서 1을 빼주게 되면 가장 오른쪽에 있던 bit는 0이 되고 그보다 오른쪽에 있는 모든 bit들이 1이 되기 때문이다. 

<br>

<br>

**10) 모든 부분 집합 순회하기**

\- A의 모든 부분 집합을 탐색하는 방법이다. 

위의 설명들을 토대로 코드에 직접 예시를 넣어보면 쉽게 이해가 갈 것이다. 

<br>

<br>

<br>

#### 참고링크: [비트마스크 (BitMask) 알고리즘 (rebro.kr)](https://rebro.kr/63)

<br>