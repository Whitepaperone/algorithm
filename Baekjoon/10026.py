

def solve(x, y):
    global tmp
    if visited[x][y] == True:
        return
    lst = []
    lst.append((x, y))
    while lst:
        dx, dy = lst.pop()
        visited[dx][dy] = True
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            newX = dx + di
            newY = dy + dj
            if 0 <= newX < N and 0 <= newY < N and visited[newX][newY] == False and arr[newX][newY]==arr[x][y]:
                lst.append((newX, newY))



    tmp += 1
    print(tmp,x,y,visited)
    print(arr)

N = int(input())
arr = [input() for i in range(N)]
visited = [[False] * N for i in range(N)]
tmp = 0
total = 0
total2 = 0
for i in range(N):
    for j in range(N):
        solve(i, j)
        if arr[i][j] == 'G':
            arr[i] = arr[i].replace('G', 'R', 1)
total = tmp
tmp = 0
visited = [[False] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        solve(i, j)
total2 = tmp
print(total, total2)
