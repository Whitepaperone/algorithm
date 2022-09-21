def fiboF(n):
    if n<=1:
        return n
    return fiboF(n-1)+fiboF(n-2)

num=int(input())
print(fiboF(num))