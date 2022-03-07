import math

A, B, V = map(int, input().split())

x = math.ceil((V - A) / (A - B)) + 1

print(x)