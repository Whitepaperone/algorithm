def solve(y,x,n):
    global one,zero,minus
    tmp=arr[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if arr[i][j]!=tmp:
                for k in range(3):
                    for l in range(3):
                        solve(y+k*n//3,x+l*n//3,n//3)
                return
    if tmp==0:
        zero+=1
    elif tmp==1:
        one+=1
    elif tmp==-1:
        minus+=1
N=int(input())
arr=[list(map(int,input().split()))for i in range(N)]
zero=0
minus=0
one=0
solve(0,0,N)
print(minus)
print(zero)
print(one)