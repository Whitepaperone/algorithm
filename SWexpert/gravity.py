lst=[7, 4, 2, 0, 0, 6, 0, 7, 0]
N = 9
maxV=0
maxP=0

for i in range(0,N-1):
    cnt=0
    for pos in range(i+1,N):
        if lst[i] > lst[pos]:
            cnt+=1
    if maxV<cnt:
        maxV=cnt
        maxP=i
print(maxV,maxP)  
