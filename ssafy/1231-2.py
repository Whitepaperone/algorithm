"""
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
"""


def inorder(v):
    global answer
    if v:
        inorder(left[v])  # 왼쪽 서브트리의 루트로 이동
        answer += tree[v]
        inorder(right[v])  # 오른쪽 서브트리의 루트로 이동


TC = 10
for test_case in range(1, TC + 1):
    N = int(input())
    left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽 자식 저장
    right = [0] * (N + 1)  # 부모를 인덱스로 오른쪽 자식 저장
    tree = [0] * (N + 1)  # 노드 데이터 저장
    for _ in range(N):
        arr = input().split()
        p = int(arr[0])
        tree[p] = arr[1]
        if len(arr) >= 3:
            left[p] = int(arr[2])  # 왼쪽 자식
        if len(arr) == 4:
            right[p] = int(arr[3])  # 오른쪽 자식

    answer = ''
    inorder(1)  # 완전 이진트리의 루트부터 순회
    print(f'#{test_case}', answer)
