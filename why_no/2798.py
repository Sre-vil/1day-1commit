n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
res = []
x = len(l)

while True:
    for i in reversed(range(x)):
        if i==x-1:
            res.append(l[i])
            continue
        if sum(res)+l[i] <= m and len(res) < 3:
            res.append(l[i])
        if len(res) == 3:
            break
    if len(res) == 3:
        break
    else:
        x -= 1
        res = []

print(sum(res))