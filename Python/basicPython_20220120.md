# 0120 함수
## 1. Scope (스코프)
1. 함수 밖의 변수(global var), 함수 안의 변수(local var)
   * 인자는 함수 안의 변수 취급한다.
2. 함수 안(local scope)에서는 함수 밖(global scope)에 접근 가능하다.
   * 함수 안에 `a`가 없으면, 함수 밖에서 `a`를 찾는다.
   * 만약, 함수 안에 `a`가 있다면, 함수 밖 `a`는 접근할 수 없다.
3. 함수 밖에서는 함수 안에 접근이 불가능하다.


# 0120 Workshop
## 1. List의 합 구하기
    list_sum([1, 2, 3, 4, 5])  #=> 15

>     def list_sum(numbers):
>        total = 0
>        for num in numbers:
>            total += num
>
>         return total
>
>         list_sum([1, 2, 3, 4, 5])

## 2. Dictionary로 이루어진 List의 합 구하기
    dict_list_sum([{'name': 'kim', 'age: 12}, {'name': 'lee', 'age': 4}])  #=> 16

>     def dict_list_sum(students):
>       total = 0
>       for student in students:
>           total += student['age']
>           return total  
>  
>     students = [{'name': 'kim, 'age': 12}, {'name': 'lee', 'age': 4}]  
>  
>     dict_list_sum(students)

## 3. 2차원 List의 전체 합 구하기
    all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
    #=> 55

>     def all_list_sum(lists):  
>
>         all_total = 0
>         for numbers in lists:
>             numbers_total = 0
>             for n in numbers:
>                 numbers_total += n
>             all_total += numbers_total  
>  
>         return all_total  
>  
>     n_list = [
>       [1],
>       [2, 3],
>       [4, 5, 6],
>       [7, 8, 9, 10],
>     ]  
>  
>     all_list_sum(n_list)


## 1.숫자의 의미
    get_secret_word([83, 115, 65, 102, 89]) #=> 'SsAfY'

## 2. 내 이름은 몇일까?
    get_secret_number('tom') #=> 336

## 3. 강한 이름
    get_strong_word('z', 'a') #=> 'z'
    get_strong_word('tom', 'john') #=> 'john'
