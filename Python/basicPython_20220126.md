# 1. Type Class (Python에서 기본적으로 정의되어 있는 클래스 5가지 작성)
* List, Dictionary, Tuple, int, float


# 2. Magic Method  #`__`가 있는 메서드는 특별한 목적을 위해 만들어진 메서드이기 때문에 Special Method 혹은 Magic Method 라고 불림.

    __init__, __del__, __str__, __repr__


* `__init__` : 생성자(constrictor) 메서드로 인스턴스 객체가 생성될 때 자동으로 호출되는 함수.
* `__del__` : 소멸자(destructor) 메서드로 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되는 함수.
* `__str__`: 특정 객체를 출력(`print()`)할 때 보여줄 내용을 정의할 수 있음.
* `__repr__` : 특정 객체의 출력을 문자열의 형태로 반환하는 함수.


# 3. Instance Method
* `self` : 호출 시 첫 번째 인자로 인스턴스 자신이 전달되도록 설계.
* `__init__` : 인스턴스 객체가 생성될 때 자동으로 호출되도록 설계.
* `__del__` : 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되도록 설계.
  

# 4. Module Import
    # fibo.py

    def fibo_recursion(n):
        if n < 2:
            return n
        else:
            return fibo_recursion(n-1) + fibo_recursion(n-2)

* 위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때 아래와 같은 형태로 함수를 실행할 수 있도록 하는 import 문을 빈칸 (a), (b), (c)를 채워넣기

    from __(a)__ import __(b)__ as __(c)__

    recursion(4)
    
* (a) : fibo.py
* (b) : fibo_recursion
* (c) : recursion

* * *

# 1.pip (1) 무엇을 위한 명령인지 (2) 실행은 어디에서 해야하는지 작성
    $ pip install faker

> * faker 모듈/ 패키지 => 그 안의 Faker 클래스를 꺼낸다.
>     from faker import Faker
>
>     fake = Faker()  # Faker는 클래스, fake는 인스턴스이다. 
>     fake.name()  # .name()은 fake의 인스턴스 메서드이다.

# 2.

# 3. Localization
>     class Faker:
>    
>         def__init__(self, locale='en_US'):
>             pass

# 4. Seeding the Generator
    import random

    random.random()  # => 임의의 수
    random.random()  #=> 임의의 수

    random.seed(7777)
    random.random()  #=>

    f = Faker()

    # class method
    Faker.seed(1)  

    f1 = Faker()
    f2 = Faker()

    # instance method
    f1.name(), f2.name()

    f = Faker()
    f1.seed_instance(123)
    f1.name()

    f2 = Faker()
    f2.name()