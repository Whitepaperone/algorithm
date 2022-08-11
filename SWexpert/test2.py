lst = [10, 20, 30, 40]
num = 5
result = []
for j in range(len(lst)):
    check = 1 << j
    if num & check:
        result.append(lst[j])
print(result)
print(bin(1),print(1<<1),bin(1<<2),bin(2),bin(3))