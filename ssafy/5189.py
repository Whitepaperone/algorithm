def perm(k, midSum, s):
    global minV
    if k==N:
        # for ...:
        # #
        # sumV =0
        # for i in range(1,N):
        #     s=result[i-1]
        #     e=result[i]
        #     sumV+=ARR[s][e]
        # s=result[N-1]
        # sumV +=ARR[s][0]
        midSum+=ARR[s][0]
        minV=min(minV,midSum)
        return
    for i in range(N):
        if visited[i]:
            continue
        # result[k]=i #
        # s=result[k-1]
        visited[i]=True
        # perm(k+1, midSum+ARR[s][i])
        perm(k+1,midSum+ARR[s][i],i)
        visited[i]=False
N=5
visited=[False]*N
result=[-1]*N
TC=int(input())
for test_case in range(1,TC):
    N=int(input())
    ARR=[list(map(int,input().split()))for i in range(N)]
    # perm(0)
    visited=[0]*N
    minV=9999
    visited[0]=True
    result[0]=0
    perm(1,0,0)
    print(f'#{test_case}',minV)