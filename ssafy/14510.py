TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    TREE = list(map(int, input().split()))
    maxV = max(TREE)
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        cnt1 += (maxV - TREE[i]) // 2
        cnt2 += (maxV - TREE[i]) % 2
    result = max(cnt1 * 2, cnt2 * 2 - 1)
    while result >= max(cnt1 * 2, cnt2 * 2 - 1):
        result = max(cnt1 * 2, cnt2 * 2 - 1)
        cnt1 -= 1
        cnt2 += 2
    print(f'#{test_case}', result)
