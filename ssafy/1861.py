def dfs(y, x):
    if visited[y][x]:
        return visited[y][x]
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if 0 <= y + dy < N and 0 <= x + dx < N and arr[y + dy][x + dx] == arr[y][x] + 1:
            return dfs(y+dy,x+dx) + 1
    return 1


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited=[[0]*N for i in range(N)]
    q=[]
    maxV = 0
    roomN = -1
    for row in range(N):
        for col in range(N):
            value = dfs(row, col)
            visited[row][col]=value
            if value > maxV:
                maxV = value
                roomN = arr[row][col]
            if value == maxV and roomN > arr[row][col]:
                roomN = arr[row][col]
    print(f'#{test_case}', roomN, maxV)
    print(visited)
