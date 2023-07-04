n, m = map(int, input().split())
rst = [i for i in range(1, n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    rst[a - 1], rst[b - 1] = rst[b - 1], rst[a - 1]

print(*rst)
