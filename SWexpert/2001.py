import sys
sys.stdin=open('2001.txt','r')
TC=int(input())
for test_case in range(1,TC+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split()))for i in range(N)]
    total=0
    maxV=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                for m in range(M):
                    total+=arr[i+k][j+m]
            if total>maxV:
                maxV=total
            total=0
    print(f'#{test_case}',maxV)