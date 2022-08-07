import sys

sys.stdin = open("4873.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    inputStr=input()    
    stackLst=[] #괄호만 받을 스택 리스트
    for i in inputStr: #괄호찾기 순회
        if len(stackLst)==0:
            stackLst.append(i)
        elif i == stackLst[-1]:
            stackLst.pop()
        else:
            stackLst.append(i)
        
    result=len(stackLst)


    print(f'#{test_case} {result}')