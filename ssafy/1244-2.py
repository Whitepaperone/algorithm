

T=int(input())
for tc in range(1,T+1):
    num, cnt = input().split()
    N = len(num)
    cnt=int(cnt)
    maxV=0
    u=[[0] for i in range(11)]
    u[0].append(num)
    for k in range(cnt):
        for n in u[k]:
            tmp = list(n)
            for i in range(N-1):
                for j in range(i+1, N):
                    tmp[i],tmp[j]=tmp[j],tmp[i]
                    result = ''.join(num)
                    if result not in u[k+1]:
                        u[k+1].append(result)
    ans=max(list(map(int,u[cnt])))
    print(f'#{tc}', maxV)