def solve(k, row, col, value):
    global total
    if k == 7:
        result.append(value)
        return
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newR, newC = row + dr, col + dc
        if 0 <= newR < 4 and 0 <= newC < 4:
            solve(k + 1, newR, newC, value+ARR[newR][newC])


TC = int(input())
for test_case in range(1, TC + 1):
    N = 7
    ARR = [list(input().split()) for _ in range(4)]
    cnt = [0] * 10000000
    result = []
    total = 0
    for row in range(4):
        for col in range(4):
            solve(1, row, col, ARR[row][col])

    print(f'#{test_case}',len(set(result)))
