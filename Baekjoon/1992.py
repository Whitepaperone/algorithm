def solve(n):
    print('*'*n)
    print('*',end='')
    print(' '*(n-2),end='')
    print('*',end='')
    print()
    print('*'*n)
    if n==1:
        return
    solve(n//3)
N=int(input())
res=''
solve(N)