import sys

sys.stdin = open("9489.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arrV = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    cnt = 0
    for i in arrV:
        for j in i:
            if j == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
        cnt = 0
    for i in range(M):
        for j in range(N):
            if arrV[j][i] == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
        cnt = 0

    print(f'#{test_case} {maxV}')
