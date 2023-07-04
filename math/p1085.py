x, y, w, h = map(int, input().split())

i = min(x - 0, w - x)
y = min(y - 0, h - y)
print(min(i, y))
