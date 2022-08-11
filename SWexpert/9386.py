import sys

sys.stdin = open("9386.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    inputV = list(map(int, input()))
    maxV = 0
    cnt = 0
    for i in inputV:
        if i == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
        else:

            cnt = 0

    print(f'#{test_case} {maxV}')
