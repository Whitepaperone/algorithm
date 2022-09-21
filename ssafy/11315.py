import pprint
def cross1(mapping):
    a,b=mapping
    a+=1
    b+=1
    if a<N+1 and b<N+1:
        return f'{arr[a][b]}'+cross1((a,b))
    else:
        return ''

def cross2(mapping):
    a,b=mapping
    a+=1
    b-=1
    if a<N+1 and b<N+1:
        return f'{arr[a][b]}'+cross1((a,b))
    else:
        return ''

TC=int(input())
for test_case in range(1,TC+1):
    N=int(input())
    arr=['.'*(N+2)]+['.'+input()+'.' for i in range(N)]+['.'*(N+2)]
    pprint.pprint(arr)
    res=0
    #가로
    for i in arr:
        temp=[]
        for j in range(1,N+1):
            temp.append(i[j])
            if temp.count('o')>4:
                res='YES'
                break
            if i[j]!=i[j+1]:
                temp=[]
        if temp.count('o')>4:
            break
    #세로
    for j in range(N+1):
        temp=[]
        for i in range(1,N+1):
            temp.append(arr[i][j])
            if temp.count('o')>4:
                res='YES'
                break
            if arr[i][j]!=arr[i+1][j]:
                temp=[]
        if temp.count('o')>4:
            break
    #대각선1
    for i in range(N+2):
        temp1=cross1((i,0))
        if i!=0:
            temp2=cross1((0,i))
        if len(temp1)>4 or len(temp2)>4:
            pass