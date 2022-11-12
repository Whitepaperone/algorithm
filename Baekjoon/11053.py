N = int(input())

arr=list(map(int,input().split()))
lst=[0 for i in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j] and lst[i]<lst[j]:
            lst[i]=lst[j]
    lst[i]+=1
print(max(lst))