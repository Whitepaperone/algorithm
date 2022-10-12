def bfs():
    q = []
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        r, c = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            newR = r + di
            newC = c + dj
            if 0 <= newR < N and 0 <= newC < N and visited[newR][newC] > visited[r][c] + arr[newR][newC]:
                visited[newR][newC] = visited[r][c] + arr[newR][newC]
                q.append((newR, newC))


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input())) for i in range(N)]
    visited = [[1e10] * N for i in range(N)]
    bfs()
    print(visited[N-1][N-1])