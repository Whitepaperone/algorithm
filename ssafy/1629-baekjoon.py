A,B,C=map(int,input().split())
cnt=1
def multi(A,B):
    global cnt
    print(A,B)
    if B<=0:
        return A
    A=A*A
    cnt*=2
    if cnt<B:
        B-=cnt
    multi(A,B)

print(multi(A,B))