def BitPrint(i):
    for j in range(3,-1,-1):
        print('1'if (i&(1<<j))else '0',end='')
def binaryF(num):
    str=[]
    while num>1:
        str.append(num%2)
        num//=2
    str.append(num)
    while len(str)!=4:
        str.append(0)
    print(str)
    return str[::-1]
TC=int(input())
for test_case in range(1,TC+1):
    N, str=input().split()
    stackL=[]
    print(f'#{test_case}',end=' ')
    for i in str:
        if i.isdigit():
            num=int(i)
            stackL.append(BitPrint(num))
        else:
            num=ord(i)-55
            stackL.append(BitPrint(num))
    print()