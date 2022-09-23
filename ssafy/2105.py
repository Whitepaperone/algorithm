def solve(k, r, c, d):
    global maxV
    if d == 3 and stR == r and stC == c:
        if maxV < k:
            maxV = k
        return
    if 0>r or r >= N or 0>c or c >= N or arr[r][c] in result[:k]:
        # r하고 c가 범위를 벗어나거나 같은 디저트면:
        return
    result[k] = arr[r][c]
    newR, newC = r + direction[d][0], c + direction[d][1]
    solve(k + 1, newR, newC, d)
    d = (d + 1) % 4
    newR, newC = r + direction[d][0], c + direction[d][1]
    solve(k + 1, newR, newC, d)


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    direction = [[1, -1], [1, 1], [-1, 1], [-1, -1]]

    maxV = -1
    for r in range(N):
        for c in range(N):
            stR, stC = r, c
            result = [-1] * (4 * N)
            solve(0, r, c, 0)
    print(f'#{test_case}', maxV)
