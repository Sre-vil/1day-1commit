# n, m = map(int, input().split())
# l = sorted(list(map(int, input().split())))
# res = []
# x = len(l)

# while True:
#     for i in reversed(range(x)):
#         if i==x-1:
#             res.append(l[i])
#             continue
#         if sum(res)+l[i] <= m and len(res) < 3:
#             res.append(l[i])
#         if len(res) == 3:
#             break
#     if len(res) == 3:
#         break
#     else:
#         x -= 1
#         res = []

# print(sum(res))

N, M = map(int, input().split())
sum = []

card = sorted(list(map(int, input().split())))

for i in range (len(card)) :
    for j in range (i+1, len(card)) :
        for k in range (j+1, len(card)) :
            sum.append(card[i] + card[j] + card[k])
sum = sum.sort()
for i in range (len(sum)) :
    if sum[i] == M :
        print(M)
        break
    elif sum[i] > M :
        print(sum[i-1])
        break
        