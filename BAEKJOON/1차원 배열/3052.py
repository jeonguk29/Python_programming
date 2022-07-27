num = [0] * 10
result = [0] * 10
result2 = [0] * 10
j = 0
z = 0
count = 0
for i in range(10):
    num[i]=int(input()) 
print(num)

for i in num:
    result[j]= i % 42 
    j = j+1

print(result)

for a in range(10):
    for b in range(10):
        if result[a] == result[b]:
            result2[a] == 1

print(result2)
