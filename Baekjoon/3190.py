N=int(input())
K=int(input())
arr=[[0 for i in range(N)]for i in range(N)]
for i in range(K):
    row,col=map(int,input().split())
    row-=1
    col-=1
L=int(input())
for i in 