n, m = map(int, input().split())
rst = [i for i in range(1, n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    rst[a - 1:b] = reversed(rst[a - 1:b])
print(*rst)
