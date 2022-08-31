import pprint
def bfs(i,j):
    cnt=0
    global visited
    q=[]
    q.append((i,j))
    visited[i][j]=True
    while q:
        i,j=q.pop(0)
        arr[i][j]=0
        visited[i][j]=True
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni=di+i
            nj=dj+j
            if 0<=ni<row and 0<=nj<col and arr[ni][nj]==1 and visited[ni][nj]==False:
                if arr[ni][nj]==0:
                    visited[ni][nj]=True
                    q.append((ni,nj))
                elif arr[ni][nj]==1:
                    arr[ni][nj]=0
                    cnt+=1
                    visited[ni][nj]=True
    return cnt

row,col=map(int,input().split())
arr=[list(map(int,input().split()))for i in range(row)]
visited=[[False]*col for i in range(row)]
time=0
while True:
    time+=1
    cnt=bfs(0,0)
    pprint.pprint(arr)