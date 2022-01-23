2022012x.md
* * *
20220122
# 컨테이너 (Container)
* 여러 개의 값을 저장할 수 있는 것(객체)를 의미하며, 서로 다른 자료형을 저장 할 수 있다.  
    
## 시퀀스(Sequence)형 컨테이너
 시퀀스는 데이터가 순서대로 나열된(ordered) 형식  # 정렬되었다(sorted)라는 뜻은 아님.
* 순서가 있음.
* 특정 위치의 데이터를 가리킬 수 있음.
* 리스트(list), 튜플(tuple), 레인지(range), 문자형(string), 바이너리(binary)

### 리스트 (List)
* 리스트는 대괄호 `[]` 및 `list()`를 통해 만들 수 있음.
* 순서가 있는 시퀀스로 인덱스를 통해 접근 가능  # `list[i]`

### 튜플 (Tuple)
* 튜플은 리스트와 유사하지만, `()`로 묶어서 표현
* 튜플은 수정 불가능(immutable) 

### 레인지(range())
* `range()`는 정수의 시퀀스를 나타내기 위해 사용
* 범위 및 스텝 지정 : range(n, m, s)  # n부터 m-1까지 s만큼 증가


## 비 시퀀스형(Non-sequence) 컨테이너
### 세트 (Set)
* 세트는 순서가 없고 중복된 값이 없는 자료 구조  # 수학에서의 집합과 동일하게 처리
* 세트는 `{}`를 통해 만듬.  # 빈 세트를 만들려면 `set()`
* 담고 있는 객체를 삽입 변경, 삭제 가능(mutable)
* 활용 가능한 연산자는 차집합(-), 합집합(|), 교집합(&)

### 딕셔너리 (Dictionary)
* 딕셔너리는 key와 value가 쌍으로 이루어져 있음.
* 딕셔너리는 `{}`를 통해 만듬.  # `dict()` 가능
* 순서를 보장하지 않음.
* key는 변경 불가능(immutable)한 데이터만 가능  # (immutable : string, integer, float, boolean, tuple, range)
* value는 list, dictionary를 포함한 모든 것이 가능

* * *
20220123
# 반복문 (Loop Statement)
## While 반복문
* While 문 조건식이 참일 때는 계속 반복됨.  # 반복문에 의해 변하는 수는 조건식의 앞에 위치.

## For 반복문
### 문자열(String) 순회  # `range()`와 순회할 string의 길이를 활용
    chars = input('문자 입력 : ')
    length = len(chars)

    for _ in range(0, length, 1):  # 역문자열 -> range(length-1, -1, -1)
    print(chars[_])

### 딕셔너리 순회
    value = []

    for _ in grades:
    value.append(grades[_])
    
    print(value, type(value))  # value값 출력하기.


    key = []

    for _ in grades:
    key.append(_)
    
    print(key)  # key값 출력하기.  # return 은 어떻게??

### for 문과 if 문 실습
> 반복문과 조건문만 활용하여 1~30까지 숫자 중 홀수만 출력
    num = range(1, 31, 1)

    for _ in num:
        if _ % 2 == 1:
            print(_)
        else:
            pass

* 출력 예시
    1
    3
    5
    '''
    27
    29

