## 🥢 동시성 vs 병렬성

## 동시성(Concurrency) vs 병렬성(Parallelism)

| 동시성                                                     | 병렬성                                                    |
| ---------------------------------------------------------- | --------------------------------------------------------- |
| 동시에 실행되는 것 같이 보이는 것                          | 실제로 동시에 여러 작업이 처리되는 것                     |
| 싱글 코어에서 멀티 쓰레드(Multi thread)를 동작 시키는 방식 | 멀티 코어에서 멀티 쓰레드(Multi thread)를 동작시키는 방식 |
| 한번에 많은 것을 처리                                      | 한번에 많은 일을 처리                                     |
| 논리적인 개념                                              | 물리적인 개념                                             |

먼저 동시성과 병렬성의 차이를 표로 살펴보았습니다. 그러나 표로만 봐서는 조금 잘 안 와닿는 면이 있어서 몇가지 그림을 통해 좀 더 살펴 보겠습니다.

![img](https://t1.daumcdn.net/cfile/tistory/99AD02405FBBB94910)

처음으로 보이는 이 그림은 직관적으로 잘 설명이 되어 있습니다. 동시적으로 실행되는 것과 병렬로 실행되는 것과 함께 추가적으로 2개의 작업이 순차적으로 실행되는 모습도 나와있습니다.

두번째 그림은 싱글 코어와 멀티 코어에서 동작하는 모습을 비교하는 그림입니다.

![img](https://t1.daumcdn.net/cfile/tistory/995359405FBBB9591C)

싱글 코어에서는 2개의 작업을 동시에 실행되는 것 처럼 보이기 위해 번갈아 가면서 작업을 수행합니다. 이때 다른 작업으로 바꾸어 실행할 때 내부적으로 [Context switch](https://en.wikipedia.org/wiki/Context_switch)가 일어납니다. 이 부분은 링크에 들어가보시면 더 자세한 내용을 살펴보실 수 있습니다.

마지막 그림은 실생활과 관련된 그림을 살펴보겠습니다.

![img](https://t1.daumcdn.net/cfile/tistory/99972F3C5FBBB96E1A)

이 그림을 보면 하나의 커피머신이 있는데 커피를 받기 위한 사람들의 줄이 2줄로 되어 있습니다. 그래서 서로 번갈아가면서 커피를 타게 되는 것이죠. 이러한 것을 동시성 처리라고 정의하고 있습니다. 반면에 병렬 처리의 경우는 2개의 커피 머신이 있고 각 커피 머신마다 하나의 줄을 가지고 있어서 각각의 줄마다 커피를 받을 수 있는 것을 병렬 처리라고 할 수 있습니다. 

그림을 예로 들면서 보니 잘 이해가 됩니다. 이렇게 3가지 그림을 통해 동시성과 병렬성에 대해서 알아보았습니다.

## References

- [parallelism concurrency](http://www.dietergalea.com/parallelism-concurrency/)
- [Concurrency vs Parallelism](https://www.codeproject.com/Articles/1267757/Concurrency-vs-Parallelism)
- [concurrent and parallel programming](https://joearms.github.io/published/2013-04-05-concurrent-and-parallel-programming.html)





<br>

<br>

#### 참고링크: [동시성(Concurrency) vs 병렬성(Parallelism) (tistory.com)](https://seamless.tistory.com/42)

<br>