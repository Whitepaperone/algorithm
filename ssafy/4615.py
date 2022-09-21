def find(x, y, stone):
    y -= 1
    x -= 1
    arr[y][x] = stone
    if stone == 1:
        op = 2
    if stone == 2:
        op = 1
    for dy, dx in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        nowY = y + dy
        nowX = x + dx
        while 0 <= nowY < N and 0 <= nowX < N and arr[nowY][nowX] == op:
            nowY += dy
            nowX += dx
        if 0 <= nowY < N and 0 <= nowX < N and arr[nowY][nowX]==stone:
            while y!=nowY or x!=nowX:
                arr[nowY][nowX]=stone
                nowY -= dy
                nowX -= dx
    print(arr)


TC = int(input())
for test_case in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = [[0 for i in range(N)] for i in range(N)]
    totalB = 0
    totalW = 0
    y, x = N // 2, N // 2
    arr[y][x], arr[y - 1][x - 1] = 2, 2
    arr[y - 1][x], arr[y][x - 1] = 1, 1
    for i in range(M):
        x, y, stone = map(int, input().split())
        find(x, y, stone)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                totalB += 1
            elif arr[i][j] == 2:
                totalW += 1
    print(f'#{test_case}', totalB, totalW)
