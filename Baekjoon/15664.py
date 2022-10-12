def per(k):
    global res
    if k==M:
        print(visited)
        tmp=[]
        for i in range(M):
            tmp.append(lst[result[i]])
        if tmp in final:
            return
        else:
            final.append(tmp)
        return
    for i in range(N):
        visited[i]=1
        result[k]=i
        per(k+1)
        visited[i]=0

N,M=map(int,input().split())
lst=list(map(int,input().split()))
visited=[0]*N
result=[-1]*N
res=[]
tmp=[]
final=[]
per(0)
final.sort()
for i in final:
    a=map(str,i)
    print(' '.join(a))