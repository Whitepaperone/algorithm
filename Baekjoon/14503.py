from pprint import pprint
def solve(r, c, d):
    global res
    res += 1
    arr[r][c] = 1
    pprint(arr)
    for i in range(4, 0, -1):
        tmp = (d + i ) % 4
        print(d,tmp)
        di, dj = dir[tmp]
        newR = r + di
        newC = c + dj
        if 0 <= newR < M and 0 <= newC < N and arr[newR][newC] != 1:
            solve(newR, newC, tmp)
            return
    dr, dc = dir[(tmp + 1) % 4]
    newR = r - dr
    newC = r - dc
    if 0 <= newR < M and 0 <= newC < N and arr[newR][newC] != 1:
        solve(newR, newC, tmp)
        return
    return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
res = 0
solve(r, c, d)
print(res)