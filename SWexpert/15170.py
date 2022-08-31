import sys

sys.stdin = open("15170.txt", "r")
def findP(i,j):
    while placeLst[j]!=1:
        if visited[i]==0:
            placeLst[i]-=1
            visited[i]+=1
        else:
            for di in [1,-1]:
                a=i+di
                if 0<a<
                i=a
                findP(a,j)



TC = int(input())
for test_case in range(1, TC + 1):
    stackL=[]
    N = int(input())
    placeLst = [0] * (N + 1)
    visited = [0] * (N + 1)
    place = []
    for i in range(3):
        a, b = map(int, input().split())
        place.append(a)
        placeLst[a] = b
    print(placeLst)
    for j in place:
        findP(j,j)
