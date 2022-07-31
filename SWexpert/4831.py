from re import L


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K,N,M=map(int,input().split())
    while 1>K>100 or 1>N>100 or 1>M>100:
        K,N,M=int(input().split())

    gasLst=[0 for i in range(N+1)]
    busPos=[0 for i in range(N+1)]
    positionLst=map(int,input().split())
    charge=0
    lastPos=0
    temp=0
    for i in positionLst:
        gasLst[i]=1
    while lastPos+K<=N:
        for i in range(lastPos+1,lastPos+K+1):
            busPos[i]=1
            lastPos=i
        if gasLst[lastPos]==0:
            for j in range(lastPos,lastPos-K,-1):
                print(j)
                busPos[j]=0
                if gasLst[j]==1:
                    charge+=1
                    lastPos=j
                    busPos[j]=1
                    break
            if gasLst[lastPos]==0:
                lastPos=N
                charge=0
        else:
            busPos[lastPos]=1
            charge+=1
    print(f'#{test_case} {charge}')

