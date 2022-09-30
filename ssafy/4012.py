def calc(lst):
    total=0
    for i in lst:
        for j in lst:
            if i!=j:
                total+=S[i][j]
    return total

# def combi(k):
#     global minV
#     if k == N // 2:
#         t = abs(calc(aList) - calc(bList))
#         if minV > t:
#             minV = t
#         return
#     for i in range(s, N - r + k):
#         aList[k] = i
#         combi(k + 1, i + 1)


def rec(k, aList, bList):
    global minV
    if k == N:
        if len(aList) == len(bList):
            t = abs(calc(aList) - calc(bList))
            if minV > t:
                minV = t
        return

    rec(k + 1, aList + [k], bList)
    rec(k + 1, aList, bList + [k])


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    # combi(0)
    minV=1e10
    rec(0, [], [])
    print(f'#{tc}',minV)
