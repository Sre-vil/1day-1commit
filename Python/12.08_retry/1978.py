n = int(input())
op = list(map(int, input().split()))[:n]
count = 0

for i in op:
    if i == 1:
        continue
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        count += 1

print(count)