a, b = map(int, input().split())

num = list(map(int, input().split()))
for i in num:
    print(i - (a * b), end=' ')
