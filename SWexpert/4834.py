import sys


sys.stdin = open("4834.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    aLst=input()
    bLst=[]
    for i in aLst:
        bLst.append(int(i))
    result={k : bLst.count(k) for k in bLst}
    maxV=max(result.values())
    maxK=[k for k, v in result.items() if v == maxV]
    if len(maxK)>1:
        maxK=max(maxK)
    else:
        maxK=maxK[0]
    print(f'#{test_case}', maxK,maxV)