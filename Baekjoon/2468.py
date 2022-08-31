import pprint


def bfs(i, j, h):
    global cnt
    q = []
    q.append((i, j))
    visited[i][j] = True
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > h and visited[ni][nj] == False:
                q.append((ni, nj))
                visited[ni][nj] = True

    cnt += 1
    return


cnt = 0
maxV = 0
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
maxH=0
for i in arr:
    for j in i:
        if maxH<j:
            maxH=j
H = [i for i in range(100)]
for h in H:
    if h>maxH:
        break
    cnt = 0
    visited = [[False] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
    if maxV < cnt:
        maxV = cnt
print(maxV)
