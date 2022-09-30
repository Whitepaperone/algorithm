def re(k, midS):
    global maxV, minV

    if not max(op):
        if midS > maxV:
            maxV = midS
        if midS < minV:
            minV = midS
        return

    for i in range(4):
        if op[i]:
            if i == 0:
                op[0] -= 1
                res[k] = '+'
                re(k + 1, midS + src[k])
                op[0] += 1
            if i == 1:
                if op[1]:
                    op[1] -= 1
                    res[k] = '-'
                    re(k + 1, midS - src[k])
                    op[1] += 1
            if i == 2:
                if op[2]:
                    op[2] -= 1
                    res[k] = '*'
                    re(k + 1, midS * src[k])
                    op[2] += 1
            if i == 3:
                if op[3]:
                    op[3] -= 1
                    res[k] = '/'
                    re(k + 1, midS // src[k] if midS > 0 else -1*(abs(midS)//src[k]))
                    op[3] += 1


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    op = list(map(int, input().split()))
    src = list(map(int, input().split()))
    maxV = -1e10
    minV = 1e10
    res = [-1] * (N)
    re(1, src[0])
    # print(re(0, src[0]), maxV, minV)
    print(f'#{test_case}',maxV-minV)