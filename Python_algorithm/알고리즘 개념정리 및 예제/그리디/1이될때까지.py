a, b = map(int, input().split())
count1 = 0

while a != 1:
    if a % b == 0 :
        a = a / b
        count1 +=1
    else:
        a -= 1 
        count1 +=1

print(count1)