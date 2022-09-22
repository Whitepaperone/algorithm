def solve(k, r, c, midSum):
    global currentMin
    if r == N - 1 and c == N - 1:
        # path에 있는 합을 구한다
        if midSum<currentMin:
            currentMin=midSum
        return
    if midSum>currentMin:
        return

    path[k] = ARR[r][c]
    if r + 1 < N:
        solve(k + 1, r + 1, c, midSum + ARR[r + 1][c])
    if c + 1 < N:
        solve(k + 1, r, c + 1, midSum + ARR[r][c + 1])


TC = int(input())
for test_case in range(1,TC+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for i in range(N)]
    path = [0] * (N * N)
    currentMin=99999
    solve(0,0,0,ARR[0][0])
    print(f'#{test_case}',currentMin)
