# <문제> 시각: 문제 설명
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성하세요. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되
# 어 있으므로 세어야 하는 시각입니다.
# 00시 00분 03초
# 00시 13분 30초
# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각입니다.
# 00시 02분 55초
# 01시 27분 45초
# 구현: 시뮬레이션과 완전 탐색


# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


# 내가 틀린 이유  시간, 분, 초 각각 카운트만 하고 시간 분 초 연달아 나올때 카운트가 없게됨

# n = int(input())
# count = 0

# for h in range(n+1):
#     if h == 3 or h == 13 or h == 23:
#         count += 1
#     for m in range(60):
#         if m == 3 or m == 13 or m == 23 or m == 33 or m == 43 or m == 53:
#             count += 1
#         for s in range(60):
#             if s == 3 or s == 13 or s == 23 or s == 33 or s == 43 or s == 53:
#                 count += 1

# print(count)


# <문제> 왕실의 나이트: 문제 설명
# 행복 왕국의 왕실 정원은 체스판과 같은 8x8좌표 평면입니다. 왕실 정원의 특정한 한 칸에 나이트가 서
# 있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없
# 습니다.
# 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.

# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])  # 행위치
column = int(ord(input_data[0])) - int(ord('a')) + \
    1  # 아스키 코드 형태로 바꾸고 계산하면 열위치임

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


# <문제> 문자열 재정렬: 문제 설명
# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으
# 로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
# 구현: 시뮬레이션과 완전 탐색


# <문제> 문자열 재정렬: 답안 예시 (Python)
data = input()
result = []

value = 0
# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입    https://appia.tistory.com/178   참고
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
# https://blockdmask.tistory.com/468 조인 함수 설명 리스트를 문자열로 반환해줌
