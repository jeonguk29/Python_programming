a,b = map(str,input().split())
c = []
d = []

for i in range(len(a), 0, -1):    # 10에서 1까지 역순으로 숫자 생성
    c.append(a[i-1])    # 역으로 리스트에 추가 

for i in range(len(a), 0, -1):    # 10에서 1까지 역순으로 숫자 생성
    d.append(b[i-1])


c = ''.join(c)  #역으로 숫자 된걸 다시 합치기
d = ''.join(d)
#print(c,d)


if int(c) > int(d):  # int형으로 형변환해서 비교후 출력 
    print(c)
else:
    print(d)

