
def bfs():
    global time
    while q:
        curY, curX, time = q.pop(0)
        print(curX,curY)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nY = curY + di
            nX = curX + dj
            if 0 <= nY < M and 0 <= nX < N and visited[nY][nX] !=-1:
                q.append((nY, nX, time + 1))
                visited[nY][nX] = time+1
    return time
def bfs2():
    global time
    while q:
        curY, curX, time = q.pop(0)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nY = curY + di
            nX = curX + dj
            if 0 <= nY < M and 0 <= nX < N and visited[nY][nX] !=-1 and visited[nY][nX]>time:
                q.append((nY, nX, time + 1))
                visited[nY][nX] = '@'*(time+1)
    return time
TC=int(input())
for test_case in range(1,TC+1):

    N, M = map(int, input().split())
    arr = [input() for i in range(M)]
    visited=[[0]*(N+2) for i in range(M+2)]
    q = []
    time = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == '*':
                q.append((i, j, time))
            if arr[i][j]=='#':
                visited[i][j]=-1
    bfs()
    bfs2()
    for i in range(M+2):
        if i==0 or i==M+1:
            for j in range(N+2):
                if '@' in visited[i][j]:
                    time=visited[i][j].count('@')
        else:
            for j in [0,N+1]:
                if '@' in visited[i][j]:
                    time=visited[i][j].count('@')

    print(time)