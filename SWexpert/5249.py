def prim():
    U=[]
    D=[10000]*(V+1)
    D[0]=0
    while len(U)<V+1:
        minV=10000
        for i in range(V+1):
            if i in U:continue
            if minV>D[i]:
                minV=D[i]
                curV=i
        U.append(curV)
        for i in range(V+1):
            if i in U:continue
            if G[curV][i] and G[curV][i]<D[i]:
                D[i]=G[curV][i]
    return sum(D)

TC=int(input())
for test_case in range(1,TC+1):
    V,E=map(int,input().split())
    G=[[0]*(V+1)for i in range(V+1)]
    for i in range(E):
        n1,n2,w=map(int,input().split())
        G[n1][n2]=w
        G[n2][n1] = w
    W=prim()
    print(f'#{test_case}',W)
