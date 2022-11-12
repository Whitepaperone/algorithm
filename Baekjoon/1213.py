arr=list(input())
arr.sort()
res=''
center=''
if len(arr)%2:
    for i in arr:
        if arr.count(i)%2:
            center+=i
    pass
else:
    for i in arr:
        if arr.count(i)%2:
            res="I'm Sorry Hansoo"
            break

print(res)