20220126

# 1. Built-in 함수와 메서드
    a = [1, 5, 2, 7, 4]
    print(sorted(a))  #=> [1, 2, 4, 5, 7]

    b = [1, 5, 2, 7, 4]
    b.sort()
    print(b)  #=> [1, 2, 4, 5, 7]
* 새로 정렬된 객체를 원하면 sorted 함수 사용.
* 새로 변경된 리스트를 원하면 .sort() 메서드 사용.

# .extend()와 .append()
    a = [1, 2, 3]
    a.append([4, 5])
    print(a)  #=> [1, 2, 3, [4, 5]]

    b = [1, 2, 3]
    b.extend([4, 5])
    print(b)  #=> [1, 2, 3, 4, 5]

* .extemd() 는 iterable 자료형의 요소를 각각 추가.
* .append() 는 객체를 추가.


# 복사가 잘 된 건가?
    a = [1, 2, 3, 4, 5]
    b = a

    a[2] = 5

    print(a)
    print(b)
* 변수 a와 b에 담긴 list의 요소는 같다. (`b = a` 에서 a와 b의 id는 다르지만 같은 주소를 바라보고 있기 때문)

* * *

# 1. 무엇이 중복일까
    duplicated_letters('apple')  #=> ['p']
    duplicated_letters('banana')  #=> ['a', 'n']

> def duplicated_letters(letter):
>     list2 = list(letter)
>     list3 = []
>     list4 = []
>
>     for _ in list2:
>         if list2.count(_) > 1:
>                 list3.append(_)
>
>     for _ in list3:
>         if _ not in list4:
>             list4.append(_)
> 
>     return list4
>   
>    
> print(duplicated_letters('apple'))  #=> ['p']
> print(duplicated_letters('banana'))  #=> ['a', 'n']


# 2. 소대소대
    low_and_up('apple')  #=> aPpLe
    low_and_up('banana')  #=> bAnAnA

> def low_and_up(letter):
>     newlist = str(letter)
>     list2 = ''
>
>     for _ in newlist:
>         if newlist.index(_) % 2 == 1:  # newlist.index(_) -> p의 인덱스 찾기 -> 같은 문자 연속으로 나오면 인덱스가 전 것으로 return -> aPPLe로 출력
>             list2 += _.upper()
>
>         else:
>             list2 += _.lower()    
>
>     return list2
> 
> print(low_and_up('apple'))  #=> aPpLe
> print(low_and_up('banana'))  #=> bAnAnA



# 3. 솔로 천국 만들기
    print(lonely([1, 1, 3, 3, 0, 1, 1]))
    print(lonely([4, 4, 4, 3, 3]))

> def lonely(templist):
>     newlist = []
>     newlist.append(templist[0])
>     for _ in range(1, len(templist)):
>         if templist[_] != templist[_-1]:
>                 newlist.append(templist[_])
>       
>     return newlist
>
> print(lonely([1, 1, 3, 3, 0, 1, 1]))  #=> [1, 3, 0, 1]
> print(lonely([4, 4, 4, 3, 3]))  #=> [4, 3]