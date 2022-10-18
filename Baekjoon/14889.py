def calc(lst):
    total=0
    for i in lst:
        for j in lst:
            if i!=j:
                total+=arr[i][j]
    return total
def rec(k,aList,bList):
    global minV
    if k==N:
        if len(aList)==len(bList):
            tmp=abs(calc(aList)-calc(bList))
            if minV>tmp:
                minV=tmp
        return

    rec(k+1,aList+[k],bList)
    rec(k+1,aList,bList+[k])


minV=1e10
N=int(input())
arr=[list(map(int,input().split()))for i in range(N)]
rec(0,[],[])
print(minV)