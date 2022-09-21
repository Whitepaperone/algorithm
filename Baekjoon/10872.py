def factoF(n):
    if n==0:
        return 1
    if n>0:
        return n*factoF(n-1)

num=int(input())
print(factoF(num))