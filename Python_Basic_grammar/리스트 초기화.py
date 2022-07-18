# 리스트 초기화
# 직접 데이터를 넣어 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
# 네 번째 원소만 출력
print(a[3])
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)


print("리스트의 인덱싱과 슬라이싱")
# 리스트의 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 여덟 번째 원소만 출력
print(a[7])
# 뒤에서 첫 번째 원소 출력
print(a[-1])
# 뒤에서 세 번째 원소 출력
print(a[-3])


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 네 번째 원소만 출력
print(a[3])
# 두 번째 원소부터 네 번째 원소까지
print(a[1: 4]) # 즉 앞에인덱스는 1 끝에 인덱스는 +1 한 값을 가져옴 3까지  즉 인덱스 1부터 4전까지  




print("리스트 컴프리헨션")
# 리스트 컴프리헨션
# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)


# 내부적으로 반복문 조건문 사용가능
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트  
array = [i for i in range(20) if i % 2 == 1]
print(array)
# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)



print("리스트 컴프리헨션을 이용해 N X M 크기의 2차원 리스트 초기화 ")
# 리스트 컴프리헨션 (좋은 예시)
# NXM 크기의 2차원 리스트 초기화
n = 4
m = 3
# 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할때 _ 를 사용함
"""
for _ in range(5)
    print("Hello world") 단순 5번 출력 

"""

array = [[0] * m for _ in range(n)]
print(array)


print("리스트 관련 기타 메서드")

# 리스트 관련 기타 메서드
a = [1, 4, 3]
print("기본 리스트: ", a)
# 리스트에 원소 삽입
a.append(2)
print("삽입 : ", a)
# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)


# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)


# 리스트 관련 기타 메서드
a = [4, 3, 2, 1]
# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)
# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)
# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수:", a.count(3))
# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)


# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}  # 이 집합 자료형은 특정한 원소의 존재유무 만을 체크하고자 할때 매우 효과적으로 사용될 수 있는 자료형
# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
