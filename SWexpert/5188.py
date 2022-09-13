import sys, pprint

sys.stdin = open('5188.txt', 'r')


def bfs(i, j): #왜 됨?
    q = []
    q.append((i, j))
    while q:
        i, j = q.pop(0)
        if i == N - 1 and j == N - 1:
            return visited[i][j]
        for di, dj in [[0, 1], [1, 0]]:
            if i + di < N and j + dj < N :
                if visited[i+di][j+dj]>visited[i][j] + arrLst[i + di][j + dj]:
                    visited[i + di][j + dj] = visited[i][j] + arrLst[i + di][j + dj]
                    q.append((i + di, j + dj))

# def dfsr(i,j):
#     for di, dj in [[0, 1], [1, 0]]:
#         if i + di < N and j + dj < N and visited[i+di][j+dj]==0:
#             if visited[i + di][j + dj] > visited[i][j] + arrLst[i + di][j + dj]:
#                 visited[i + di][j + dj] = visited[i][j] + arrLst[i + di][j + dj]
#             dfsr(i+di,j+dj)

# def dfsr(v):
#   visited[v] = True
#
#   print(v, end=' ')
#   for w in G[v]:
#     if not visited[w]:
#         dfsr(w)

def findF(i, j):
    if i == N - 1 and j == N - 1:
        return visited[i][j]
    if i + 1 < N and j + 1 < N:
        temp1 = arrLst[i + 1][j]
        temp2 = arrLst[i][j + 1]
        if temp1 > temp2:
            visited[i][j + 1] = visited[i][j] + arrLst[i][j + 1]
            j += 1
            findF(i, j)
        elif temp1 < temp2:
            visited[i + 1][j] = visited[i][j] + arrLst[i + 1][j]
            i += 1
            findF(i, j)
        else:
            visited[i][j + 1] = visited[i][j] + arrLst[i][j + 1]
            j += 1
            findF(i, j)
            visited[i + 1][j] = visited[i][j] + arrLst[i + 1][j]
            i += 1
            findF(i, j)


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    arrLst = [list(map(int, input().split())) for i in range(N)]
    visited = [[99999] * N for i in range(N)]

    visited[0][0]=arrLst[0][0]
    bfs(0,0)
    print(f'#{test_case}', visited[N-1][N-1])
    pprint.pprint(visited)