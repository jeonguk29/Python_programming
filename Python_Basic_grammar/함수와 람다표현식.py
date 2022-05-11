print("더하기 함수 예시 1")


def add(a, b):
    return a + b


print(add(3, 7))    # 3,7 을 인자값    함수안에 있는 a,b를 매개변수라고 사용함

print("더하기 함수 예시 2")


def add(a, b):
    print('함수의 결과:', a + b)


add(3, 7)


# 파라미터 지정하기
# 파라미터의 변수를 직접 지정할 수 있습니다.
# 이 경우 매개변수의 순서가 달라도 상관이 없습니다.
def add(a, b):
    print('함수의 결과:', a + b)


add(b=3, a=7)


print("global 키워드")
# global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를
# 바로 참조하게 됩니다. 주로 전역변수에 값을 바꾸려고 할때 사용함 일반출력및 전역변수에 연산 출력은 가능하기 때문

# https://dojang.io/mod/page/view.php?id=2364    전역범위, 지역범위 참조
a = 0


def func():
    global a  # 전역변수에 값 변화
    a += 1


a = 10


def func():
    print(a + 20)  # 이렇게 전역변수에 값이 바뀌지 않는다면 이렇게 출력가능함


func()


array = [1, 2, 3, 4, 5]


def func():
    array.append(6)
    print(array)


func()


# 또한 한가지 유의하면 좋은점은 전역변수로 한가지 리스트가

# 선언되어있을때 전역변수로 선언된 리스트객체에 내부메서드를 호출하는 것은 또 오류없이 수행가능함 보면 6 추가됨

# 또한 이또한 마찮가지로 만약에 함수안에 지역변수로서 이 전역변수와 동일한 이름에 하나의 리스트가 선언이된다면 이 함수 안에서는 이 지역변수가 우선적으로 참조가됨


array = [1, 2, 3, 4, 5]


def func():
    array = [3, 4, 5]
    array.append(6)
    print(array)


func()


def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var


a, b, c, d = operator(7, 3)
print(a, b, c, d)

# 이렇게 여러개의 변수가 한꺼번에 반환되는 것을 엄밀히는 패킹이라고 말함
# 이제 이렇게 함수를 호출하는 측면에서 그 반환된 값들을 차례대로 특정 번수에 담는것을
# 언패킹이라고 말함


print("람다 표현식")
# 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있습니다.
# · 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징입니다.
#  https://wikidocs.net/64  참고


def add(a, b):
    return a + b


# 일반적인 add() 메서드 사용
print(add(3, 7))
# 람다 표현식으로 구현한 add() 메서드

print((lambda a, b: a + b)(3, 7))


# 람다 표현식 예시: 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

# sorted 함수 설명 https://blockdmask.tistory.com/466


print("람다 표현식 예시: 여러 개의 리스트에 적용")
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
# map함수는 함수와 리스트를 인자로 받습니다. 그렇죠? 그리고, 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담아준답니다
result = map(lambda a, b: a + b, list1, list2)
print(list(result))

# 일반적으로는 이렇게 쓰는게 맞음
# print()
# print((lambda a, b: a + b)(3, 7))
