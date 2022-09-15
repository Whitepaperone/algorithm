def pre(n):
    if n==1:
        return lst
    if parent[n]:
        lst.append(parent[n])
        pre(parent[n])

def subt(n):
    global total
    if n:
        total+=1
        subt(left[n])
        subt(right[n])
    return total


TC=int(input())

for test_case in range(1,TC+1):
    V,E,node1,node2 = map(int,input().split())
    left=[0]*(V+1)
    right=[0]*(V+1)
    parent=[0]*(V+1)
    lst=[]
    arr=list(map(int,input().split()))
    for i in range(0,E*2,2):
        parent[arr[i+1]]=arr[i]
        if not left[arr[i]]:
            left[arr[i]]=arr[i+1]
        else:
            right[arr[i]]=arr[i+1]
    lst.append(pre(node1))
    lst.append(pre(node2))
    temp=[]
    for i in lst:
        if lst.count(i)>1:
            temp.append(i)
    end=temp[0]
    total=0
    print(f'#{test_case}',end,subt(end))
