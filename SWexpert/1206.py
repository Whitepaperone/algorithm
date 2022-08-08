import sys
sys.stdin = open("1206.txt", "r")
def getValue(Lst,pos):
    maxV=0
    for i in range(5):
        if i==2:
            continue
        if maxV<Lst[pos-2+i]:
            maxV=Lst[pos-2+i]
    if maxV< Lst[pos]:
        return Lst[pos]-maxV
    else:
        return 0

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    buildings=list(map(int,input().split()))
    sumV=0
    for i in range(2,N-2):
        t=getValue(buildings,i)
        sumV+=t
    print(f'#{test_case} {sumV}')