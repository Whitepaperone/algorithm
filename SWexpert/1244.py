import sys
sys.stdin=open('1244.txt','r')


TC=int(input())
for test_case in range(1,TC+1):
    arr,N=map(int,input().split())
    arr=[i for i in str(arr)]
    for j in range(N):
        maxV=0
        minV=1e10
        maxIdx=0
        minIdx=0
        for k in range(j+1,len(arr)):
            if maxV<=int(arr[k]):
                maxV=int(arr[k])
                maxIdx=k
        arr[j%len(arr)],arr[maxIdx]=arr[maxIdx],arr[j%len(arr)]
    print(f'#{test_case}',''.join(arr))