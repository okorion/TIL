import sys
sys.stdin = open('input3.txt')

N = int(input())

tmp_list = list(map(int, input().split()))
num_list = tmp_list

cnt = 0
plus_cnt = 0
tmp_num = 0  # 순회

for _ in range(0, N):  # 오름차 길이
    if num_list[_] >= tmp_num:
        tmp_num = num_list[_]
        plus_cnt += 1
        if plus_cnt == N:
            cnt = plus_cnt
    elif num_list[_] < tmp_num:
        tmp_num = num_list[_]
        if plus_cnt >= cnt:
            cnt = plus_cnt
        plus_cnt = 1

new_num_list = tmp_list[::-1]
cnt_under = 0
plus_under_cnt = 0
tmp_under_num = 0

for _ in range(0, N):  # 내림차 길이
    if new_num_list[_] >= tmp_under_num:
        tmp_under_num = new_num_list[_]
        plus_under_cnt += 1
        if plus_under_cnt == N:
            cnt_under = plus_under_cnt

    elif new_num_list[_] < tmp_under_num:
        tmp_under_num = new_num_list[_]

        if plus_under_cnt >= cnt_under:
            cnt_under = plus_under_cnt

        plus_under_cnt = 1

# cnt_under = plus_under_cnt
list_set = []

for _ in range(0, 10):
    temp_list = [_]*N
    list_set.append(temp_list)

if tmp_list in list_set:
    print(N)
else:
    print(max(cnt, cnt_under))

    # if num_list == temp_list:
    #     print(N)
    # else:
    #     print(max(cnt, cnt_under))

    # N = int(input())
    #
    # tmp_list = list(map(int, input().split()))
    # num_list = tmp_list
    #
    # plus_cnt = 0
    # tmp_num = 0  # 순회
    # apap = []
    #
    # for _ in range(0, N):  # 오름차 길이
    #     if num_list[_] >= tmp_num:
    #         tmp_num = num_list[_]
    #         plus_cnt += 1
    #
    #     apap.append(plus_cnt)
    #     tmp_num = num_list[_]
    #     plus_cnt = 1
    #
    #
    # new_num_list = tmp_list[::-1]
    #
    # plus_under_cnt = 0
    # tmp_under_num = 0
    #
    # for _ in range(0, N):  # 내림차 길이
    #     if new_num_list[_] >= tmp_under_num:
    #         tmp_under_num = new_num_list[_]
    #         plus_under_cnt += 1
    #
    #     apap.append(plus_under_cnt)
    #     tmp_under_num = new_num_list[_]
    #     plus_under_cnt = 1
    #
    # list_set = []
    #
    # for _ in range(0, 10):
    #     temp_list = [_]*N
    #     list_set.append(temp_list)
    #
    # if tmp_list in list_set:
    #     print(N)
    # else:
    #     print(max(apap))

