# 1
# 6개 : 2~7
# 12개 : 8~19
# 18개 : 20~37
# 24개 : 38~61

# n = int(input())
# # lv = []
# count = 0
# # tmp = []
# loc = 0
# x = 1

# for i in range(1, n+1):
#     if count == 0:
#         # lv.append([i])
#         loc += 1
#     elif count == 6*x:
#         # tmp.append(i)
#         # lv.append(tmp)
#         # tmp = []
#         count = 0
#         loc += 1
#         x += 1
#     else:
#         # tmp.append(i) # i:2, c:1
#         count += 1
#         continue
#     count += 1
    
# print(loc+1)

n = int(input())
i = 1
tmp = 0
loc = 0
x = 1

while True:
    if i == 1:
        loc += 1
        tmp += 6
    if i > tmp*x: # i:7, tmp*x:6
        loc += 1
        x += 1
    if n <= i:
        break
    i += tmp*x # i:19

print(loc)