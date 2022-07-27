n = int(input()) 
minData = [0] * n
data = list(map(int, input().split()))

for i in range(n):
    minData[i] = data[i]

print(min(minData), max(minData))