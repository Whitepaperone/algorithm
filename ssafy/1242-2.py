def code_pat(a):    # 암호문 해독
    a = str(a)
    code_patt = {
        '211': 0,
        '221': 1,
        '122': 2,
        '411': 3,
        '132': 4,
        '231': 5,
        '114': 6,
        '312': 7,
        '213': 8,
        '112': 9,
    }
    return code_patt[a]


def htob(arr):  # 16진수를 2진수로 변환
    answer = ''
    for i in arr:
        if i.isdecimal():
            intC = int(i)
        else:
            intC = ord(i) - ord('A') + 10

        result = ''
        for i in range(4):
            result = str(intC % 2) + result
            intC //= 2
        answer += result

    return answer


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    r_lst = []
    for _ in range(N):
        row = input()
        r_lst.append(row)

    h_lst = []   # 16진수 list
    for i in r_lst:
        h = ''
        for j in i:
            h += htob(j)
        h_lst.append(h)

    res = 0
    for row in range(1, N):
        if h_lst[row] == '0' * M:
            continue
        j = M * 4 - 1   # 오른쪽 끝자리 idx
        while j >= 56:
            code = [0] * 8    # 암호문 8자리 초기화 list
            if h_lst[row][j] == '1' and h_lst[row-1][j] == '0': # 끝자리가 1이고, 위에서 해독하지 않은 암호문 일 때
                for i in range(8):
                    a = [0, 0, 0]   # 1, 0, 1의 비
                    while h_lst[row][j] == '1':
                        a[2] += 1
                        j -= 1
                    while h_lst[row][j] == '0':
                        a[1] += 1
                        j -= 1
                    while h_lst[row][j] == '1':
                        a[0] += 1
                        j -= 1
                    while h_lst[row][j] == '0':
                        j -= 1

                    k = min(a)  # 비 중에서 가장 최솟값
                    code[7-i] = code_pat((a[0]*100+a[1]*10+a[2]*1)//k)    # 암호문 끝자리부터 삽입

                # 암호문 검증
                odd = 0
                even = 0
                for k in range(8):
                    if k % 2 == 0:
                        odd += code[k]
                    else:
                        even += code[k]
                if (odd * 3 + even) % 10 == 0:
                    res += sum(code)
                else:
                    res += 0

            # 끝자리가 0일때 j는 1씩 감소
            else:
                j -= 1

    print(f'#{tc} {res}')