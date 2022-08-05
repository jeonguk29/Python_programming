'''
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=

문자를 변환하는 함수는 replace함수를 사용하였다. 이 함수를 for문 안에서 사용하며 주의했던 점은 문자를 변환하고서 저장하는 변수를 처음에 문자를 입력받을 때의 변수와 동일한 이름으로 지정한 것이다. replace함수는 함수를 사용한 문자열 원형을 변형시키지 않는 비파괴적 함수이기 때문이다. 이와 같은 사용 예시는 아래에서 설명한다.

'''

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수 i 와 같은게 있다면 *로 바꿔버림 
print(len(word))