from collections import deque
def bfs():
    global time
    while q:
        curY, curX, time = q.pop(0)
        if time == 0:
            visited[curY][curX] = '*'
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nY = curY + di
            nX = curX + dj
            if 0 <= nY < M + 2 and 0 <= nX < N + 2 and visited[nY][nX] != -1 and visited[nY][nX] == 0:
                q.append((nY, nX, time + 1))
                visited[nY][nX] = time + 1
    return time


def bfs2(y, x, time):
    q.append((y, x, time))
    while q:
        curY, curX, time = q.pop(0)
        if time == 0:
            visited[curY][curX] = '@'
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nY = curY + di
            nX = curX + dj
            if 0 <= nY < M + 2 and 0 <= nX < N + 2 and visited[nY][nX] != -1:
                if type(visited[nY][nX]) == int:
                    if visited[nY][nX] > time:
                        q.append((nY, nX, time + 1))
                        visited[nY][nX] = 10 * (time + 1)
    return time


TC = int(input())
for test_case in range(1, TC + 1):

    N, M = map(int, input().split())
    arr = [input() for i in range(M)]
    visited = [[0] * (N + 2) for i in range(M + 2)]
    q = []
    time = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == '*':
                q.append((i + 1, j + 1, time))
            if arr[i][j] == '#':
                visited[i + 1][j + 1] = -1
            if arr[i][j] == '@':
                a = i + 1
                b = j + 1
    bfs()
    bfs2(a, b, 0)
    minV = 999999
    time = 0
    for i in range(M + 2):
        if i == 0 or i == M + 1:
            for j in range(N + 2):
                if visited[i][j]%10:
                    time = visited[i][j]//10
                    if time < minV:
                        minV = time
        else:
            for j in [0, N + 1]:
                if visited[i][j]%10:
                    time = visited[i][j]//10
                    if time < minV:
                        minV = time
    if time == 0:
        minV = 'IMPOSSIBLE'
    print(minV)