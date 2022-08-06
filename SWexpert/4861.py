
import sys
sys.stdin = open("4861.txt", "r")

def divideStr(strV): #입력받은 문자열은 반절씩 슬라이싱해 비교하는 함수
    a=len(strV) #문자열 길이 구하기
    b=a//2 #문자열의 반절이 어느 인덱스인지 구하기
    c=strV[:b] #인덱스까지 슬라이싱
    d=strV[-1:a-b-1:-1] #오른쪽에서부터 인덱스 칸수만큼 역으로 슬라이싱
    if c==d: #슬라이싱한 왼쪽열과 오른쪽열이 같다면 해당 문자 반환
        return strV


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    result =''
    Narray=[]
    b=''
    #배열 만들기
    for i in range(N):
        Narray.append(input())

    for i in range(N):
        a=Narray[i] #i번째 행의 가로 문자 구하기
        for j in range(N):
            b+=Narray[j][i] #i번째 열의 세로 문자 구하기
        for k in range(N-M+1): #M만큼의 문자열 구하기
            c=a[k:k+M] #가로열의 M만큼 슬라이싱
            d=b[k:k+M] #세로열의 M만큼 슬라이싱

            if divideStr(c) != None: #회문이라서 값을 반환받았다면 결과값을 저장, 문제에서 출력이 리스트가 아니어서 한개의 문자열만 저장함
                result=c
            if divideStr(d) != None:
                result=d
        b='' #위에서 문자열로 받았으므로 초기화 시켜줘야함
    print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
