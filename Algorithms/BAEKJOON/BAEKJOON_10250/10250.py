T = int(input())

for tc in range(1, T+1):
    H, W, N = list(map(int, input().split()))  # 1 10 9 => 109
    num = N % H
    num2 = N // H

    if num == 0 and num2 < 10:
        num = str(H)
        num2 = "0" + str(num2)
    elif num == 0 and num2 >= 10:
        num = str(H)
        num2 = str(num2)

    elif num2 < 10:
        if num2 == 9:
            num = str(num)
            num2 = str(num2 + 1)
        else:
            num = str(num)
            num2 = "0" + str(num2 + 1)
    else:
        num = str(num)
        num2 = str(num2+1)

    new_str = num + num2

    print(new_str)