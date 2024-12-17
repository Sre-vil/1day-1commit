# iter은 두 개의 인자를 받아 반복 가능한 객체를 생성 
# 두번째 인자는 종료 조건 
# n = list(iter(lambda: int(input()), 0))

# for i in range(len(n)):
#     if str(n[i]) == reversed(str(n[i])):
#         print("yes")
#     else:
#         print("no")

while True:
    n = input()
    
    if n == '0':
        break
    if n == n[::-1]:
        print("yes")
    else:
        print("no")