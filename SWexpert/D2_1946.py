
import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    strLst=''
    for i in range(num):
        str, size = input().split()
        for j in range(int(size)):
            strLst+=str
    print(f'#{test_case}')
    for i in range(len(strLst)):
        if i==0 or i%9!=0:
            print(strLst[i],end='')
        else:
            print(strLst[i])

    else:
        print('\n')



    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
