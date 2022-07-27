import sys         
a, b = map(int, input().split())

data = list(map(int, input().split()))      # a 길이를 넘어으면 리스트에서 삭제 
if len(data) > a:
    for _ in range(len(data) - a):
        data.pop()

data2 = []

for i in range(len(data)):
    if(data[i] < b):       
        data2.append(data[i])

for i in data2:
    print(i,'',end='')    # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨)


