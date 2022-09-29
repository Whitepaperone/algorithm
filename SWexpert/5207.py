def binary(low, high, key):
    global total,flag

    if low > high:
        return -1
    mid = (low + high) // 2
    if key == aLst[mid]:
        total += 1
        return total
    elif key < aLst[mid]:
        if flag>=0:
            flag = -1
            binary(low, mid - 1, key)
    else:
        if flag<=0:
            flag = 1
            binary(mid + 1, high, key)


TC = int(input())

for test_case in range(1, TC + 1):
    A, B = map(int, input().split())
    aLst = list(map(int, input().split()))
    bLst = list(map(int, input().split()))
    aLst=sorted(aLst)
    bLst=sorted(bLst)

    total = 0
    for i in bLst:
        flag=0
        binary(0, len(aLst) - 1, i)
    print(f'#{test_case}', total)
