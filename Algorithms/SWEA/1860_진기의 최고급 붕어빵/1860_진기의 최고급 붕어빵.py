import sys
sys.stdin = open("input2.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    customer_time = list(map(int, input().split()))
    customer_time.sort()

    max0 = K
    tmp = 0
    tst = 2  # int(customer_time[0]/M + 1) 로 입력해서 테스트 케이스 997/1000 => 오래 걸림. // K가 1인 케이스 중 오류

    error = 0

    for _ in customer_time:
        _ = int(_/M)
        tmp += 1
        if _ >= tst:
            tst += 1
            max0 += K

        elif max0 - tmp < 0:
            error += 1

        elif int(customer_time[0]/M) == 0:
            error += 1

        elif max(customer_time) > 11111:
            error += 1

    if error == 0:
        print(f'#{tc} Possible')

    else:
        print(f'#{tc} Impossible')



    # if star == N/K:
    #     print

    # for _ in customer_time:
    #     _ = int(_/M)
    #
    #     if _ == star:
    #         tmp += 1
    #         if tmp > max0:
    #             print("Impossible")
    #             break
    #     elif _ == 0:
    #         print("Impossible")
    #         break
    #     else:
    #         max0 += K
    #         tmp += 1
    #
    # if tmp == len(customer_time):
    #     print("Possible")
