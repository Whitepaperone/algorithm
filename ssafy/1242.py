#입력
code = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9
    }
TC=int(input())
for test_case in range(1,1+TC):
    N,M=map(int,input().split())
    ARR=[input().strip() for i in range(N)]

    # 1. 16진수를 2진수로 만든다.

    newArr=[] #N x (M*4)

    for row in range(1, N):
        if not 1 in newArr[row]:
            continue
    #2.
        j=M*4-1 #오른쪽 끝
        while j>=56:
            if newArr[row][j]==1 and newArr[row-1][j] == 0:

            # 제일 오른쪽 끝에 있는1을 찾는다
            # 코드 8개를 구한다
                for i in range(8):
                    a=[0]*3
                    #하나구하기
                    # a[2] = 1의 갯수를 세고
                    while newArr[row][j]==1:
                        a[2]+=1
                        j -= 1
                    # a[1] = 0의 갯수를 세고
                    while newArr[row][j] == 0:
                        a[1] += 1
                        j -= 1
                    # a[0] = 1의 갯수를 센다.
                    while newArr[row][j] == 1:
                        a[0] += 1
                        j -= 1
                # a[0] = 0의 갯수를 세서 버린다.
                    while newArr[row][j] == 0:
                        j -= 1
                    k=min(a)
                    # 코드 하나를 찾아온다
                    #code_pat = {221:0,221:1 와 같은 정수형태의 경우}
                    code[7-i] = code_pat[a[0]//k*100+a[1]//k*10+a[2]//k]
            # 암호 검증
            else:
                j-=1