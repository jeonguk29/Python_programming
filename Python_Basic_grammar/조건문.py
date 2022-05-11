# 조건문

# 성적 구간에 따른 학점 출력 예제
score = 85

if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점 : C")
else:
    print("학점: F")


# 논리 연산자
a = 15
if a <= 20 and a >= 0:    # and , or , not 있음   ex  not X : 가 거짓일때 참이다
    print("Yes")


# in연산자 not in 연산자         in 포함되어있으면 true / not in 포함 안되어 있으면 true
print("in연산자 not in 연산자")
a = [1, 2, 3]
print(1 in a)
print(4 in a)
print(1 not in a)
print(4 not in a)

# pass 키워드
# 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용합니다.
# 예시) 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우
score = 85
if score >= 80:
    pass  # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')


# 조건문의 간소화
# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있습니다.
Score = 85
if score >= 80:
    result = "Success"
else:
    result = "Fail"
print(result)

# 조건부 표현식(Conditional Expression)은 if ~ else문을 한 줄에 작성할 수 있도록 해줍니다.
Score = 85
result = "Success" if score >= 80 else "Fail"

print(result)
