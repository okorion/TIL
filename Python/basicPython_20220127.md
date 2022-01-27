# 1. Circle 인스턴스 만들기
    class Circle:
    pi = 3.14

    def __init__(self, r, x, y) :
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)

>     a = Circle(3, 2, 4)
>  
>     print(a.area())
>     print(a.circumference())

# Dog과 Bird는 Animal이다
    class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

>     class Animal:
>         def __init__(self, name):
>         self.name = name
>
>         def walk(self):
>         print(f'{self.name}! 걷는다!')
>
>         def eat(self):
>         print(f'{self.name}! 먹는다!')
>
>
>     class Dog(Animal):
>         def walk(self):
>         print(f'{self.name}! 달린다!')
>
>         def bark(self):
>         print(f'{self.name}! 짖는다!')
>
>
>     class Bird(Animal):
>         def fly(self):
>         print(f'{self.name}! 푸드덕!')

    dog = Dog('멍멍이')
    dog.walk()  # 멍멍이! 달린다!
    dog.bark()  # 멍멍이! 짖는다!

    bird = Bird('구구')
    bird.walk() # 구구! 걷는다!
    bird.eat()  # 구구! 먹는다!
    bird.fly()  # 구구! 푸드덕!

# 3. 오류의 종류
    ZeroDivisionError, NameError, TypeError, IndexError, KeyError, ModuleNotFoundError, ImportError

* `ZeroDivisionError` : 파이썬에서 어떤 수를 0으로 나누게 되면 에러가 발생
* `NameError` : 지역 혹은 전역 이름 공간 내에서 유효하지 않는 이름은 사용할 수 없음. 즉, 어느 곳에서도 정의되지 않은 변수를 호출하였을 경우 에러가 발생
* `TypeError` : 자료형이 올바르지 못한 경우, 함수 호출 과정에서 필수 매개변수가 누락된 경우, 함수 호출 과정에서 매개변수 개수가 초과해서 들어온 경우 에러가 발생
* `IndexError` : 존재하지 않는 index로 조회할 경우 에러가 발생
* `KeyError` : 존재하지 않는 Key로 접근한 경우 에러가 발생
* `ModuleNotFoundError` : 존재하지 않는 Module을 import 하는 경우 에러가 발생
* `ImportError` : Module은 찾았으나 존재하지 않는 클래스/함수를 가져오는 경우 에러가 발생

* * *

# 도형 만들기

    p1 = Point(1, 3)
    p2 = Point(3, 1)
    r1 = Rectangle(p1, p2)
    print(r1.get_area())
    print(r1.get_perimeter())
    print(r1.is_square())
    p3 = Point(3, 7)
    p4 = Point(6, 4)
    r2 = Rectangle(p3, p4)
    print(r2.get_area())
    print(r2.get_perimeter())
    print(r2.is_square())

* 위의 코드를 실행하였을 때, 아래와 같이 출력
    4
    8
    True
    9
    12
    True