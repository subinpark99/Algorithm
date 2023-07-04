n = []
rst = 0

for i in range(4):
    a, b = map(int, input().split())
    rst = rst - a + b
    n.append(rst)
print(max(n))
