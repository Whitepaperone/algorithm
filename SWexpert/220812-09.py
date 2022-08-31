import sys

sys.stdin = open("220812-09.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    bus_line = int(input())
    bus_normal = []
    bus_fast = []
    bus_far_fast = []
    for i in range(1, bus_line + 1):
        bus, start, end = map(int, input().split())
        if bus == 1:
            for i in range(start, end + 1):
                bus_normal.append(i)
        elif bus == 2:
            for i in range(start, end + 1, 2):
                bus_fast.append(i)
            if end not in bus_fast:
                bus_fast.append(end)
        else:
            for i in range(start, end + 1):
                if start % 2 and i % 4 == 0:
                    bus_far_fast.append(i)
                elif start % 2 == 0 and i % 3 == 0 and i % 10 != 0:
                    bus_far_fast.append(i)
            if start not in bus_far_fast:
                bus_far_fast.insert(0, start)
            if end not in bus_far_fast:
                bus_far_fast.append(end)
    print(set(bus_normal) & set(bus_fast) & set(bus_far_fast))
    print(bus_normal,bus_fast,bus_far_fast)
