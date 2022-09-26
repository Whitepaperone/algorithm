def find():
    for i in range(len(binS)):
        # 이진수의 i번째까 틀린경우
        binL = binS[:]
        binL[i] = str((int(binS[i]) + 1) % 2)  # b = 이진수의i번째 데이터를 변경하고
        for j in range(len(triS)):  # 삼진수의 j번째가 틀린 경우
            # for k in [1,2]:
            #     t[j]=(t[j]+k)%3
            # if b(10)==t(10):
            # binS[i]=str((int(binS[i])+1)%2)
            triL = triS[:]
            for k in range(1, 3):  # t = 삼진수의 i번째 데이터를 변경해서
                triL[j] = str((int(triS[j]) + k) % 3)
                binV = int(''.join(binL), 2)
                triV = int(''.join(triL), 3)
                if binV == triV:
                    return binV
    return -1


TC = int(input())
for test_case in range(1, TC + 1):
    binS = list(input())
    triS = list(input())
    print(f'#{test_case}', find())
