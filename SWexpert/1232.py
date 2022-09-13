import sys
sys.stdin=open('1232.txt','r')

def post(n):
    n=int(n)
    if n:
        post(ch1[n])

        post(ch2[n])
        if tree[n].isdigit():
            digit.append(int(tree[n]))
        else:
            digit.append(calF(tree[n]))
    return digit
def calF(tmp):
    result=0
    if tmp=='+':
        a=digit.pop()
        b=digit.pop()
        result=b+a

    elif tmp=='-':
        a = digit.pop()
        b = digit.pop()
        result = b - a

    elif tmp=='/':
        a = digit.pop()
        b = digit.pop()
        result = b // a

    elif tmp=='*':
        a = digit.pop()
        b = digit.pop()
        result = b * a
    return result
TC=10
for test_case in range(1,TC+1):
    N=int(input())
    tree=[0]*(N+1)
    ch1=[0]*(N+1)
    ch2=[0]*(N+1)
    s=[]
    digit=[]
    for i in range(N):
        temp=input().split()
        idx=int(temp.pop(0))
        if not temp[0].isdigit():
            tree[idx]=temp.pop(0)
            ch1[idx]=temp.pop(0)
            ch2[idx]=temp.pop(0)
        else:
            tree[idx]=temp.pop()


    s=post(1)
    print(f'#{test_case}',s[0])