>     N = 5
>     K = 2
>     arr = [0]*K
>     A = [1, 2, 3, 4, 5]
>     def combi(level, S):
>       # 종료조건
>       if level == K:
>         print(arr)
>         return
>     
>       for i in range(S, N-K+level+1):
>         arr[level] = A[i]
>         combi(level+1, i+1)
>     
>     combi(0,0)
