# 기본 입출력
import sys          # 표준 라이브러리에 포함되어있는 시스템 모듈을 불러옴
a, b, c = map(int, input().split())

print(a, b, c)

# 즉, 디폴트값으로 공백이 기본 구분자가 되는데

# 괄호 안에 다른 구분 문자를 넣는다면 그 구분 문자로 데이터는

# 나뉠 것이다.

# map( ) 사용 시 일괄적인 형 변환이 가능하다
# 위에서 input() 을 int()로 감싸주어 형 변환 입력을 받은 바 있다

# 복수의 데이터를 입력받으면서 모두가 숫자로 변환하고 싶다면

# map( )을 이용하자


# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))  # 리스트 각 요소를 int로 바꿀때는 이렇게 하고 
plans = input().split() # 아래와 같이 하면 문자열 리스트로 자동 변환됨 
data.sort(reverse=True)
print(data)


# 빠르게 입력 받기
# 문자열 입력 받기
data = sys.stdin.readline().rstrip()  # 이렇게 readline() 이후에
# .rstrip() 까지 한꺼번에 불러와 사용할수 있음

print(data)


# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있습니다.
# 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용합니다.
# 단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용합니다.


print("출력을 위한 전형적인 소스코드")
# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")   # end에 " "공백 넣어주면 출력이후 공백하나로 처리됨 줄바꿈이아니라
# 출력할 변수
answer = 7
print(" 정답은 " + str(answer) + "입니다.")


print("f-string 예제")
# 파이썬 3.6부터 사용 가능하며, 문자열 앞에 접두사 'f를 붙여 사용합니다.
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있습니다.
answer = 7
print(f"정답은 {answer}입니다.")
