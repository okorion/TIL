import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    array = []
    for _ in range(N):
        array.append(list(map(str, input().split())))

    new_arr = []  # 중복 리스트 제거
    for _ in array:
        if _ not in new_arr:
            new_arr.append(_)
    nn = []

    for _ in new_arr:  # 0으로 된 문자열 제거
        if _ != [str(0)*M]:
            nn += _

    mm = ''
    for _ in nn:
        mm += _

    a = list(reversed(mm))

    temp = a.index('1')

    b = []

    for _ in range(1, 9):
        b.append(a[temp+(_*7)-1:temp+(_-1)*7-1:-1])

    b.reverse()
    c = []

    for _ in b:
        if _ == list('0001101'):
            c.append(0)
        elif _ == list('0011001'):
            c.append(1)
        elif _ == list('0010011'):
            c.append(2)
        elif _ == list('0111101'):
            c.append(3)
        elif _ == list('0100011'):
            c.append(4)
        elif _ == list('0110001'):
            c.append(5)
        elif _ == list('0101111'):
            c.append(6)
        elif _ == list('0111011'):
            c.append(7)
        elif _ == list('0110111'):
            c.append(8)
        elif _ == list('0001011'):
            c.append(9)

    if ((c[0] + c[2] + c[4] + c[6])*3 + c[1] + c[3]+ c[5] + c[7]) % 10 == 0:
        print(f'#{tc} {c[0] + c[1] + c[2] + c[3] + c[4] + c[5]+ c[6] + c[7]}')
    else:
        print(f'#{tc} 0')
