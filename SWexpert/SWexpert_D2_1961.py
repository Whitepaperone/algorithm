import sys

sys.stdin = open('input.txt','r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    n=int(input())
    if 3>n>7:
        n= int(input())

    arr = []
    arr90=[]
    arr180=[]
    arr270=[]

    for i in range(n):
        arr.append(list(map(int, input().split())))


    for i in range(n):
        for j in range(n):
            arr90[i][j]=arr[n-1-j][i]

    for i in range(n):
        for j in range(n):
            arr180[i][j]=arr90[n-1-j][i]

        for i in range(n):
            for j in range(n):
                arr270[i][j]=arr180[n-1-j][i]

    print(f'#{test_case} ')
    for i in range(n):
        for a in range(n):
            print(arr90[i][a], end='')
        print(end=' ')
        for b in range(n):
            print(arr180[i][b], end='')
        print(end=' ')
        for c in range(n):
            print(arr270[i][c], end='')
        print()    

