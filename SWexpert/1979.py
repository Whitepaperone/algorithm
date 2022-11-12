import sys

sys.stdin = open('1979.txt', 'r')
TC = int(input())
for test_case in range(1, TC + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    col = []
    row = []
    res = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                col.append((i, j))
            else:
                if len(col) == K:
                    res += 1
                col = []

            if arr[j][i] == 1:
                row.append((j, i))
            else:
                if len(row) == K:
                    res += 1
                row = []
        if len(col) == K:
            res += 1
            col = []
        if len(row) == K:
            res += 1
            row = []
        col,row=[],[]

    print(f'#{test_case}', res)
