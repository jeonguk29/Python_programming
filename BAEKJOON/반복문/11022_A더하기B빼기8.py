import sys
n = int(input())

num1 = [0] * n
num2 = [0] * n
hap = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    num1[i] = a
    num2[i] = b
    hap[i] = a+b

for i in range(n):
    print("Case #{0}: {1} + {2} = {3}".format(i+1,num1[i],num2[i],hap[i]))    # Case #1: 1 + 1 = 2