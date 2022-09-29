def find_set(x):
    while x!=lst[x]:
        x=lst[x]
    return x
def union(x,y):
    lst[find_set(y)]=find_set(x)
TC=int(input())
for test_case in range(1,TC+1):
    N,M=map(int,input().split())
    arr=list(map(int,input().split()))
    lst=[i for i in range(N+1)]
    for i in range(M):
        n1=arr[i*2]
        n2=arr[i*2+1]
        union(n1,n2)
    tmp=0
    for i in range(1,N+1):
        if lst[i]==i:
            tmp+=1
    print(f'#{test_case}',tmp)