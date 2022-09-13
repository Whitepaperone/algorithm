import sys
sys.stdin = open('5186.txt','r')
def BitPrint(i): #비트연산자로 마이너스제곱 가능할줄 알았는데 그냥 값이 날라간다고함,,
    for j in range(-1,-13,-1):
        print('1'if (i&(1<<j))else '0',end='')

def binaryF(num,depth):
    if not num:
        return ''
    if depth>13:
        return 'overflow'
    if num>=2**(-depth):
        num-=2**(-depth)
        return '1'+binaryF(num,depth+1)
    return '0'+binaryF(num,depth+1)
    pass
TC=int(input())
for test_case in range(1,TC+1):
    N=float(input())
    cnt=0
    result=binaryF(N,1)
    if 'overflow' in result:
        result='overflow'
    print(f'#{test_case}',result)