## **다익스트라 알고리즘** 구현

**특정한 노드에서 출발하여 각 다른 노드까지의 최단 경로를 구해주는 알고리즘**

다만, 음의 간선이 없을때 정상작동이 된다.

이때, **최단 거리 테이블** 개념이 사용된다.

```
import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

#노드의 개수, 간선의 개수
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1) #최단 거리 테이블

#간선 입력
for _ in range(m) :
  a, b, c = map(int, input().split()) #a->b 간선의 비용 : c
  graph[a].append((b, c))

def dijkstra(start) :
  #큐를 설정하여 시작점을 큐에 넣는다
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  #큐가 빌때까지 반복하여 실시한다
  while q :
    #최단거리, 해당 노드를 가져온다
    dist, now = heapq.heappop(q)

    #이미 처리된 값인 경우 무시한다
    if distance[now] < dist :
      continue
    
    #인접한 노드 개수만큼 반복한다
    for i in graph[now] :
      cost = dist + i[1] #i[0] : 노드값, i[1] : 간선비용

      #갱신값이 작은경우 갱신한다
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1) :
  if distance[i] == INF :
    print("INFINITY")
  else :
    print(distance[i])
```

이 코드가 작동되는 원리를 간단히 설명하면

 

방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 고른다 (heapq 구조를 사용해 자동으로 가져와진다)

이 노드를 기준으로 인접한 모든 노드에 대해, 현재 노드 + 연결된 간선값을 통한 새로운 거리값과, 기존에 저장된 거리값을 비교를 통해

적은값으로 계속하여 갱신된다.

이러한 과정을 heapq가 없을때까지 반복하면 최종적으로 각 노드의 거리값의 최소값만 저장되어 있다.



참고링크: [이것이 코딩 테스트다 - Chapter9 최단 경로 정리 (tistory.com)](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter9-최단-경로-정리)







**최단 경로 알고리즘**은 지하철 노선도, 네비게이션 등 다방면에 사용되는 알고리즘입니다. 이번 시간에는 **Python**을 이용해 **하나의 시작 정점**으로 부터 **모든 다른 정점까지의 최단 경로**를 찾는 최단 경로 알고리즘인 **다익스트라(dijkstra) 알고리즘**에 대해서 알아 보려고 합니다.

## 목차

> 1. 최단 경로 알고리즘의 아이디어
> 2. 사전 배경 지식
> 3. 코드 구현



## 최단 경로 알고리즘의 아이디어

최단 경로 알고리즘의 아이디어는 다음과 같습니다. 자료 구조로는 `graph` 를 사용하며, **노드**와 **가중치를 가진 간선** 을 이용하여 실제 거리를 표현합니다. 알고리즘을 간단하게 설명 하자면, 다음과 같습니다.

> 1. 출발 노드와, 도착 노드를 설정
> 2. 알고 있는 모든 거리 값을 부여
> 3. 출발 노드부터 시작하여, 방문하지 않은 인접 노드를 방문, 거리를 계산한 다음, 현재 알고있는 거리보다 짧으면 해당 값으로 갱신한다.
> 4. 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드는 방문한 것이므로, 미방문 집합에서 제거한다.
> 5. 도착 노드가 미방문 노드 집합에서 벗어나면, 알고리즘을 종료한다.

## 사전 배경 지식

다익스트라 알고리즘을 실행 하는 중에는 **방문하지 않은 인접 노드**를 방문하는 부분이 있습니다. 이 부분에서 **우선순위 큐**를 사용 하면, **지금까지 발견된 가장 짧은 거리의 노드에 대해서 먼저 계산**할 수 있으며, **더 긴 거리로 계산 되었을 시 스킵** 또한 가능합니다.

우선순위 큐는 `heapq` 모듈을 이용해 구현 할 수 있습니다.

https://justkode.kr/python/pygorithm-2 (heapq 부분 참조)

## 코드 구현

- 출발 노드와, 도착 노드를 설정 (전체 거리를 알고 싶을 때는, 출발 노드만 설정 하여도 무방)
- 알고 있는 모든 거리 값을 부여 (`Python`에서는 `dictionary` 객체를 이용하여 `graph`를 표현 할 수 있다.)

```python
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
```



- 출발 노드부터 시작하여, 방문하지 않은 인접 노드를 방문, 거리를 계산한 다음, 현재 알고있는 거리보다 짧으면 해당 값으로 갱신한다.
- 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드는 방문한 것이므로, 미방문 집합에서 제거한다.

```python
import heapq  # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
  return distances
```



- 실행 결과

**in**

```python
print(dijkstra(graph, 'A'))
```

**out**

```terminal
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
```





참고링크: [Python으로 다익스트라(dijkstra) 알고리즘 구현하기 (justkode.kr)](https://justkode.kr/algorithm/python-dijkstra)