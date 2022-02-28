import sys
sys.stdin = open('input.txt')

N = int(input())

direction_list = []
length_list = []

for tc in range(1, 7):
    direction, length = list(map(int, input().split()))
    direction_list.append(direction)
    length_list.append(length)

ab_list = []
minus_list = []
max_index = []

for _ in range(1, 7):
    if direction_list.count(_) == 1:
        ab_list.append(length_list[direction_list.index(_)])
        max_index.append(direction_list.index(_))

    elif direction_list.count(_) == 2:
        minus_list.append(length_list[direction_list.index(_)])
        # del length_list[direction_list.index(_)]

a, b = max(max_index)+2, min(max_index)-2

# print(ab_list, minus_list, max_index, a, b)

if max_index == [0, 5]:
    a, b = 2, 3

elif max_index == [5, 0]:
    a, b = 2, 3

elif max(max_index)+2 >= 6:
    a = max(max_index)-4

minus_area = length_list[a] * length_list[b]
total_area = 1

for _ in ab_list:
    total_area *= _

result = (total_area - minus_area) * N

print(result)
