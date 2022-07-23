import sys
n = int(input())

hap = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    hap[i] = a+b

for i in range(n):
    print("Case #{0}: {1}".format(i+1,hap[i]))    # Case #1: 2