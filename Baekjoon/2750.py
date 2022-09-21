TC = int(input())
arr = [int(input()) for i in range(TC)]

# Insert Sort
for i in range(1, TC):
    while (i > 0) and (arr[i] < arr[i - 1]):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]

        i -= 1

for test_case in arr:
    print(test_case)