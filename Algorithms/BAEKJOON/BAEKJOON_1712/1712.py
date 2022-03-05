A, B, C = map(int, input().split())

if A != 0 and B > C:
    print(-1)
elif B == C:
    print(-1)
else:
    print(int(A / (C-B)) + 1)