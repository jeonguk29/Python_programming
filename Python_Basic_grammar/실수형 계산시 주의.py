# 실수 재대로 떨어지지 않아서 round 함수로 반올림 필요

"""
a = 0.3 + 0.6

if a == 0.9:
    print(True)
else:                   
    print(False)                // 출력됨 0.89999999999999 나옴 

"""

a = 0.3 + 0.6
print(round(a, 2)) # 반올림 소수점 3번째 자리에서 반올림 한 값 출력  
if round(a, 2) == 0.9:
    print(True)
else:
    print(False)


# 참고로 나누기 수행시 실수형으로 나옴 주의
print(7/3)

# 나머지       :   정수형 반환       
print(7 % 3)       

# 몫            :   정수형 반환
print(7 // 3)


# 거듭 제곱 
print(7 ** 3)   

# 제곱근 
print(7 ** 0.5)