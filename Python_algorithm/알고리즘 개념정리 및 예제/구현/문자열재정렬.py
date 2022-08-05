# 내가 푼 소스 
a = input()

alphabet = list(range(65,91))  # 아스키코드 숫자 범위
num = list(range(1,10))

Str = []

for i in a:
    for j in alphabet:
        if i == chr(j):
            Str.append(i)


Str = sorted(Str)

Hap = 0
for i in a:
    for j in num:
        if i == str(j):
            Hap += j

Str.append(Hap)


for i in Str:
    print(i,end='')



# 나동빈 코드 


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
