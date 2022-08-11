import sys

sys.stdin = open("1209.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    arrV=[list(map(int,input().split())) for i in range(100)]
    total=0
    maxV=0
    for i in arrV:
        for j in i:
            total+=j
        if maxV<total:
            maxV=total
        total=0
    for i in range(100):
        for j in range(100):
            total+=arrV[j][i]
        if maxV < total:
            maxV = total
        total = 0
    for i in range(100):
        total+=arrV[i][i]
        if maxV < total:
            maxV = total
        total = 0
    for i in range(100):
        total+=arrV[i][99-i]
        if maxV < total:
            maxV = total
        total = 0
    print(f'{test_case} {maxV}')
    pass
