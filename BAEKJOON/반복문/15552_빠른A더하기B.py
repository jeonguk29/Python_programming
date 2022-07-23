import sys    

n = int(input())
# split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.

for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)