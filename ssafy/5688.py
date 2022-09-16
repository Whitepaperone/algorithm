def findF(num,s,e):
    if s==e and arr[s]!=num:
        return -1
    a=(s+e)//2
    if arr[a]<num:
        findF(num,a,e)
    elif arr[a]>num:
        findF(num,s,a)
    else:
        return a
TC=int(input())
arr=[i**3 for i in range(10**6)]
for test_case in range(1,TC+1):
    num=int(input())
    try:
        a=arr.index(num)
    except:
        a=-1
    print(f'#{test_case}',a)
