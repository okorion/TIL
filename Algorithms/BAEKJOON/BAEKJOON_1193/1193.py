import sys
sys.stdin = open('input.txt')

X = int(input())

t = 0
K = 0
M = 0

for _ in range(4773):
    t += _
    if X == t:
        if _ % 2 == 0:
            print(str(_) + "/1")
        else:
            print("1/" + str(_))
        break
    else:
        if X < t:  # X = 8, t = 10
            if _ % 2 == 0:
                K = _   # K = 4
                M = t - X
                result = str(K - (t - X)) + "/" + str(t - X + 1)
                print(result)
                break
            else:
                K = _   # K = 4
                M = t - X
                result2 = str(t - X + 1) + "/" + str(K - (t - X))
                print(result2)
                break