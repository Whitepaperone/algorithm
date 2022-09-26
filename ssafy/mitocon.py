def check():
    ARR.sort()
    pre = 0
    for k in range(1, K):
        if ARR[k][2] == 0: continue
        if ARR[pre][0] == ARR[k][0] and ARR[pre][1] == ARR[k][1]:
            ARR[k][2] += ARR[pre][2]
            ARR[pre][2] = 0
        pre = k


dc = [0, 0, 0, -1, 1]
dr = [0, -1, 1, 0, 0]
rev = [0, 2, 1, 4, 3]
TC = int(input())
for test_case in range(1, TC + 1):
    N, M, K = map(int, input().split())

    ARR = [ list(map(int, input().split())) for i in range(K)]
    for t in range(M):
        for k in range(K):
            if ARR[k][2] == 0: continue
            newR = ARR[k][0] + dr[ARR[k][3]]
            newC = ARR[k][1] + dc[ARR[k][3]]
            if newC == 0 or newC == N - 1 or newR == 0 or newR == N - 1:
                ARR[k][2] //= 2
                ARR[k][3] = rev[ARR[k][3]]
            ARR[k][0] = newR
            ARR[k][1] = newC
        check()
    sumV = 0
    for i in range(K):
        sumV += ARR[i][2]
    print(f'#{test_case}', sumV)
