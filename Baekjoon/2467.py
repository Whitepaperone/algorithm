import pprint
def bfs(i,j):
    global cnt
    total=1
    q=[]
    q.append((i,j))
    maze[i][j]+=1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 1:
                q.append((ni, nj))
                maze[ni][nj] +=1
                total+=1
    cnt+=1
    return total

N = int(input())
maze = [list(map(int, input())) + [0] for i in range(N)]
visited=[[0]*N for i in range(N)]
cnt=0
total=[]
for i in range(N):
    for j in range(N):
        if maze[i][j]==1:
            total.append(bfs(i,j))

print(cnt)
for i in sorted(total):
    print(i)