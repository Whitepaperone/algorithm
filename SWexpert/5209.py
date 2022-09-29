def per(k,total):
    global minV
    if k==N:
        if minV>total:
            minV=total
        return
    if minV<total:
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            result[k]=i
            per(k+1,total+arr[k][i])
            visited[i]=False
TC=int(input())

for test_case in range(1,TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited=[False]*N
    result=[-1]*N
    minV=1500000
    per(0,0)
    print(f'#{test_case}',minV)