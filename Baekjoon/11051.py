TC=int(input())
for test_case in range(1,TC+1):
    N=int(input())
    arr=list(map(int,input().split()))
    maxV=0
    res=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i]<maxV:
            res+=maxV-arr[i]
        else:
            maxV=arr[i]
    print(res)