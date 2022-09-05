import sys

sys.stdin = open("5177.txt", "r")

TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    cnt = 0
    inputLst = [0] + list(map(int, input().split()))
    for i in range(1, N + 1):
        while inputLst[i // 2] > inputLst[i]:  # 부모가 나보다 클때 바꿔주기
            inputLst[i // 2], inputLst[i] = inputLst[i], inputLst[i // 2]
            i //= 2
    idx = len(inputLst)-1
    total = 0
    while idx != 1:
        idx //= 2
        total += inputLst[idx]

    print(f'#{test_case}', total)
