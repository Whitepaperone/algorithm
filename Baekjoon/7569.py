from collections import deque
def bfs():
    global day
    while q:
        curZ, curY, curX, day = q.popleft()
        for di, dj, dk in [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]:
            nZ = curZ + di
            nY = curY + dj
            nX = curX + dk
            if 0 <= nZ < H and 0 <= nY < M and 0 <= nX < N and arr[nZ][nY][nX] == 0 :
                q.append((nZ, nY, nX, day + 1))

                arr[nZ][nY][nX] = 1
    return day


N, M, H = map(int, input().split())
arr = []
visited = []
q = deque()
day = 0
for i in range(H):
    arr.append([list(map(int, input().split())) for i in range(M)])
for i in range(H):
    for j in range(M):
        for k in range(N):
            if arr[i][j][k] == 1:
                q.append((i, j, k, day))
bfs()
for i in range(H):
    for j in range(M):
        for k in range(N):
            if arr[i][j][k] == 0:
                day = -1
print(day)
