def fibo(n):
    f = [[0, 1]] * n
    print(f)

    for i in range(2, n + 1):
        f.append(f[i][i - 1] + f[i][i - 2])

    return f

import sys

sys.stdin = open("2005.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    ARR = [[] for i in range(n)]
    for row in range(n):
        for col in range(row+1):
            if col == 0 or col==row:
                ARR[row].append(1)
            else:
                ARR[row].append(ARR[row - 1][col - 1] + ARR[row - 1][col])
    print(f'#{test_case}')
    for i in ARR:
        print(" ".join(map(str, i)))