T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result=0
    str=input()
    if str==str[::-1]:
        result=1
    else:
        result=0
    print(f'#{test_case} {result}')