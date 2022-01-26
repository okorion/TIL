20220124

# 1. 모음은 몇 개나 있을까?
    count_vowerls('apple')  #=> 2
    count_vowerls('banana')  #=> 3

> def count_vowels(wod):
>     vowels = 'aeiou'
>     cnt = 0
>     for vowel in vowels:
>         for char in word:
>             if vowel == char:
>                 cnt += 1
>        return cnt
>   
> count_vowels('apple'), count_vowels('banana')

# 2. 문자열 조작
    (1) .find(x)는 x 의 첫번째 위치를 반환한다 . 없으면 1 을 반환한다.
    (2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를 기준으로 나누어 list 로 반환한다 . 특정 문자를 지정하지 않으면 공백을 기준으로 나눈다.
    (3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다.
    (4) .strip([chars])은 특정 문자를 지정하면 , 양쪽에서 해당 문자를 찾아 제거한다 . 특정 문자를 지정하지 않으면 오류가 발생한다.

* `.strip([chars])`
* (4) 특정한 문자들을 지정하면, 양쪽을 제거하거나(strip) 왼쪽을 제거하거나(lstrip), 오른쪽을 제거한다(rstrip). chars 파라미터를 지정하지 않으면 공백을 제거한다.

# 3. 정사각형만 만들기
    only_square_area([32, 55, 63], [13, 32, 40, 55])  #=> [1024, 3025]

>    def only_square_area(widths, heights):
>        for width in widths:
>             for height in heights:
>                 if width == height:
>                     results.append
>
>    only_square_area([32, 55, 63], [13, 32, 40, 55])


* * *
20220124

# 1. 평균 점수 구하기
    get_dict_avg({
        'python': 80,
        'algorithm': 90,
        'django': 89,
        'web': 83.
    })  #=> 85.5

>   from functools import reduce
> 
>   #1
>   def sum_total(total, scores):
>       return total + score
>   #2
>   def get_average(scores):
>        return reduce(lambda total, score: total + score, scores, 0) / len(scores)
> 
>   get_average(d.value())


# 2. 혈액형 분류하기
    count_blood([
        'A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B' , 'AB',
    ])  #=> {'A': 3, 'B': 3, 'O': 3, 'AB': 3}


#1
>   def count_blood(bloods):
>       blood_dict = {}
> 
>       for blood in bloods:
>            # 1. 해당 혈액형이 blood_dict에 있다면, 카운트 +1
>           if blood in blood_dict:
>               blood_dict[blood] += 1
>           # 2. 없다면, 카운트 시작
>           else:
>               blood_dict[blood] = 1
>
>       return blood_dict

>       count_blood(['A', 'A', 'B', 'B', 'O', 'AB']) 

#2
>   def count_blood(bloods):
>       blood_dict = {}
> 
>       for blood in bloods:
>           if blood_dict.get[blood]:
>               blood_dict[blood] += 1
>           else:
>               blood_dict.set_default(blood, 1)
> 
>       return blood_dict