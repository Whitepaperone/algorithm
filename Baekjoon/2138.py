def push(index):
    if 0 <= index - 1 and index + 1 < N:
        arr[index - 1] = abs(arr[index - 1] - 1)
        arr[index] = abs(arr[index] - 1)
        arr[index + 1] = abs(arr[index + 1] - 1)
    elif index == 0:
        arr[index] = abs(arr[index] - 1)
        arr[index + 1] = abs(arr[index + 1] - 1)
    elif N-1 == index:
        arr[index - 1] = abs(arr[index - 1] - 1)
        arr[index] = abs(arr[index] - 1)
    elif index - 1 < 0 and N < index + 1:
        arr[index] = abs(arr[index] - 1)


N = int(input())
arr = list(map(int,input()))
pair = list(map(int,input()))
cnt = 0
isRunning = True
for i in range(N):
    for j in range(N):
        if arr[j] != pair[j]:
            push(j)
            cnt+=1
        arr_str=list(map(str,arr))
        pair_str=list(map(str,pair))
        if ''.join(arr_str)==''.join(pair_str):
            break
    if ''.join(arr_str)==''.join(pair_str):
        break
if ''.join(arr_str)!=''.join(pair_str):
    cnt=-1
print(cnt)
