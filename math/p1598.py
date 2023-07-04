a, b = map(int, input().split())
b = b - 1
a = a - 1
x = (b // 4 + 1) - (a // 4 + 1)
y = (b % 4) - (a % 4)

print(abs(x) + abs(y))
