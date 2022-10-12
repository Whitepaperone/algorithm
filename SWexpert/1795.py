# def dijk(check):
#     U = [False] * (N + 1)
#     D = [1e5] * (N + 1)  # start
#     D[X] = 0
#     while U.count(True) < N:
#         minV = 1e5
#         for i in range(N + 1):
#             if U[i]: continue
#             if minV > D[i]:
#                 minV = D[i]
#                 curV = i
#
#         U[curV] = True
#         # curV하고 연결된 D의 값을 수정
#         for i in range(N + 1):
#             if U[i]: continue
#             if check==1:
#                 D[i] = min(D[i], D[curV] + gr[curV][i])
#             else:
#                 D[i] = min(D[i], D[curV] + gr[i][curV])
def dijk(gr):
    U = [False] * (N + 1)
    D = [1e5] * (N + 1)  # start
    D[X] = 0
    while U.count(True) < N:
        minV = 1e5
        for i in range(N + 1):
            if U[i]: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U[curV] = True
        # curV하고 연결된 D의 값을 수정
        for i in range(N + 1):
            if U[i]: continue
            D[i] = min(D[i], D[curV] + gr[curV][i])
    return D


TC = int(input())
for tc in range(1, TC + 1):
    N, M, X = map(int, input().split())
    G1 = [[1e5] * (N + 1) for _ in range(N + 1)]
    G2 = [[1e5] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        G1[x][y] = c
        G2[y][x] = c

    a=dijk(G1)
    b=dijk(G2)
    total=0
    for i in range(1,N+1):
        if a[i]+b[i]>total:
            total=a[i]+b[i]

    print(f'#{tc}',total)
