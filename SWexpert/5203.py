def check(lst):
    lst = sorted(lst)

    for i in range(len(lst)):
        if lst.count(lst[i]) == 3:
            return True
    lst=list(set(lst))
    for i in range(len(lst) - 2):

        if lst[i] == lst[i + 1] - 1 and lst[i] == lst[i + 2] - 2:
            return True

    return False


TC = int(input())
for test_case in range(1, TC + 1):
    arr = list(map(int, input().split()))
    pl1 = []
    pl2 = []
    winner = 0
    for i in range(0, len(arr), 2):
        pl1.append(arr[i])
        pl2.append(arr[i + 1])
    for i in range(3, 7):
        if check(pl1[:i]):
            winner = 1
            break

        if check(pl2[:i]):
            winner = 2
            break
    print(f'#{test_case}', winner)
