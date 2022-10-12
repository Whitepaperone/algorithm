from pprint import pprint
from collections import deque


def solve(fuel):
    global minV
    q = deque()
    q.append((0, 0))
    visited[0][0]=0
    while q:
        cY, cX = q.popleft()

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nY = cY + di
            nX = cX + dj
            if 0 <= nY < N and 0 <= nX < N :
                gap=max(arr[nY][nX]-arr[cY][cX],0)+1
                if visited[nY][nX] > visited[cY][cX]+gap:
                    visited[nY][nX] = visited[cY][cX] + gap
                    q.append((nY, nX))


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [[99999] * N for i in range(N)]
    minV = 99999
    solve(0)
    print(f'#{test_case} {visited[N-1][N-1]}')
    print(visited)
