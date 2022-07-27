arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)  # (set함수는 간단하게 말하면, 중복을 제거하기 위한 필터역할을 해준다.)
print(len(arr))