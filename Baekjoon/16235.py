from pprint import pprint
def spring(x, y):
    if tree[x][y]:
        tree[x][y].sort()
        index = []
        for i in range(len(tree[x][y])):
            ground[x][y] -= tree[x][y][i]
            tree[x][y][i]+=1
            if ground[x][y] < 0:
                ground[x][y] += tree[x][y][i]
                ground[x][y] += tree[x][y][i] // 2
                index.append(i)
        for i in index:
            tree[x][y].pop(index[0])


def fall(x, y):
    if tree[x][y]:
        for t in tree[x][y]:
            if t % 5 == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        r = x + i
                        c = y + j
                        if 0 <= r < N and 0 <= c < N:
                            if not tree[r][c]:
                                tree[r][c]=[1]
                            else:
                                tree[r][c].append(1)


def winter():
    for x in range(N):
        for y in range(N):
            ground[x][y] += biryo[x][y]


N, M, K = map(int, input().split())
biryo = [list(map(int, input().split())) for i in range(N)]
tree = [[0 for i in range(N)] for i in range(N)]
ground = [[5 for i in range(N)] for i in range(N)]
total=0
for i in range(1,M+1):
    x, y, z = map(int, input().split())
    tree[x-1][y-1] = [z]
for k in range(K):
    for i in range(N):
        for j in range(N):
            spring(i,j)
    for i in range(N):
        for j in range(N):
            fall(i,j)
    pprint(tree)
    winter()
for i in range(N):
    for j in range(N):
        if tree[i][j]:
            total+=len(tree[i][j])

print(total)