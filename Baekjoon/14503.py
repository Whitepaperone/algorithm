from pprint import pprint
def solve(r, c, d):
    global res,flag
    arr[r][c] = res
    if flag:
        return
    for i in range(4, 0, -1):
        tmp = (d + (i - 1)) % 4
        di, dj = dir[tmp]
        newR = r + di
        newC = c + dj
        if 0 <= newR < N and 0 <= newC < M and arr[newR][newC] == 0:
            res += 1
            solve(newR, newC, tmp)
            return
    dr, dc = dir[d]
    newR = r - dr
    newC = c - dc
    if 0 <= newR < N and 0 <= newC < M and arr[newR][newC] != 1:
        solve(newR, newC, d)
        return
    elif 0 <= newR < N and 0 <= newC < M and arr[newR][newC] == 1:
        flag=True
    return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
res = 2
flag=False
solve(r, c, d)
print(res-1)
