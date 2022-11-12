def right(x,y,index):

    if index>N**2:
        return
    if 0<=x<N and 0<=y<N:
        if not visited[x][y]:
            visited[x][y]=True
            arr[x][y]=index
            right(x,y+1,index+1)
        else:
            down(x + 1, y - 1, index)
    else:
        down(x+1,y-1,index)
def down(x,y,index):
    if index>N**2:
        return
    if 0<=x<N and 0<=y<N:
        if not visited[x][y]:
            visited[x][y]=True
            arr[x][y]=index
            down(x+1,y,index+1)
        else:
            left(x - 1, y - 1, index)
    else:
        left(x-1,y-1,index)
def left(x,y,index):

    if index>N**2:
        return
    if 0<=x<N and 0<=y<N:
        if not visited[x][y]:
            visited[x][y]=True
            arr[x][y]=index
            left(x,y-1,index+1)
        else:
            up(x - 1, y + 1, index)
    else:
        up(x-1,y+1,index)
def up(x,y,index):

    if index>N**2:
        return
    if 0<=x<N and 0<=y<N:
        if not visited[x][y]:
            visited[x][y]=True
            arr[x][y]=index
            up(x-1,y,index+1)
        else:
            right(x + 1, y + 1, index)
    else:
        right(x+1,y+1,index)

T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    arr=[[0 for i in range(N)]for i in range(N)]
    visited=[[False for i in range(N)]for i in range(N)]
    right(0,0,1)
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()
