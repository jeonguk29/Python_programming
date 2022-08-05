n = int(input())
count = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]

    for i in arr[1:]:
        if i > avg:
            count = count +1
    rate = count / arr[0] * 100
    print(f'{rate:.3f}%')
    avg = 0
    count = 0