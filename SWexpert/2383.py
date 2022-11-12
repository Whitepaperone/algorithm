import sys
sys.stdin = open('2383.txt','r')

def solve(index):
    tmp=[]
    pr,pc=human[index]
    for i in range(len(exit)):
        sr,sc=exit[i]
        minV=abs(pr-sr)+abs(pc-sc)
        tmp.append((minV,i))
    dis,goal=min(tmp)
    lst[1][index]=dis
    goalr,goalc=exit[goal]
    lst[2][index]=arr[goalr][goalc]
    lst[3][index]=goal
    lst[2][index]+=1
    lst[2][index]+=lst[3][index]
    pass
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    result = 0
    human=[]
    exit=[]
    visited=[list(i for i in range(100))for i in range(3)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                human.append((i,j))
            if arr[i][j]>1:
                exit.append((i,j))
    lst=[list(human)for i in range(4)]
    for i in range(len(human)):
        solve(i)
    print(f'#{test_case}', max(lst[2]))
