## bisect 라이브러리란?

**bisect 라이브러리**는 **원소들이 정렬된 리스트에서 특정 원소를 찾을 때 효과적**입니다. bisect 라이브러리는 아래 2가지 함수가 가장 중요합니다.

 

**(1) bisect_left(list, data):** 리스트에 데이터를 삽입할 가장 왼쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지).

**(2) bisect_right(list, data):** 리스트에 데이터를 삽입할 가장 오른쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지).

 

예를 들어, ***그림 1*** 과 같이 a라는 리스트 [1,2,3,3,5,10] 가 있을 때, 새로운 데이터 3을 삽입하려고 할 때의 bisect_left()와 bisect_right() 함수는 각각 2 와 4 를 반환합니다.

 



![img](https://blog.kakaocdn.net/dn/mgcHI/btq2CkXhyhK/8xuJer8yUM54BiRvtI8G80/img.png)그림 1. bisect 함수 동작 예제



 

위의 예제를 파이썬으로 구현하면 다음과 같습니다.

```
from bisect import bisect_left, bisect_right

a = [1, 2, 3, 3, 5, 10]
x = 3

print(f"bisect_left: {bisect_left(a, x)}") # 2
print(f"bisect_right: {bisect_right(a, x)}") # 4
```

 

이와 같은 두 함수의 특성 덕분에 bisect_left()와 bisect_right()는 **원소들이 정렬된 리스트에서 특정 범위 내에 속하는 특정 값의 개수를 구할 때 효과적**이며 ***�(����)*** 으로 빠르게 계산할 수 있다는 장점이 있습니다. 이러한 특성을 살려 특정 범위 내에 속하는 특정 값의 개수를 구하는 예제를 살펴보겠습니다.

 

```
from bisect import bisect_left, bisect_right

# [left_v, right_v] 범위 내에 있는 원소 개수 출력 함수
def cnt_within_range (arr, left_v, right_v):
    # 맨 좌측 인덱스
    left_idx = bisect_left(arr, left_v)
    # 맨 우측 인덱스
    right_idx = bisect_right(arr, right_v)
    return right_idx - left_idx

# 리스트 생성
arr = [5, 6, 7, 7, 7, 7, 8, 8, 9, 10]

# 값이 9인 원소 개수 출력
print(cnt_within_range(arr, 9, 9)) # 1
# [4, 7] 범위 내에 있는 원소 개수 출력
print(cnt_within_range(arr, 4, 7)) # 6
```



참고링크: [[파이썬\] 이진 탐색 구현을 도와주는 bisect 라이브러리에 대해 알아보자! (tistory.com)](https://heytech.tistory.com/79)