def solve(row,col):
    Q=(row,col)
    while Q:
        row, col, cnt=Q.pop(0)
        shapeNo = T[row][col]
        for dNo in isValidDir[shapeNo]:
            newR, newC, newShape

            if newShape가 valid한지 확인:
                Q.append((newR,newC,cnt+1))

TC=int(input())
for tc in range(1,TC+1):
    N, M , R,C,L=map(int,input().split())
    T=[list(map(int,input().split())) for _ in range(N)]

    d=[(-1,0),(1,0),(0,-1),(0,1)]
    isValidShape=[[1,2,5,6],[1,2,4,7],[1,3,4,5],[1,3,6,7]]
    isValidDir=[[],[0,1,2,3],[0,1],[2,3],[0,3],[1,2],[1,3],[0,2]]
    solve(R,C,0)