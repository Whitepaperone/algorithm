def tree(root):
    global total
    if arrLst[0][root]!=0:
        total+=1
        tree(arrLst[0][root])
    if arrLst[1][root]!=0:
        total+=1
        tree(arrLst[1][root])
    else:
        return total

TC=int(input())
for test_case in range(1,TC+1):
    E, N= map(int,input().split())
    arrLst=[[0 for i in range(E+2)] for i in range(2)]
    inputLst=list(map(int,input().split()))
    total=1
    for i in range(0,len(inputLst),2):
        cnt=0
        if arrLst[0][inputLst[i]]!=0:
            cnt+=1
        arrLst[cnt][inputLst[i]]=inputLst[i+1]

    tree(N)
    print(f'#{test_case}',total)