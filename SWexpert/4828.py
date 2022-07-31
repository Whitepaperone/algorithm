

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N =int(input())
    while 5>N>1000:
        N=int(input())
    nLst=list(map(int,input().split()))
    maxN=max(nLst)
    print(f'#{test_case} {maxN}')