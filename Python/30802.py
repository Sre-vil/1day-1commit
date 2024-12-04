n = int(input()) # 참가자 수
size = list(map(int, input().split()))
t, p = map(int, input().split())

count_t = 0
count_p1 = 0
count_p2 = 0

for i in size:
    if i == 0:
        continue
    elif i % t == 0:
        count_t += i//t
    else:
        count_t += i//t + 1

count_p1 += n//p
count_p2 += n%p

print(count_t)
print(count_p1, end=' ')
print(count_p2)