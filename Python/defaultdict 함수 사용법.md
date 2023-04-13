<br>

### 🎇 [Python] 딕셔너리 defaultdict 함수 사용법

<br>

```python
animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
dic = {}

for animal in animals:
    dic[animal] += 1
```

<br>

![img](https://blog.kakaocdn.net/dn/cnoYLu/btrpdpazWU6/T9h8dMBbbD4E8yGlUYc6F0/img.png)

<br>

다음과 같이 딕셔너리에 접근할 때, 존재하지 않는 key에 대해 접근할 경우 keyError가 발생한다. 따라서 반드시 key 값이 먼저 존재하는지 여부를 파악하고 없다면 초기화를 하여 에러를 막아야 한다. 

 <br>

 <br>

#### **기본적인 딕셔너리 사용법** 

```bash
animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
dic = {}

for animal in animals:
    # key가 있다면 1 증가
    if animal in dic.keys():
        dic[animal] += 1
    # key가 없다면 1로 초기화
    else:
        dic[animal] = 1

print(dic)
```

<br>

![img](https://blog.kakaocdn.net/dn/oLuQ1/btrpcO9ufvN/2tECK4cPrHMFtCD5CDrUm1/img.png)

<br>

위처럼 해당 key 값이 존재하는지 조건문을 통해 파악하고 만약 딕셔너리 내부에 key 값이 없다면 1로 초기화하는 작업을 수행해야 한다. 하지만 collection 모듈의 defualdict을 사용하면 key 값이 존재하지 않아도 내부적으로 디폴트 값을 줄 수 있어 이러한 작업을 생략할 수 있다. 아래의 예시를 통해 살펴보자. 

 <br>

 <br>

 <br>

 <br>

**defualt 값을 int로 주었을 때 defualtdict 사용법**

```python
from collections import defaultdict

animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
dic = defaultdict(int)

for animal in animals:
    dic[animal] += 1

print(dic)
print(dic['door'])
print(dic)
```

<br>

![img](https://blog.kakaocdn.net/dn/bHFCXr/btro7C2HOjl/GJwqDZoDqlr1ElPh0QYOJK/img.png)

<br>

for문에서 key 검사 여부를 하지 않았지만 딕셔너리에 key 값을 추가하여 자동적으로 value값을 1씩 증가한 사실을 파악할 수 있다. defualtdict을 사용하면 key가 존재하지 않아도 에러를 발생하지 않고 처음 선언했을 때의 자료형에 대한 초기값을 세팅해준다. 위에서는 defualtdict()의 매개변수로 int를 추가하여 초기값을 0으로 세팅해주었다. 

 <br>

하지만 dic['door'] 과 같이 animal에 포함되지 않은 데이터에 대해 접근할지라도 해당 딕셔너리에 원소로 추가되기 때문에 사용에 있어 주의가 필요하다. 

 <br>

 <br>

 <br>

#### **defualt 값을 set으로 주었을 때 defualtdict 사용법**

```python
from collections import defaultdict

animals = [('dog', 'Ricky'), ('cat', 'Momo'), ('rabbit', 'Jimmy'), ('cat', 'Chars'), ('cat', 'Pipy')]
dic = defaultdict(set)

for animal, name in animals:
    dic[animal].add(name)

print(dic)
```

 <br>

<br>

![img](https://blog.kakaocdn.net/dn/cdXmWJ/btro09NJlzD/4IBEaUTlRZghkJcs7LnzLK/img.png)

<br>

이번 예제에서는 디폴트 값으로 set을 주었기에 딕셔너리 value의 자료형은 set이 된다. 따라서 dic[animal]에 접근할 경우 해당 자료형이 set이므로 add() 함수를 사용하여 원소에 접근해야 한다. 

 <br>

 <br>

 <br>

#### **defualt 값을 list로 주었을 때 defualtdict 사용법**

```go
from collections import defaultdict

animals = [('dog', 'Ricky'), ('cat', 'Momo'), ('rabbit', 'Jimmy'), ('cat', 'Chars'), ('cat', 'Pipy')]
dic = defaultdict(list)

for animal, name in animals:
    dic[animal].append(name)

print(dic)
```

<br>

![img](https://blog.kakaocdn.net/dn/cduBvM/btrpfgjVsSv/w9tB3JjbMVlYlVeY5yKkGK/img.png)

<br>

마찬가지로 이번에는 딕셔너리의 디폴트 값이 list이므로 append를 이용하여 원소를 추가하였다. 

<br>

<br>

<br>

#### 참고링크: https://dogsavestheworld.tistory.com/entry/python-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-defaultdict-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95

<br>