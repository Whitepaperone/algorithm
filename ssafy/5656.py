def break_block(col):
    row=col의 첫번째 block의 위치를 찾아서
    lst=[]
    lst.append((row, col))
    while lst:
        size=arr[row][col]
        for i in size:
            for d in 4개 방향:
                newX,newY
                if 범위 안에 있으면:
                    lst.append((newY, nexX))
                    arr[newY][newX]=0
def drop(k):
    if k==N:
        return

    for col in range(W):
        backup=k단계의arr
        #arr수정(i번째 벽돌drop에 의한_
        break_block(i)
        clean()
