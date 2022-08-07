import sys

sys.stdin = open("4866.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result=0
    inputStr=input()
    
    stackLst=[] #괄호만 받을 스택 리스트
    for i in inputStr: #괄호찾기 순회
        print(i)
        if i=='(' or i=='{': #여는 괄호면 스택에 추가
            stackLst.append(i)
            print(stackLst)
        elif i==')' : #닫는 괄호면
            if stackLst[-1]=='(': #스택 마지막 기호가 동일한 괄호인지 체크
                stackLst.pop()
                
        elif i=='}':
            if stackLst[-1]=='{':
                stackLst.pop()
                    
            
    if len(stackLst)==0:
        result=1


    print(f'#{test_case} {result}')