'''  내코드 : 시간 초과 판정 
n = input()

ar = [-1] * 24

for i in range(len(n)):
    for j in range(97,123): # 글자 하나당 알파벳 소문자 다돌면서
        if(n[i] == chr(j)): # 같은게 있으면 
            ar[j-97] = n.index(n[i]) # ar 배열안에 넣게 

for i in ar:
    print(i,end=' ')
'''
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 


# find 함수를 이용해서 입력받은 문자열 안에 chr 함수로 변환된 문자가 있는지 찾는다. 만일 문자열이 있으면 찾는 문자가 첫 번째에 위치한 인덱스 숫자를 출력하고 없으면 -1을 출력하게 된다.

 