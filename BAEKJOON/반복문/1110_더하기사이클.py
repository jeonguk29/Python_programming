n = int(input())         # 68
num = n
cnt = 0                  # 사이클 수

while True:              # while 1이랑 동일
    a = num // 10       # 6
    b = num % 10         # 8
    c = (a + b) % 10     # 6 + 8 = 1"4"
    num = (b * 10) + c   # 80 + 4 = 84

    cnt = cnt + 1        # 사이클 수 + 1
    if(num == n):        # num에서 입력된 n과 똑같은 숫자(68)가 나오면 멈춤
        break

print(cnt)
"""             
문자열로 하면 시간 초과 판정남 

n = input()                               # n = "26"
num = n
cnt = 0

while 1:
    if len(num) == 1:
        num = "0" + num
    plus = str(int(num[0]) + int(num[1]))  # 2 + 6 = "8"
    num = num[-1] + plus[-1]               # "6" + "8" = "68"
    cnt += 1
    if num == n:
        print(cnt)
        break
"""