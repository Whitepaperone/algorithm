'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''


def dijk():
    U = []
    D = [10000] * (N + 1) #start
    P = [10000] * (N + 1)
    D[0]=0
    while len(U) < (N + 1):
        # D가 최선인 curV를 선택
        minV = 10000
        for i in range(N + 1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하고 연결된 D의 값을 수정
        for i in range(N + 1):
            if i in U: continue
            if G[curV][i] and D[i] > D[curV]+G[curV][i]:
                D[i] = D[curV]+G[curV][i]
                P[i]=curV
    return D

TC=int(input())
for test_case in range(1,TC+1):
    N, E = map(int, input().split())
    G = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w
    # print(G)
    D= dijk()
    print(f'{test_case}',D[N])