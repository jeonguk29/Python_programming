# 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시 해야함
# 종료 조건을 제대로 명시 하지 않으면 함수가 무한히 호출될 수 있습니다.

def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')


recursive_function(1)

# 이처럼 재귀함수를 이용하게 되면 마치 스택에 데이터를 넣었다가 꺼내는것과 마친가지임
# 실제로 스텍 프레임에 담겨서 차례대로 종료가 됨


# 팩토리얼 구현 예제  n! = 1 x 2 x 3 x....x(n-1)x n
# 수학적으로 0!과 1!의 값은 1입니다.
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!


def factorial_recursive(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)


# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))


# 최대공약수 계산 (유클리드 호제법) 예제
# https://www.youtube.com/watch?v=TxdljAFjTNw 설명 참고

# 최대공약수 계산 (유클리드 호제법) 예제
# 유클리드 호제법
# 두 자연수 A, B에 대하여 (A〉B) A를 B로 나눈 나머지를 R이라고 합시다.
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))





# 재귀 함수 사용의 유의 사항
# 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있습니다.
# 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 합니다.
# 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있습니다.
# 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있습니다.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓입니다.
# 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많습니