# 0118 Workshop
## 1. 세로로 출력하기 
    [입력]
    10

    [출력]
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

>     number = int(input())
>
>     for i in range(1, number+1):  
>         print(i)

## 2. 거꾸로 세로로 출력하기
    [입력]
    5

    [출력]
    5
    4
    3
    2
    1
    0
    
>     number = int(input())
>
>     for i in range(number, -1, -1):
>         print(i)

>     n = 1
>         while n < number+1:
>         print(n)
>         n += 1

## 3. N줄 덧셈 (number까지의 sum)
    [입력]
    10

    [출력]
    55

>     number = int(input())  
>     x = 1  
>     sum = 0  
>   
>     while x < number + 1:  
>         sum = sum + x  
>         x = x + 1  
>   
>     print(sum)

>     sum(range(1,number+1))

>     for n in range(1, number+1):
>         total -= n
> 
>     total

>     number = 10
>
>     total = (number+1) * number / 2
>     int(total)