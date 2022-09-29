def per(k,total):
    global maxV
    if k>=1 and total<maxV:
        return
    if k==N:
        if maxV<total:
            maxV=total
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            if arr[k][i]!=0:
                per(k+1,total*arr[k][i]/100)
            visited[i]=False
TC=int(input())
for test_case in range(1,TC+1):
    N=int(input())
    arr=[list(map(int,input().split())) for i in range(N)]
    visited=[False]*N
    maxV=0
    per(0,1)

    print(f'#{test_case} {maxV*100:.6f}')