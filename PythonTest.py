T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max = 0  # for 문 안에 최대값 변수 설정
    for i in range(N):  # 중심 원소 찾기
        for j in range(M):

            s = arr[i][j]   # 중심 숫자
            di = [0, 1, 0, -1]  # 우하좌상
            dj = [1, 0, -1, 0]

            for k in range(4):  # 우하좌상 한 번 사이클
                for z in range(1, M):   # 스프레이 길이
                    ni, nj = i + di[k]*z, j + dj[k]*z   # ni, nj = 스프레이 광역 인덱스
                    if 0 <= ni < N and 0 <= nj < N: # 인덱스 초과 방지
                        s += arr[ni][nj]    # 스프레이 중심 합 + 주위 광역 합

                if maxV < s:
                    maxV = s

    print(N, M, arr)




'''
number = int(input())


for i in range(1, number + 1):
    print(i)
'''
'''
number = int(input())

for i in range(number, -1, -1):
    print(i)
'''
'''
number = int(input())
x = 1
sum = 0

while x < number + 1:
    sum = sum + x
    x = x + 1

print(sum)
'''