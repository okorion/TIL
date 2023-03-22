### 👨‍💻 **ChatGPT Study** 👩‍💻

> 의존성 주입을 사용하는 이유!

 의존성 주입(Dependency Injection)은 객체 지향 프로그래밍에서 사용되는 디자인 패턴 중 하나입니다. 이 패턴은 객체 사이의 의존 관계를 느슨하게 만들어줍니다.

 일반적으로 객체는 다른 객체와 상호작용하며, 이때 의존성이 발생합니다. 예를 들어, A 객체가 B 객체를 사용하는 경우 A는 B에 의존합니다. 이 경우 A 객체를 수정하면 B 객체도 영향을 받을 수 있습니다. 따라서 **<u>객체 간의 의존성이 강하면 코드를 수정하거나 유지보수하는 것이 어렵고, 확장성이 떨어집니다.</u>**

 이를 해결하기 위해 의존성 주입을 사용합니다. 의존성 주입은 객체를 생성하는 시점이나 사용하는 시점에, 해당 객체가 의존하는 다른 객체를 외부에서 주입해주는 것을 말합니다. 이를 통해 객체 간의 의존성을 느슨하게 만들어주고, 코드의 유지보수성과 확장성을 높일 수 있습니다.

 간단히 말해, 의존성 주입은 객체 간의 결합도를 낮춰주어 유연하고 확장성 있는 코드를 작성할 수 있도록 도와줍니다.

<br>

> 간단한 예시 코드를 보여줘!

 🎑 **간단한 예시 코드를 보여드리겠습니다.**

 우선 의존성이 강한 코드를 예시로 살펴보겠습니다.

```python
class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

class Engine:
    def __init__(self):
        pass

    def start(self):
        print("Engine started")
```

 위 코드에서 Car 클래스는 Engine 클래스를 의존하고 있습니다. Car 객체가 생성될 때마다 Engine 객체도 함께 생성되어 의존성이 강해집니다.

 이제 의존성 주입을 적용한 예시 코드를 살펴보겠습니다.

```python
class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

class Engine:
    def __init__(self):
        pass

    def start(self):
        print("Engine started")
```

 위 코드에서 Car 클래스는 ***생성자*** 에서 Engine 객체를 받아서 의존성을 주입받습니다. Car 객체를 생성할 때 필요한 Engine 객체를 외부에서 주입받기 때문에 의존성이 느슨해집니다.

 이렇게 의존성 주입을 적용하면, 코드의 유지보수성과 확장성이 높아지며, 객체 간의 결합도가 낮아져서 코드의 품질이 향상됩니다.
 
<br>
<br>

<details>
    <summary> 🥎 생성자란? </summary>

- - -
> 🎊 생성자(Constructor)는 객체를 생성할 때 자동으로 호출되는 특별한 메서드입니다. 생성자 메서드는 객체의 초기화를 담당하며, 객체가 생성될 때 필요한 작업을 수행합니다.


 파이썬에서 생성자는 __init__ 메서드로 정의됩니다. 생성자는 클래스의 인스턴스를 생성할 때 호출되며, 인스턴스 변수를 초기화하는 등의 작업을 수행할 수 있습니다.

 아래는 생성자를 사용하는 간단한 클래스의 예시 코드입니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 30)
print(person1.name) # 출력결과: "John"
print(person1.age) # 출력결과: 30
```

 위 코드에서 `Person` 클래스는 `__init__` 생성자 메서드를 정의하고 있습니다. 이 생성자 메서드는 `name`과 `age` 두 개의 인자를 받아서 `self.name`과 `self.age` 인스턴스 변수를 초기화합니다.

 이후 `Person` 클래스의 인스턴스를 생성할 때는, 생성자 메서드 `__init__`을 호출하여 초기화 작업을 수행합니다. 이때 생성자 메서드에 전달되는 첫 번째 인자 `self`는 객체 자신을 가리키는 것으로, 일반적으로 모든 메서드의 첫 번째 인자로 사용됩니다.

 생성자를 사용하면 객체를 생성하는 동시에 초기화 작업을 수행할 수 있으므로, 객체의 생성과 초기화를 한 번에 처리할 수 있어서 편리합니다.
- - -
</details>
