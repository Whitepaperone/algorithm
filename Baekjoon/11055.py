N = int(input())

arr=list(map(int,input().split()))
lst=[0 for i in range(N)]
dp=[]
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j] and lst[i]<lst[j]:
            dp.append(arr[i])
    lst[i]+=1
print(max(lst))