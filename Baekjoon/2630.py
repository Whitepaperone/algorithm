def solve(y,x,n):
    global cnt,zero
    tmp=arr[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if arr[i][j]!=tmp:
                for k in range(2):
                    for l in range(2):
                        solve(y+k*n//2,x+l*n//2,n//2)
                return
    if tmp==1:
        cnt+=1
    elif tmp==0:
        zero+=1
N=int(input())
arr=[list(map(int,input().split()))for i in range(N)]
cnt=0
zero=0
solve(0,0,N)
print(zero)
print(cnt)