def partition(L, R):
    p = L
    i = L + 1
    j = R
    while i <= j:
        while i <= j and arr[i] < arr[p]:
            i += 1
        while i <= j and arr[j] > arr[p]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[j] = arr[j], arr[p]
    return j


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


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_s(0, len(arr) - 1)
print(arr)
