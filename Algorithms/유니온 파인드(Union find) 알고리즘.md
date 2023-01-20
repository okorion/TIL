## 동작 방법

1. union 연산 확인
   : 서로 연결된 두 노드를 확인
   1.1 A의 루트 노드 A'과 B의 루트 노드 B'를 찾기 (find)
   1.2 A'를 B'의 부모 노드로 설정 (A' < B')
2. 모든 union 연산을 처리할 때까지 1 반복

e.g.
{1,2,3,4,5,6}의 집합과 4개의 union 연산 *union 1,4 union 2,3 union 2,4 union 5,6*이 주어졌다.
이를 그래프로 표현하면,
![img](https://velog.velcdn.com/images%2Fwoo0_hooo%2Fpost%2F57361bd0-91fc-4ac2-bdf6-b0e781b8c884%2FIMG_31AF69E3B899-1.jpeg)
위와 같이 구성됨을 알 수 있다.

이를 완성하기 위한 구체적인 알고리즘 동작 방법은 아래와 같다.

1. 부모 테이블 초기화
   노드의 개수 크기의 부모 테이블을 초기화 한다. 초기값은 자기 자신을 부모로 가지도록 설정한다.

   | 노드번호 | 1    | 2    | 3    | 4    | 5    | 6    |
   | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
   | 부모     | 1    | 2    | 3    | 4    | 5    | 6    |

2. 각각의 union 연산을 확인한다. -> union 1,4
   1과 4의 루트노드를 각각 찾는다. 현재 루트 노드는 각각 1과 4이므로 더 큰 번호인 루트 노드 4의 부모를 1로 설정

   | 노드번호 | 1    | 2    | 3    | 4    | 5    | 6    |
   | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
   | 부모     | 1    | 2    | 3    | 1    | 5    | 6    |

3. union 2,3

   | 노드번호 | 1    | 2    | 3    | 4    | 5    | 6    |
   | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
   | 부모     | 1    | 2    | 2    | 1    | 5    | 6    |

4. union 1,2

   | 노드번호 | 1    | 2    | 3    | 4    | 5    | 6    |
   | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
   | 부모     | 1    | 1    | 2    | 1    | 5    | 6    |

5. union 5,6

   | 노드번호 | 1    | 2    | 3    | 4    | 5    | 6    |
   | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
   | 부모     | 1    | 1    | 2    | 1    | 5    | 5    |

-> 모든 union 연산을 수행한 결과

## 소스코드

코드로 구현하면 아래와 같다.

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```





참고링크: [[알고리즘\] union-find 알고리즘 (velog.io)](https://velog.io/@woo0_hooo/알고리즘-union-find-알고리즘)