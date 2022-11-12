TC=int(input())
for test_case in range(1,TC+1):
    N=int(input())
    arr=list(map(int,input().split()))
    maxV=0
    res=0
    for i in range(N-1,-1,-1):
        if maxV<arr[i]:
            maxV=arr[i]
        else:
            res+=maxV-arr[i]
    if res<0:
        res=0
    print(f'#{test_case}',res)