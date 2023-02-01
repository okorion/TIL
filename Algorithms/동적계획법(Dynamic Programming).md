# 다이나믹 프로그래밍(Dynamic Programming)이란?

- DP란 **'동적 계획법'**이라고도 불리는 알고리즘
- **큰 문제를 작은 문제로 나누어 푸는 문제를 일컫는 말** / 한 번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘
- DP는 다음의 조건을 만족할 때 사용할 수 있음
  1. **최적 부분 구조 (Optimal Substructure)**
     큰 문제를 작은 문제로 나눌 수 있고, 작은 문제의 답을 모아 큰 문제를 해결할 수 있는 경우를 의미
  2. **중복되는 부분 문제 (Overlapping Subproblem)**
     동일한 작은 문제를 반복적으로 해결해야 하는 경우



**※** 일반적인 프로그래밍 분야에서 **동적(Dynamic)**의 의미는?

- 자료구조에서 동적 할당(Dynamic Allocation)은 '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미한다.
- 반면에 DP에서 Dynamic은 별다른 의미가 없다. 알고리즘을 만든 사람도 멋있다는 이유로 Dynamic이란 단어를 프로그래밍에 결합했다.



피보나치 수열을 점화식으로 표현해보자.

![img](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2F0f9c8ab0-9abd-492f-942b-76381e3ec410%2Fimage.png)

수학적 점화식을 프로그래밍으로 표현하려면 단순 재귀함수를 사용하면 간단하다. Python 코드로 작성해보자.

```python
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
>> 3
```

재귀함수의 호출을 그림으로 표현하면 아래와 같다.

![img](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2F15857380-5742-42a1-aa0d-25c35b3fa8e7%2Fimage.png)

### 피보나치 수열을 단순 재귀함수로 구현했을 때의 문제점

위와 같이 코드를 작성하게 되면 심각한 문제가 생길 수 있다. `f(n)`함수에서 `n`이 커지면 커질수록 수행 시간이 기하급수적으로 늘어나기 때문이다. 아래 그림을 보자.

![img](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2Fd90e2e4d-1a1f-43f2-82e2-edd9f629aeab%2Fimage.png)

`f(6)`을 계산할 때에 그림과 같이 `f(2)`가 여러 번 호출되는 것을 확인할 수 있다. *(중복되는 부분 문제)* 즉, 같은 연산을 여러 번 수행하므로 시간 복잡도가 엄청 커지게 된다.

피보나치 수열의 시간 복잡도는 `O(2 ** N)`이다. 예를 들어 `f(30)`을 계산하기 위해 약 10억번의 연산을 수행해야 한다. 우리는 DP를 사용하면 이러한 문제를 효율적으로 해결할 수 있다.



### DP로 피보나치 수열 계산하기

DP는 항상 사용할 수 없기 때문에 DP의 사용 조건을 만족하는지 확인해보자.

1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

피보나치 수열은 위 2가지 조건을 만족하므로 DP를 사용할 수 있다! 이 문제를 메모이제이션 (Memoization) 기법을 사용해서 해결해보자.

> **※ 메모이제이션 (Memoization) 이란?**
>
> - DP를 구현하는 방법 중 한 종류이다.
> - 한 번 구한 결과를 메모리 공간에 메모해두고 --> 같은 식을 호출하면 메모한 결과를 그대로 가져오는 기법이다. (값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 한다.)

```python
# 메모이제이션하기 위한 리스트 초기화
memoization = [0] * 100


# 피보나치 함수를 재귀함수로 구현 (Top-down DP)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있으면 그대로 반환
    if memoization[x] != 0:
        return memoization[x]
    # 계산한 적 없으면 점화식에 따라 피보나치 결과 반환
    memoization[x] = fibo(x - 1) + fibo(x - 2)
    return memoization[x]


print(fibo(6))
```

메모이제이션을 사용하여 `f(6)`을 구하는 과정은 아래의 그림과 같다.

![img](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2Fc14e7275-a0c3-4ec2-b3d7-e885a2bb0757%2Fimage.png)

메모이제이션을 사용하게 되면 그림의 색칠된 노드만 방문하게 된다.



실제 코드에서 호출되는 함수만 보게되면 아래의 그림과 같이 방문한다.

![img](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2Fe026ab38-eeab-442d-b9b9-8b6316d470c8%2Fimage.png)

> ```
> f(6) -> f(5) -> f(4) -> f(3) -> f(2) -> f(1) -> f(2) -> f(3) -> f(4)
> ```

DP를 적용했을 때의 피보나치 수열 알고리즘의 시간 복잡도는 `O(N)`이다. 왜냐하면 `f(1)`을 구한 다음 그 값이 `f(2)`를 구하는 데 사용되고, `f(2)`의 값이 `f(3)`을 푸는 데 사용되는 방식으로 이어지기 때문이다. 또한, 메모이제이션 때문에 한 번 구한 결과는 다시 구해지지 않는다.





참고링크: [[알고리즘\] 다이나믹 프로그래밍 (Dynamic Programming) (velog.io)](https://velog.io/@kimdukbae/다이나믹-프로그래밍-Dynamic-Programming)