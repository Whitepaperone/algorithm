import sys

sys.stdin = open("1225.txt", "r")


def encrypF(inputLst):
    isRunning = True
    while isRunning:
        for i in range(1, 6):
            temp = inputLst.pop(0)
            temp -= i
            if temp <= 0:
                inputLst.append(0)
                isRunning = False
                break
            inputLst.append(temp)
    return inputLst

for i in range(10):
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    inputLst = list(map(int, input().split()))
    lst=encrypF(inputLst)
    print(f'#{T}',end=' ')
    for i in lst:
        print(i,end=' ')
    print()
