import sys

sys.stdin = open("5105.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    mazeLst = [list(map(int, input())) for i in range(N)]
    checkLst = [[False] * N for i in range(N)]
    pos = []
    goal = []
    stackLst = []
    for i in range(N):
        for j in range(N):
            if mazeLst[i][j] == 3:
                pos = [i, j]
            if mazeLst[i][j] == 2:
                goal = [i, j]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    result = 0
    checkLst[pos[0]][pos[1]] = True
    stackLst.append(pos)

    while len(stackLst) != 0:
        for i in range(4):
            x = pos[0] + dx[i]
            y = pos[1] + dy[i]
            if 0 <= x < N or 0 <= y < N:
                if mazeLst[x][y] == 2:
                    break
                elif mazeLst[x][y] == 0 and [x,y]not in stackLst:
                    pos[0] = x
                    pos[1] = y
                    checkLst[x][y] == True
                    stackLst.append(pos)
                    cnt += 1
                elif mazeLst[x][y] == 1:
                    continue
                elif checkLst[x][y] == True:
                    pos = stackLst.pop()
                else:
                    continue

    print(f'#{test_case} {cnt}')
