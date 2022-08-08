from copy import deepcopy
from inspect import stack
from itertools import product
import sys

sys.stdin = open("4869.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    idx=N//10
    myLst=['a','b','c'] #A=20*10 B=20*20 C=10*20
    stackLst=list(product(myLst,repeat=idx))#중복순열
    copyLst=deepcopy(stackLst) #원본에 영향이 없도록 deepcopy
    for i in copyLst: 
        temp=list(i) #튜플을 리스트로 변환
        temp.insert(0,-1) #range out of index방지
        lenT=len(temp)-1 #range out of index 방지
        for j in range(lenT): 
            lastV=temp[-1] #마지막 요소가
            if lastV=='b' or lastV=='c': #B나 C라면 두칸씩 차지해야함
                if  lastV!=temp[-2]: # 하지만 마지막 요소와 그 전요소가 같지않다면
                    stackLst.remove(i) #원본에서 해당 튜플을 제거
                    break #더이상 포문을 돌릴 이유가 없으므로 빠져나옴
                else:
                    temp.pop() #두칸을 차지하고있다면
                    temp[-1]=-1 #BBB CCC의 상황을 방지하고자 한칸을 다른값으로 대체함 ex)B,-1,(B) 
            else: #마지막 요소가 B와C가 아니라면 pop
                temp.pop()
    lenS=len(stackLst) #중복순열중 규칙에 맞지않는 튜플을 제거했으므로 요소의 개수를 파악
    print(f'#{test_case} {lenS}')