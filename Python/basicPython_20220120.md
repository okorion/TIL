# 0120 Workshop
## 1. List의 합 구하기
    list_sum([1, 2, 3, 4, 5])  #=> 15

> def list_sum(numbers):
>    total = 0
>    for num in numbers:
>        total += num
>
>     return total
>
>     list_sum([1, 2, 3, 4, 5])

## 2. Dictionary로 이루어진 List의 합 구하기
    dict_list_sum([{'name': 'kim', 'age: 12}, {'name': 'lee', 'age': 4}])  #=> 16

> def dict_list_sum(students):
>   total = 0
>   for student in students:
>       total += student['age']
>       return total  
>  
> students = [{'name': 'kim, 'age': 12}, {'name': 'lee', 'age': 4}]  
>  
> dict_list_sum(students)

## 3. 2차원 List의 전체 합 구하기
    all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
    #=> 55

> def all_list_sum(lists):  
>
>     all_total = 0
>     for numbers in lists:
>         numbers_total = 0
>         for n in numbers:
>             numbers_total += n
>         all_total += numbers_total  
>  
>     return all_total  
>  
> n_list = [
>   [1],
>   [2, 3],
>   [4, 5, 6],
>   [7, 8, 9, 10],
> ]  
>  
> all_list_sum(n_list)