import sys
sys.stdin = open('Algorithms\BAEKJOON\BAEKJOON_1244\input.txt')

switch_total = input()
switch_list = list(map(int, input().split()))

T = int(input())


def man(temp_switch_num):
    idx_balance = len(switch_list)//temp_switch_num

    for temp_num in range(idx_balance+1):
        if switch_list[temp_switch_num*temp_num-1] == 0:
            switch_list[temp_switch_num*temp_num-1] += 1
        else:
            switch_list[temp_switch_num*temp_num-1] -= 1

    del switch_list[len(switch_list)-1]  # 마지막 인덱스(input 에서는 인덱스 8) 삭제

    return switch_list


def woman(temp_switch_num):  # t_s_n = 3, 0 1 1 1 0 1 0 1 => 0 1 0 1 0 1 0 1 =>            1 0 0 0 1 1 0 1

    if switch_list[temp_switch_num - 1] == 0:
        switch_list[temp_switch_num - 1] += 1
    else:
        switch_list[temp_switch_num - 1] -= 1

    cnt = 0

    while temp_switch_num + cnt < len(switch_list)-1 and temp_switch_num - cnt > 1:  # < 8 ,
        if switch_list[temp_switch_num-2-cnt] != switch_list[temp_switch_num+cnt]:
            break
        else:
            if switch_list[temp_switch_num-2-cnt] == 0:
                switch_list[temp_switch_num-2-cnt] += 1
                switch_list[temp_switch_num+cnt] += 1
                cnt += 1
            else:
                switch_list[temp_switch_num-2-cnt] -= 1
                switch_list[temp_switch_num+cnt] -= 1
                cnt += 1

    del switch_list[len(switch_list)-1]  # 마지막 인덱스(input 에서는 인덱스 8) 삭제

    return switch_list


for student in range(1, T+1):
    giriboy, switch_num = map(int, input().split())

    if giriboy == 1:  # 남학생일 경우 0 1 0 1 0 0 0 1 => 0 1 1 1 0 1 0 1
        switch_list += [2]
        man(switch_num)
    elif giriboy == 2:  # 여학생일 경우
        switch_list += [2]
        woman(switch_num)

if len(switch_list) <= 20:
    print(*switch_list)
elif len(switch_list) <= 40:
    print(*switch_list[:20])
    print(*switch_list[20:])
elif len(switch_list) <= 60:
    print(*switch_list[:20])
    print(*switch_list[20:40])
    print(*switch_list[40:])
elif len(switch_list) <= 80:
    print(*switch_list[:20])
    print(*switch_list[20:40])
    print(*switch_list[40:60])
    print(*switch_list[60:])
else:
    print(*switch_list[:20])
    print(*switch_list[20:40])
    print(*switch_list[40:60])
    print(*switch_list[60:80])
    print(*switch_list[80:])
