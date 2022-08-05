def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i <= 1:
        return 1
    else:
        return i * recursive_function(i - 1) 
        #5 4 3 2 1


i = int(input())

print(recursive_function(i))
