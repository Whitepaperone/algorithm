def partitionL(L, R):
    p = R
    i = L - 1
    for j in range(L, R):
        if arr[j] < arr[p]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[p], arr[i] = arr[i], arr[p]
    return i


def quick_s(L, R):
    if L<R:
        p = partitionL(L, R)
        quick_s(L, p - 1)
        quick_s(p + 1, R)


TC=int(input())
for test_case in range(1,TC+1):
    N=int(input())
    arr=list(map(int,input().split()))
    quick_s(0, len(arr) - 1)
    print(f'#{test_case}',arr[N//2])
