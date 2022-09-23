# def comb(n,r):
#     if r==0:
#         print(tmp)
#     elif n<r:
#         return
#     else:
#         tmp[r-1]=H[n-1]
#         comb(n-1,r-1)
#         comb(n-1,r)

TC=int(input())
for test_case in range(1,TC+1):
    N,B=map(int,input().split())
    H=list(map(int,input().split()))
    tmp=[]
    minV=999999
    # comb(N,N)
    for i in range(0,(1<<N)):
        for j in range(0,N):
            if i&(1<<j):
                tmp.append(H[j])
            if sum(tmp)>=B and abs(sum(tmp)-B)<minV:
                minV=abs(sum(tmp)-B)

        tmp=[]
    visited=[False]*N
    result=[[]for i in range(N)]
    print(f'#{test_case}',minV)