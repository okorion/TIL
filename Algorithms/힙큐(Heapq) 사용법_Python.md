## Heapq

자세한 내용은 https://docs.python.org/ko/3/library/heapq.html 참조

- 최소 힙(Min Heap)의 구조
- 모든 k에 대해 `heap[k] <= heap[2*k+1]` 또는 `heap[k] <= heap[2*k+2]` 만족
- 가장 작은 요소가 `heap[0]`에 위치
- 힙을 만들기 위해서는, 초기화된 리스트 `[]`를 사용하거나, `heapify`를 통해 값이 들어있는 리스트를 힙으로 변환 가능

```python
import heapq

hq = []
```



#### push

- `heapq.heappush(heap, item)`
- 힙의 형태를 유지하면서 item을 push

```python
heapq.heappush(hq, 4)
heapq.heappush(hq, 1)
heapq.heappush(hq, 3)
heapq.heappush(hq, 7)
```



#### pop

- `heapq.heappop(heap)`
- 힙의 형태를 유지하면서 가장 작은 항목을 pop, 반환
- 비어있으면 IndexError 발생
- 반환하지 않고 접근하고 싶다면, `heap[0]` 활용

```python
heapq.heappop(hq) # 1
```



#### heapify

- `heapify(x)`
- 리스트 x를 선형 시간으로 제자리에서 heap으로 변환

```python
x = [4, 3, 1, 2, 5, 6]
print(x) # [4, 3, 1, 2, 5, 6]
heapq.heapify(x)
print(x) # [1, 2, 4, 3, 5, 6]
```





참고링크: [[Python\]우선순위 큐, heapq (velog.io)](https://velog.io/@mein-figur/Python우선순위-큐-heapq)