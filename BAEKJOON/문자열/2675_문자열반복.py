'''
2
3 ABC
5 /HTP

'''

n = int(input())

for i in range(n):
    data = list(map(str, input().split()))
    for i in data[1]:
        print(i*int(data[0]),end='')
    print()