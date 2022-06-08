T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    temp = 1

    if n == 1:
        print(1)

    else:
        for _ in range(1, k+2):
            temp *= ((_-1)+n)/_
        print(round(temp))