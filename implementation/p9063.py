n = int(input())
x, y = [], []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

i = max(x) - min(x)
j = max(y) - min(y)

print(i * j)
