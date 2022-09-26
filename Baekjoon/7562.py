from pprint import pprint
def solve(row,column):
    global depth
    lst=[]
    lst.append((row,column))
    while lst:
        curR,curC=lst.pop(0)
        if curR==goalR and curC==goalC:
            return arr[curR][curC]
        for dx,dy in [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]:
            newR=curR+dx
            newC=curC+dy
            if 0<=newR<N and 0<=newC<N and arr[newR][newC]==0:
                lst.append((newR,newC))
                arr[newR][newC]=arr[curR][curC]+1

TC=int(input())
for test_case in range(TC):
    N=int(input())
    arr=[[0 for i in range(N)]for i in range(N)]
    startR,startC=map(int,input().split())
    goalR,goalC=map(int,input().split())
    depth=0
    solve(startR,startC)
    print(arr[goalR][goalC])