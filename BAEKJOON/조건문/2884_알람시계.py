import sys         
a, b = map(int, input().split())


#분이 -45 한게 0보다 작을때     시간에서 - 1   만약 시간이 0보다 클때는 가능 하지만 시간이 정시와 같다면 드냥 시간은 23 
if b - 45 < 0 :
    if a > 0:
        a = a - 1
        b = (60+b) - 45 
        print(a, b)
    elif a <= 0:
        a = 23
        b = (60+b) - 45 
        print(a, b)   

elif b - 45 == 0:    # 분-45 한게 0이면 그대로 쓰기     
    b = 0
    print(a, b)
elif b - 45 > 0:         # 분 -45 한게 1이상이면  
    b = b - 45
    print(a, b)