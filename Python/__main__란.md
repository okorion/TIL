## 45.2 모듈과 시작점 알아보기

<iframe width="100%" height="480" src="https://www.youtube.com/embed/jpmL9YcXjhg?list=PLa9dKeCAyr7iWPMclcDxbnlTjQ2vjdIDD&amp;vq=hd720" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>

인터넷에 있는 파이썬 코드를 보다 보면 if \__name\__ == '\__main\__':으로 시작하는 부분을 자주 만나게 됩니다.

```
if __name__ == '__main__':
    코드
```

도대체 이 코드는 왜 사용하는 것일까요? 이 코드는 현재 스크립트 파일이 실행되는 상태를 파악하기 위해 사용합니다.

먼저 __name__부터 알아보겠습니다. 다음 내용을 프로젝트 폴더(C:\project) 안에 hello.py 파일로 저장하세요.

hello.py

```
print('hello 모듈 시작')
print('hello.py __name__:', __name__)    # __name__ 변수 출력
print('hello 모듈 끝')
```

그리고 다음 내용을 프로젝트 폴더(C:\project) 안에 main.py 파일로 저장한 뒤 실행해보세요.

main.py

```
import hello    # hello 모듈을 가져옴
 
print('main.py __name__:', __name__)    # __name__ 변수 출력
```

실행 결과

```
hello 모듈 시작
hello.py __name__: hello
hello 모듈 끝
main.py __name__: __main__
```

실행을 해보면 hello.py 파일과 main.py 파일의 \__name\__ 변수 값이 출력됩니다.

파이썬에서 import로 모듈을 가져오면 해당 스크립트 파일이 한 번 실행됩니다. 따라서 hello 모듈을 가져오면 hello.py 안의 코드가 실행됩니다. 따라서 hello.py의 \__name\__ 변수에는 'hello'가 들어가고, main.py의 \__name\__ 변수에는 '\__main\__'이 들어갑니다.

▼ **그림 45-2** hello.py를 모듈로 가져왔을 때![img](https://dojang.io/pluginfile.php/14074/mod_page/content/4/045002.png)

즉, \__name\__은 모듈의 이름이 저장되는 변수이며 import로 모듈을 가져왔을 때 모듈의 이름이 들어갑니다. 하지만 파이썬 인터프리터로 스크립트 파일을 직접 실행했을 때는 모듈의 이름이 아니라 '\__main\__'이 들어갑니다(참고로 \__name\__과 \__main\__을 헷갈리지 마세요. 같은 네 글자에 알파벳 모양이 비슷해서 헷갈리기 쉽습니다).

좀 더 정확하게 알아보기 위해 콘솔(터미널, 명령 프롬프트)에서 **python**으로 main.py 파일을 실행해봅니다(리눅스, macOS에서는 **python3** 사용).



```
C:\project>python main.py
hello 모듈 시작
hello.py __name__: hello
hello 모듈 끝
main.py __name__: __main__
```

**python main.py**와 같이 파이썬으로 스크립트 파일을 직접 실행했습니다. 여기서도 hello.py 파일의 \__name\__ 변수에는 'hello' 그리고 main.py 파일의 \__name\__ 변수에는 '\__main\__'이 들어갑니다.

▼ **그림 45-3** hello.py를 모듈로 가져왔을 때![img](https://dojang.io/pluginfile.php/14074/mod_page/content/4/045003.png)

하지만 다음과 같이 **python**으로 hello.py 파일을 실행해보면 결과가 조금 달라집니다.

```
C:\project>python hello.py
hello 모듈 시작
hello.py __name__: __main__
hello 모듈 끝
```



hello.py 파일의 \__name\__ 변수에는 'hello'가 아니라 '\__main\__'이 들어갑니다. 즉, 어떤 스크립트 파일이든 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 \__name\__에는 '\__main\__'이 들어갑니다. 이는 프로그램의 시작점(entry point)이라는 뜻입니다.

▼ **그림 45-4** hello.py를 단독으로 실행했을 때![img](https://dojang.io/pluginfile.php/14074/mod_page/content/4/045004.png)

파이썬은 최초로 시작하는 스크립트 파일과 모듈의 차이가 없습니다. 어떤 스크립트 파일이든 시작점도 될 수 있고, 모듈도 될 수 있습니다. 그래서 \__name\__ 변수를 통해 현재 스크립트 파일이 시작점인지 모듈인지 판단합니다.

if \__name\__ == '\__main\__':처럼 \__name\__ 변수의 값이 '\__main\__'인지 확인하는 코드는 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업입니다. 즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도입니다.

### 45.2.1 스크립트 파일로 실행하거나 모듈로 사용하는 코드 만들기

그럼 스크립트 파일을 그대로 실행할 수도 있고, 모듈로도 사용할 수 있는 코드를 만들어보겠습니다. 다음 내용을 프로젝트 폴더(C:\project) 안에 calc.py 파일로 저장한 뒤 실행해보세요.

calc.py

```
def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b
 
if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    print(add(10, 20))
    print(mul(10, 20))
```

실행 결과

```
30
200
C:\project>python calc.py
30
200
```

IDLE에서 실행하거나 **python calc.py**와 같이 파이썬 인터프리터로 실행하면 10, 20의 합과 곱이 출력됩니다. 즉, 프로그램의 시작점일 때는 if \__name\__ == '\__main\__': 아래의 코드가 실행됩니다.

그럼 calc.py를 모듈로 사용하면 어떻게 될까요? 다음과 같이 import로 calc를 가져와봅니다.

```
>>> import calc
>>> 
```

모듈로 가져왔을 때는 아무것도 출력되지 않습니다. 왜냐하면 \__name\__ 변수의 값이 '\__main\__'일 때만 10, 20의 합과 곱을 출력하도록 만들었기 때문입니다. 즉, 스크립트 파일을 모듈로 사용할 때는 calc.add, calc.mul처럼 함수만 사용하는 것이 목적이므로 10, 20의 합과 곱을 출력하는 코드는 필요가 없습니다.

이때는 다음과 같이 calc.add와 calc.mul 함수에 원하는 값을 넣어서 사용하면 됩니다.

```
>>> calc.add(50, 60)
110
>>> calc.mul(50, 60)
3000
```

**참고 |** **파이썬은 왜 프로그램의 시작점이 정해져 있지 않나요?**

파이썬이 처음에 개발 될 당시에는 리눅스/유닉스에서 사용하는 스크립트 언어 기반이었기 때문에 프로그램의 시작점이 따로 정해져 있지 않았습니다. 보통 리눅스/유닉스의 스크립트 파일은 파일 한 개로 이루어진 경우가 많은데, 이 스크립트 파일 자체가 하나의 프로그램이다 보니 시작점이 따로 필요하지 않습니다. 하지만 C 언어나 자바같은 언어는 처음 만들어질 때부터 소스 파일을 여러 개 사용했기 때문에 여러 소스 파일의 함수들 중에서도 시작 함수(main)를 따로 정해 놓았습니다.



<br>

<br>

참고링크: https://dojang.io/mod/page/view.php?id=2448