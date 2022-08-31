import sys

sys.stdin = open("1223.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    inputLst = input()
    result = ''
    stackLst = []
    for i in inputLst:
        if i.isdigit():
            result += i
        else:
            if i == '*':
                while stackLst and stackLst[-1] == '*':
                    result += stackLst.pop()
                stackLst.append(i)
            elif i == '+':
                while stackLst:
                    result += stackLst.pop()
                stackLst.append(i)

    while stackLst:
        result += stackLst.pop()

    for i in result:
        if i.isdigit():
            stackLst.append(int(i))
        else:
            num1=stackLst.pop()
            num2=stackLst.pop()
            if i=='+':
                stackLst.append(num2+num1)
            else:
                stackLst.append(num2*num1)
    ans=stackLst.pop()

    print(f'{test_case}',ans)
