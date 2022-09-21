"""
5
3 4
1 1
1 -1
2 2
3 3
"""

TC=int(input())
lst=[list(map(int,input().split())) for i in range(TC)]
lst=sorted(lst)
for i in lst:
    print(i[0],i[1])