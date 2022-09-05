import sys

sys.stdin = open("5178.txt", "r")

TC = int(input())
for test_case in range(1, TC + 1):
    N,M,L = map(int,input().split())
    arrLst=[0]+[0 for i in range(N)]
    for i in range(M):
        idx, val=map(int,input().split())
        arrLst[idx]=val

    for i in range(N,0,-1):
        if i//2>0:
            arrLst[i//2]+=arrLst[i]

    print(f'#{test_case}', arrLst[L])
