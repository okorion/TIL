import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    tree = [0] * (N+1)

    for _ in range(M):
        i, j = list(map(int, input().split()))
        tree[i] = j

    for _ in range(N, 1, -1):
        tree[_//2] += tree[_]

    print(f'#{tc} {tree[L]}')

# def in_order(v):
#     global last
#     if v <= last:
#         in_order(v*2)
#         print(v)
#         in_order(v*2+1)


# def create_list(m, n):  # m은 출력할 노드 번호 L, n은 cnt-1
#     new_list = []
#     count2 = 0
#     while count2 <= n:
#         new_list.append(m*2)
#         create_list(m*2, n-1)
#         new_list.append(m*2+1)
#         create_list(m*2+1, n-1)
#         m = m*2
#         count2 += 1
#     return new_list
#
#
# def create_list2(m, n):
#     new_list = []
#     count2 = 0
#     while count2 <= n:
#         new_list.append(m*2)
#         create_list2(m*2, n-1)
#         new_list.append(m*2+1)
#         create_list2(m*2+1, n-1)
#         m = m*2+1
#         count2 += 1
#     return new_list
#
#
# for tc in range(1, T+1):
#     N, M, L = list(map(int, input().split()))
#
#     result_list = []
#
#     for num in range(1, M+1):
#         temp = list(map(int, input().split()))
#         tmp_num = 0
#         tmp_num = temp[0]
#
#         cnt = 0
#         while N >= 2**cnt:
#             cnt += 1
#
#         hahaha_list = list(set(create_list2(L, cnt - 1) + create_list(L, cnt - 1)))
#
#         print(hahaha_list, temp, tmp_num)
#
#         for _ in hahaha_list:
#             if _ == tmp_num:
#                 result_list.append(temp[1])
#
#     print(f'#{tc} {sum(result_list)}')


        # if temp[0] == L*2 and temp[0] == L*2+1:
