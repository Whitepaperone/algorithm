import pprint
def solve(x, y):
    global total
    if visited[x][y] == True or ground[x][y] == 0:
        return
    lst = []
    lst.append((x, y))
    while lst:
        dx, dy = lst.pop()
        visited[dx][dy] = True
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            newX = dx + di
            newY = dy + dj
            if 0 <= newX < N and 0 <= newY < M and visited[newX][newY] == False and ground[newX][newY]:
                lst.append((newX, newY))
    total += 1


TC = int(input())
for test_case in range(1, TC + 1):
    N, M, K = map(int, input().split())
    ground = [[0] * M for i in range(N)]
    visited = [[False] * M for i in range(N)]
    arr = []
    total = 0
    for i in range(K):
        arr.append(list(map(int, input().split())))
    for dx, dy in arr:
        ground[dx][dy] = 1

    pprint.pprint(ground)
    for n in range(N):
        for m in range(M):
            solve(n, m)

    print(total)
