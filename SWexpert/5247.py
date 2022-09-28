def bfs(k, depth):
    global minV
    q = []
    q.insert(0,(k, depth))
    while q:
        print(q)
        nowK, nowD = q.pop()
        if nowK == M:
            minV = nowD
            return
        if nowD > minV:
            return
        for i in [nowK + 1, nowK - 1, nowK - 10, nowK * 2]:
            if 0 < i <= 1000000 and visited[i] == 0:
                visited[i] = 1
                q.insert(0,(i, nowD + 1))
    # if k == M:
    #     if minV > depth:
    #         minV = depth
    #         return
    # if depth > minV:
    #     return
    # if k <= 0:
    #     return
    # if k>1000000:
    #     return
    # solve(k + 1, depth + 1)
    # solve(k - 10, depth + 1)
    # solve(k - 1, depth + 1)
    # solve(k * 2, depth + 1)


TC = int(input())
for i in range(1, TC + 1):
    N, M = map(int, input().split())
    minV = 10000000
    visited = [0] * 1000001
    bfs(N, 0)
    print(f'#{i}', minV)
