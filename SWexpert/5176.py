import sys

sys.stdin = open("5176.txt", "r")
def tree(node):
    global cnt
    if node<=N:
        tree(node*2)
        arrLst[node]=cnt
        cnt+=1
        tree(node*2+1)
    pass
TC=int(input())
for test_case in range(1,TC+1):
    N=int(input())
    cnt=1
    arrLst=[0 for i in range(N+1)]
    tree(1)
    print(f'#{test_case}',arrLst[1],arrLst[N//2])