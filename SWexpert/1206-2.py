import sys
sys.stdin = open("1206.txt", "r")

TC=10
for test_case in range(1,TC+1):
    N=int(input())
    arr=list(map(int,input().split()))
    res=0
    for i in range(2,N-2):
        mid=arr[i]
        left=max(arr[i-2:i])
        right=max(arr[i+1:i+3])
        if mid>max(left,right):
            res+=mid-max(left,right)
    print(f'#{test_case}',res)
