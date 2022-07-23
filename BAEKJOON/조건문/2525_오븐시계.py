import sys         
a, b = map(int, input().split())
c = int(input())

a += c // 60  # 60을 나눈 몫만 하면 시간
b += c % 60  # 60을 나눈 나머지만 하면 분


if b >= 60 :
    a += 1        # 분이 60을 넘을때 시간에 1더하거
    b = b % 60    # 나머지 값을 분으로

if a >= 24 :    #만약 24보다 시간이 크다면
    a = a - 24  # 24를 빼서 시간 단위를 맞춰줌 


print(a, b)