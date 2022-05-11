# 실수 재대로 떨어지지 않아서 round 함수로 반올림 필요

a = 0.3 + 0.6
print(round(a, 2))
if round(a, 2) == 0.9:
    print(True)
else:
    print(False)


# 참고로 나누기 수행시 실수형으로 나옴 주의
print(7/3)
