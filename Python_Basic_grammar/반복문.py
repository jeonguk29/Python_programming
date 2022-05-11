
print("1부터 9까지 모든 정수의 합 구하기")
i = 1
result = 0
# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)


print("1부터 9까지 홀수의 합 구하기 예제 (while문)")
i = 1
result = 0
# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

# 무한루프 조심 조건 갑이 ture이면 계속 무한루프 돌거임
# x = 10
# while x > 5:
#     print(x)

print("반복문 for문")
array = [9, 8, 7, 6, 5]

for x in array:
    print(x)


print("1부터 30까지 모든 정수의 합 구하기 예제 (for문)")
result = 0

for i in range(1, 31):
    result += i
print(result)


# 파이썬의 continue 키워드
# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue를 사용합니다.
# 1부터 9까지의 홀수의 합을 구할 때 다음과 같이 작성할 수 있습니다.
print("continue 키워드이용")
result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i
print(result)


# 파이썬의 break 키워드
# 반복문을 즉시 탈출하고자 할 때 break를 사용합니다.
# 1부터 5까지의 정수를 차례대로 출력하고자 할 때 다음과 같이 작성할 수 있습니다.

print("break 키워드 이용")
i = 1
while True:
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1


print("학생들의 합격 여부 판단 예제 1) 점수가 80점만 넘으면 합격")
scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다. ")


print("학생들의 합격 여부 판단 예제 2) 특정 번호의 학생은 제외하기")
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}
for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다. ")

print("2중 for문 구구단 예제")

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i * j)
    print()
