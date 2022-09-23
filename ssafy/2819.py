def solve(k, row, col, value):
    global total
    if k == 7:
        if visited[value]:
            return
        visited[value]=1
        total+=1
        return
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

        newR, newC = row + dr, col + dc
        if 0 <= newR < 4 and 0 <= newC < 4:
            # result[k]=ARR[newR][newC]
            solve(k + 1, newR, newC, value*10+ARR[newR][newC])


TC = int(input())
for test_case in range(1, TC + 1):
    N = 7
    ARR = [list(map(int,input().split())) for _ in range(4)]
    visited = [0] * 1000000000
    result = []
    total = 0
    for row in range(4):
        for col in range(4):
            solve(1, row, col, ARR[row][col])

    print(f'#{test_case}',total)
