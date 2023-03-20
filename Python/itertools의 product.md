### [1) itertools.product()](https://soundprovider.tistory.com/entry/python-itertools#--%--itertools-product--)

itertools.product()는 두개 이상의 리스트(or 집합) 끼리의 데카르트 곱(cartesian product)를 계산하여 iterator로 반환해준다. Cartesian Product는 아래와 같이 정의된다.



A×B={(x,y)| x∈A and y∈B}



```
import itertools

A = [1,2,3]
list(itertools.product(A, repeat=2))
>>>> [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print(itertools.product(A, repeat=2))
>>>> <itertools.product object at 0x7fa24fddc7e0>

A = [[1,2,3], [4, 5]]
list(itertools.product(*A))
>>>> [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

A = [1,2,3]
B = [4,5]
print(itertools.product(A, B))
>>>> <itertools.product object at 0x7fa24fddc7e0>
```

 

참고링크: [[python\] itertools — 끄적끄적 (tistory.com)](https://soundprovider.tistory.com/entry/python-itertools)