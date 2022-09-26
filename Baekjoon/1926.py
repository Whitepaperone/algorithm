def solve(n, m):
    global total, cnt
    if visited[n][m] == True or arr[n][m] == 0:
        return
    lst = []
    lst.append((n, m))
    while lst:
        ne, me = lst.pop()
        cnt += 1
        visited[ne][me] = True
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            newN = ne + di
            newM = me + dj
            if 0 <= newN < N and 0 <= newM < M:
                if visited[newN][newM] == False and arr[newN][newM]==1:
                    lst.append((newN, newM))
    total += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
visited = [[False] * M for i in range(N)]
total = 0
cnt = 0
maxV = 0
for i in range(N):
    for j in range(M):
        solve(i, j)
        if maxV < cnt:
            maxV = cnt
        cnt = 0
print(total)
print(maxV)
