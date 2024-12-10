r = 31
m = 1234567891

L = int(input())
s = input()
sum = 0

for i in range(L):
    sum += (ord(s[i])-96)*(r**i)

print(sum%m)