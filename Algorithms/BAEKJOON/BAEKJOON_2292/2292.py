import sys
import math
sys.stdin = open('input.txt')

T = int(input())

tmp = math.ceil((T-1) / 6)

cnt = 0
idx = 0

for _ in range(0, tmp+1):
    cnt += _
    idx += 1
    if tmp > cnt:
        pass
    else:
        print(idx)
        break