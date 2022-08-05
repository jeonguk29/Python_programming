n = int(input())

arr = list(map(int, input().split()))
MAX = max(arr)
arr2 = [0] * n

for i in range(n):
    arr2[i] = arr[i] / MAX *100

Hap = 0.0
for i in arr2:
    Hap += i



print(Hap / len(arr2))
'''
result = 0
for val in arr2:
    result += val  # 하나하나 더하기

print(f"average : {result / len(arr)}")
'''