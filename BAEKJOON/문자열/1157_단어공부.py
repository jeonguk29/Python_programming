# 내코드는 중복 값을 어떻게 계산할지 모르겠음 

n = input()
str1 = n.lower()
count1 = [0] * 26


alphabet = list(range(97,123))  # 아스키코드 소문자 범위
for x in alphabet :
    for i in str1:
        if i == chr(x):
            count1[x-97] = count1[x-97] + 1
            
if count1.count(max(count1)) >= 2: # 가장 큰값의 개수가 2개 즉 중복이라면 ? 출력
    print("?")
else:
    print(chr(count1.index(max(count1))+65))  #가장 큰 값을 가진 인덱스의 값에 +65 더하고 문자로 출력하면 대문자로 가장 많이 나온 값 출력됨 

