# import sys
# sys.stdin=open('5202.txt','r')
TC = int(input())
for test_case in range(1, TC + 1):
    case = int(input())
    arr = [list(map(int, input().split())) for i in range(case)]
    tmp = [[] for i in range(case)]
    arr.sort(key=lambda x: (x[1]))
    for i in range(case):
        tmp[i].append(arr[i])
        for j in range(i + 1, len(arr)):
            if tmp[i][-1][1] <= arr[j][0] and arr[j] not in tmp[i]:
                tmp[i].append(arr[j])
    maxV=0
    for i in tmp:
        if maxV<len(i):
            maxV=len(i)
    print(f'#{test_case}',maxV)
