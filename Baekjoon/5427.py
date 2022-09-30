from collections import deque


def bfs():
    global time
    while q:
        curY, curX, time = q.pop(0)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nY = curY + di
            nX = curX + dj
            if 0 <= nY < M and 0 <= nX < N and arr[nY][nX] != -1 and arr[nY][nX] == 0:
                q.append((nY, nX, time + 1))
                arr[nY][nX] = time + 1
    return


def bfs2(y, x, time):
    q.append((y, x, time))
    while q:
        curY, curX, time = q.pop(0)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nY = curY + di
            nX = curX + dj
            if 0 <= nY < M and 0 <= nX < N and arr[nY][nX] != -1 and arr[nY][nX] > time:
                q.append((nY, nX, time + 1))
                arr[nY][nX]=time+1
            if 0>nY or nY >= M or 0>nX or nX >= N:
                return time
    return 'IMPOSSIBLE'


TC = int(input())
for test_case in range(1, TC + 1):

    N, M = map(int, input().split())
    arr = [list(input()) for i in range(M)]
    q = []
    time = 1
    for i in range(M):
        for j in range(N):
            if arr[i][j] == '*':
                arr[i][j] = 1
                q.append((i, j, time))
            if arr[i][j] == '#':
                arr[i][j] = -1
            if arr[i][j] == '@':
                arr[i][j] = 1
                a = i
                b = j
            if arr[i][j] == '.':
                arr[i][j] = 0
    print(arr)
    bfs()
    time = bfs2(a, b, 0)


    if time != 'IMPOSSIBLE':
        print(time+1)
    else:
        print(time)
