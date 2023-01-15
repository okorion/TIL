## 클래스 임포트

우선 `PriorityQueue` 클래스는 `queue` 내장 모듈에서 제공되기 때문에 파이썬만 설치되어 있으면 별다른 추가 설치없이 임포트할 수 있습니다.

```py
from queue import PriorityQueue
```

## 우선순위 큐 생성

`PriorityQueue()` 생성자를 이용해서 비어있는 우선순위 큐를 초기화할 수 있습니다.

```py
que = PriorityQueue()
```

우선순위 큐의 디폴트 사이즈는 무한대입니다. 만약에 특정 최대 크기를 가진 우선순위 큐가 필요하다면 `maxsize`를 넘기면 됩니다.

```py
que = PriorityQueue(maxsize=8)
```

## 우선순위 큐에 원소 추가

`PriorityQueue` 클래스의 `put()` 메서드를 이용하여 우선순위 큐에 원소를 추가할 수 있습니다.

```py
que.put(4)
que.put(1)
que.put(7)
que.put(3)
```

## 우선순위 큐에 원소 삭제

`PriorityQueue` 클래스의 `get()` 메서드를 이용하여 우선순위 큐에 원소를 삭제할 수 있습니다.

```py
print(que.get())  # 1
print(que.get())  # 3
print(que.get())  # 4
print(que.get())  # 7
```

`get()` 메서드는 삭제된 원소를 리턴하기 때문에, 위와 같이 출력을 해보면, 크기 순서대로 원소가 삭제됨을 알 수 있습니다.

## 정렬 기준 변경

만약 단순 오름차순이 아닌 다른 기준으로 원소가 정렬되기를 원한다면, `(우선순위, 값)`의 튜플의 형태로 데이터를 추가하고 제거하면 됩니다.

```py
que.put((3, 'Apple'))
que.put((1, 'Banana'))
que.put((2, 'Cherry'))

print(que.get()[1])  # Banana
print(que.get()[1])  # Cherry
print(que.get()[1])  # Apple
```

## 마치면서

지금까지 파이썬의 내장 자료구조인 우선순위 큐(PriorityQueue)를 사용하는 방법에 대해서 알아보았습니다. 참고로, 내부적으로 `heap` 모듈을 사용하는 `PriorityQueue` 클래스의 `put()`, `get()` 함수는 `O(log n)`의 시간 복잡도를 가집니다.





[파이썬의 우선순위 큐(PriorityQueue) 사용법 | Engineering Blog by Dale Seo](https://www.daleseo.com/python-priority-queue/)



