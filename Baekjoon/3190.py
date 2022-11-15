def go():
    global res,dir
    r,c=snake[-1]
    res+=1
    nr=r+dr[dir%4]
    nc=c+dc[dir%4]
    if (nr,nc) in snake:
        return res
    snake.append((nr,nc))
    if arr[nr][nc]==0:
        snake.pop(0)
N=int(input())
K=int(input())
arr=[[0 for i in range(N)]for i in range(N)]
snake=[]
dr=[0,1,0,-1]
dc=[1,0,-1,0]
dir=4
res=0
for i in range(K):
    row,col=map(int,input().split())
    row-=1
    col-=1
    arr[row][col]=1
L=int(input())
snake.append((0,0))
for i in range(L):
    X,C=map(str,input().split())
    for i in range(int(X)):
        go()
    if C=='D':
        