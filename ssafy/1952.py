def rec(k,mid):
    global minV
    if k>12:
        return
    if k==12:
        if mid<minV:
            minV=mid
        return
    rec(k+1,mid+min(ticket[1],month[k]*ticket[0]))
    rec(k+3,mid+ticket[2])

TC=int(input())
for test_case in range(1,TC+1):
    ticket=list(map(int,input().split()))
    month=list(map(int,input().split()))
    minV=1e10
    rec(0,0)
    if minV>ticket[3]:
        minV=ticket[3]
    print(f'#{test_case}',minV)