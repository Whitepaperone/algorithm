
from collections import defaultdict
import sys
sys.stdin = open("4871.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E =map(int,input().split())
    checkLst=[False for i in range(V)] #해당 노드를 들렸는지 확인하는 리스트
    stackLst=[] #DFS를 위한 스택리스트
    nodeDict=defaultdict(list) #연결 노드를 리스트로 받기 위함
    for i in range(E):
        a,b=map(int,input().split())
        a-=1 #인덱스 값에 맞추기 위한 -1
        b-=1
        nodeDict[a].append(b) #해당노드에 연결노드를 value값으로 추가
    
    S,G=map(int,input().split())
    S-=1 #인덱스 값에 맞추기 위한 -1
    G-=1
    result=0
    flagB=True
    stackLst.append(S)
    checkLst[S]=True
    while checkLst[G]==False:
        if nodeDict.get(S)!=None: #해당 노드와 연결노드가 있다면
            for i in sorted(nodeDict.get(S)): #연결 노드를 숫자가 작은 순부터 들리며
                if checkLst[i]==False: #들린적이 없다면
                    S=i # 연결노드로 이동
                    checkLst[S]=True #해당 노드에 들렸음을 표시
                    stackLst.append(S) #stack의 top은 늘 현재 노드 위치
                    break
        else: #해당 노드에 연결노드가 없다면
            try:
                stackLst.pop() #해당 노드를 스택에서 팝시키고
                S=stackLst[-1] #이전 노드로 돌아간다
            except: #만약 stack에 값이 없어 pop을 시키지 못할경우
                checkLst[G]=None #while문에서 빠져나가기 위해 도착노드를 다른 값으로 저장한다
    if checkLst[G]==True:
        result=1
    print(f'#{test_case} {result}')
            