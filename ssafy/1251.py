def prim():
    U = []
    D = [MAX] * (N)  # start
    D[0] = 0
    while len(U) < (N):
        # D가 최선인 curV를 선택
        minV = MAX
        for i in range(N):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하고 연결된 D의 값을 수정
        for i in range(N):
            if i in U: continue
            if arr[curV][i] and D[i] > arr[curV][i]:
                D[i] = arr[curV][i]

    return D


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y =  list(map(int, input().split()))
    E = float(input())
    arr = [[0] * (N ) for i in range(N )]
    MAX = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                arr[i][j] = 0
            else:
                arr[i][j] = (((x[i] - x[j]) ** 2) + ((y[i] - y[j]) ** 2)) * E
                MAX += arr[i][j]
    MAX += 1

    D=prim()
    print(f'#{test_case}',round(sum(D)))
    '''
    [0, 0, 0, 0, 0]
[0, 0, 10000.0, 160000.0, 170000.0]
[0, 10000.0, 0, 170000.0, 160000.0]
[0, 160000.0, 170000.0, 0, 10000.0]
[0, 170000.0, 160000.0, 10000.0, 0]
    '''