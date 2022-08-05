from itertools import combinations  # 조합 구할때 사용
from itertools import permutations  # 순열 구할때 사용
from itertools import product  # 중복 순열때 사용
from itertools import combinations_with_replacement  # 중복 조합때 사용
from collections import Counter  # Counter 이용시 사용
import math  # 최대공약수, 최대공배수, 팩토리얼 등등 이용시 사용

print("자주 사용되는 내장 함수")
# sum()
result = sum([1, 2, 3, 4, 5])
print(result)
# min(), max(()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)


# eval()
# eval 함수는 흔히 사람에 입장에서 이렇게 수식으로 표현된 하나의 식이 있을때 이제
# 이것을 계산한 결과를 실제 수 형태로 반환해주는 함수입니다.
result = eval("(3+5)*7")
print(result)


# 자주 사용되는 내장 함수  그중 정렬함수
# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)
# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)


# 순열과 조합
# 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# {'A', 'B', 'C}에서 두 개를 선택하여 나열하는 경우: 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
print("순열")
# from itertools import permutations # 순열 구할때 사용
data = ['A', 'B', 'C']  # 데이터 준비
result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

# 이렇게 순열의 수를 구해 보았을때 값이 천만 1억 단위를 넘어가는 경우 완전탐색을 이용했을때 시간 초과 판정을 받을 확률이 높기 때문에 실제로 전체 경우의 수를 고려할때 이러한 순열의 수와 조합의 수를 많이 계산하게 됩니다 자 먼저

print("조합")
# from itertools import combinations # 조합 구할때 사용
data = ['A', 'B', 'C']  # 데이터 준비
result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)


print("중복 순열과 중복 조합")
# from itertools import product # 중복 순열위해 사용
data = ['A', 'B', 'C']  # 데이터 준비
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

# from itertools import combinations_with_replacement 중복 조합 위해 사용
data = ['A', 'B', 'C']  # 데이터 준비
result = list(combinations_with_replacement(
    data, 2))  # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)


# Counter
# 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공합니다.
# 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지를 알려줍니다.
# from collections import Counter  # Counter 이용시 사용

print("counter 사용")
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])  # 'blue'가 등장한 횟수 출력
print(counter['green'])  # 'green'이 등장한 횟수 출력
print(dict(counter))  # 사전 자료형으로 반환


# 최대 공약수와 최소 공배수
# 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd()) 함수를 이용할 수 있습니다.
# import math 필요함
# 최소 공배수(LCM)를 구하는 함수
print("최대 공약수 최대 공배수")


def lcm(a, b):
    return a * b // math.gcd(a, b)


a = 21
b = 14
print(math.gcd(21, 14))  # 최대 공약수(GCD) 계산
print(lcm(21, 14))  # 최소 공배수(LCM) 계산


# 최대 공약수란 : 두 수가 주어졌을때 공통된 약수중에서 가장 큰 값을 의미

# 최소 공배수란 : 공통된 배수 중에서 가장 작은 값을 의미합니다

# 이밖에도 math라이브러리는 팩토리얼 과 재곱끈 과 같은 다양한 함수부터 원주율과 같은 상수 까지 포함하고 있으니까 여러분들이 수학적 기능이 필요할때 마다 요긴하게 호출해서 사용할수 있습니다



# 알파벳인경우 확인 함수

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

# 리스트 한줄에 출력 
# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))




#문자열 교체 

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수 i 와 같은게 있다면 *로 바꿔버림 
    print(word)
print(word)
print(len(word))

