import sys
sys.stdin = open('input.txt')

N = 9
K = 7
arr = [0]*K
ggoma_list = []

for tc in range(1, N+1):
    ggoma_list.append(int(input()))


def recursive(level, S):
    temp_sum = 0
    # 종료조건
    if level == K:
        if sum(arr) == 100:
            arr.sort()
            for _ in arr:
                print(_)
            # print(arr, type(arr))
        return

    for i in range(S, N-K+level+1):
        arr[level] = ggoma_list[i]
        recursive(level+1, i+1)

recursive(0, 0)


# for _ in :
#     if sum(_) == 100:
#         print(arr)
