
import sys
sys.stdin = open("4865.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1=input() #문자열 입력받기
    str2=input()
    dict1={k:0 for k in str1} #문자열의 문자를 키로 딕셔너리 만들기
    dict2={k:0 for k in str2}

    for i in str1: #str1의 문자를 카운트
        if dict1[i]==0:
            dict1[i]+=1
        else:
            dict1[i]+=1

    for i in str2: #str2의 문자를 카운트
        if dict2[i]==0:
            dict2[i]+=1
        else:
            dict2[i]+=1
    aLst=[]
    for i in dict1.keys(): #dict1의 키를 대상으로
        aLst.append(dict2.get(i)) #dict2에서 value값을 가져와서 Lst에 추가해주고
    result =max(aLst) #그중 max값을 찾음 
    print(f'#{test_case} {result}')