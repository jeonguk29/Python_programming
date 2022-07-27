
data = [0]*9

for i in range(9):
    data[i] = int(input()) 

max_value = max(data)

print(max_value)
print(data.index(max_value)+1)