def fibonacci(i):
    if i <= 1:
        return i
    else:
        return fibonacci(i-1) + fibonacci(i-2)


i = int(input())
print(fibonacci(i))
