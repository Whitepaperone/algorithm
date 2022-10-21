from pprint import pprint
import copy
def solve():
    global lst
    cnt = 0
    q = []
    visited = [[False] * M for i in range(N)]
    check=copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j]=True
    while q:
        row, column = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            newR = row + di
            newC = column + dj
            if 0 <= newR < N and 0 <= newC < M and arr[newR][newC] != 1 and not visited[newR][newC]:
                q.append((newR, newC))
                visited[newR][newC] = True
                check[newR][newC]=2
    for i in range(N):
        for j in range(M):
            if check[i][j] == 0:
                cnt += 1
    lst.append(cnt)
    pass


def wall(cnt):
    if cnt == 3:
        solve()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0
    pass


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
cnt = 0
lst = []
wall(0)
print(max(lst))
