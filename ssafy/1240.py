arr = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3','0100011' : '4','0110001' : '5', '0101111': '6',
       '0111011':'7' ,'0110111' : '8', '0001011': '9'}


def encrypt(n):
    return arr[n]
def checkF(n):
    even=0
    odd=0
    for i in range(8):
        if i%2==1:
            even+=int(n[i])
        else:
            odd+=int(n[i])
    if (odd*3+even)%10==0:
        return odd+even
    else:
        return 0



TC=int(input())
for test_case in range(1,TC+1):
    N,M=map(int,input().split())
    inputLst=[input() for i in range(N)]
    result=''
    ans=''
    total=0
    for i in inputLst:
        if i.count('1')>0:
            temp=i.rstrip('0')
            temp=temp[-56:]
            for i in temp:
                result+=i
                if len(result)==7:
                    ans+=encrypt(result)
                    if len(ans)==8:
                        total=checkF(ans)
                        ans=''
                    result=''
    print(f'#{test_case}',total)
