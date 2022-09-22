TC=int(input())
for test_case in range(1,TC+1):
    N,M=map(int,input().split())
    cont=list(map(int,input().split()))
    truck=list(map(int,input().split()))
    truck.sort(reverse=True)
    cont.sort(reverse=True)
    total=0
    for c in cont:
        if truck and c<=truck[0]:
            total+=c
            truck.pop(0)
    print(f'#{test_case}',total)