def solve():
    global minV
    total=0
    for i in range(len(home)):
        distance=[]
        for j in range(M):
            hx,hy=home[i]
            px,py=lst[j]
            dis=abs(hx-px)+abs(hy-py)
            distance.append(dis)
        total+=min(distance)
        if total>minV:
            return
    if total<minV:
        minV=total



def per(k):
    global tmp
    if k == M:
        lst.sort()
        if lst in tmp:
            return
        else:
            tmp.append(lst[:])
            solve()
        return
    for i in range(Q):
        if not res[i]:
            res[i]=1
            lst[k]=q[i]
            per(k+1)
            res[i]=0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
q=[]
home=[]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            q.append((i, j))
        elif arr[i][j]==1:
            home.append((i,j))
Q=len(q)
res=[0]*Q
lst=[0]*M
tmp=[]
minV=1e10
per(0)
print(minV)