while True:
    try:      # 구분 오류가 없으면 계속 반복 
        a, b = map(int, input().split())
    except:   # 오류 나면 빠져나옴 
        break
    print(a+b) # 출력 