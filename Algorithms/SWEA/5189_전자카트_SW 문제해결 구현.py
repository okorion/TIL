# DFS (완전탐색)

T = int(input())


def dfs(cnt, start, total):
    global result

    if cnt == N - 1:
        result = min(result, matrix[start][0] + total)

    for i in range(1, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(cnt + 1, i, total + matrix[start][i])
            visited[i] = 0


for _ in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 10e10
    dfs(0, 0, 0)

    print(f'#{_+1} {result}')
    
