
n = int(input())
taget = 3; 
count = 0;

for i in range(n+1): # 시간
    for j in range(0,60):  # 분
        for z in range(0,60): # 초 or 초 분 or 초 분 시간  
            if '3' in str(i) + str(j) + str(z):
                count += 1
print(count)
