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
number = int(input())
x = 1
sum = 0

while x < number + 1:
    sum = sum + x
    x = x + 1

print(sum)