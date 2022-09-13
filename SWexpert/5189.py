import sys
sys.stdin=open('5189.txt','r')
def per(k):
    if k==N-1:
        temp=[]
        temp.append(0)
        for i in range(N-1):
            temp.append(lst[result[i]]-1)
        temp.append(0)
        res.append(temp)
        return
    for i in range(N-1):
        if not visited[i]:
            visited[i]=True
            result[k]=i
            per(k+1)
            visited[i]=False



TC=int(input())
for test_case in range(1,TC+1):
    N=int(input())
    lst=[i for i in range(2,N+1)]
    result=[-1]*N
    visited=[False]*N
    res=[]
    per(0)
    arr=[list(map(int,input().split())) for i in range(N)]
    min=99999999
    for i in range(len(res)):
        total=0
        for j in range(len(res[0])-1):
            total+=arr[res[i][j]][res[i][j+1]]
            if total>min:
                break
        if min>total:
            min=total
    print(f'#{test_case}',min)