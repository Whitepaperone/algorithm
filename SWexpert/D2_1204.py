import sys

sys.stdin = open("D2_1204.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    numLst=list(map(int,input().split()))
    numDict={}
    for num in numLst:
        if num in numDict:
            numDict[num]+=1
        else:
            numDict[num]=1
    print(f'{test_case}',max(numDict,key=numDict.get))

    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
