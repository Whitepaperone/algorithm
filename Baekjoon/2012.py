N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))
arr.sort()
res=0
for i in range(1,N+1):
    res+=abs(i-arr[i-1])
print(res)