def par(k, remain, ans):
    global minV
    if ans>minV:
        return
    if k == N:
        if ans < minV:
            minV = ans
        return ans
    if remain == 0:
        return
    par(k + 1, remain - 1, ans)
    par(k + 1, arr[k + 1], ans + 1)


# def per(k,total):
#     global minV
#     if k==N:
#         if minV>total:
#             minV=total
#         return
#     if minV<total:
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i]=True
#             result[k]=i
#             per(k+1,total+arr[k][i])
#             visited[i]=False

# def bus(i, n, depth):
#     global total
#     if i + n >= N - 1:
#         if depth < total:
#             total = depth
#     for k in range(1, n + 1):
#         if i + k == N:
#             total = depth + 1
#             return depth
#         if n - k >= 0:
#             bus(i + k, arr[i] - k, depth + 1)
#     return depth


TC = int(input())
for test_case in range(1, TC+1):
    arr = list(map(int, input().split())) + [0]
    total = 0
    N = arr[0]
    arr[0] = 0
    result = [-1] * (N + 1)
    ans = 0
    minV = N + 1
    par(1, arr[1], 0)
    print(f'#{test_case}', minV)
    # visited=[False]*N
    # minV=99999999999
    # per(1,arr[1])
    # print(minV)
    # print(total)
