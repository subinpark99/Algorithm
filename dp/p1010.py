# 1

def fac(a):
    if a >= 2:
        return a * fac(a - 1)
    else:
        return 1


for _ in range(int(input())):
    a, b = map(int, input().split())

    rst = fac(b) // (fac(b - a) * fac(a))
    print(rst)

# 2

d = [[1] * 31 for _ in range(31)]

for i in range(31):
    d[1][i] = i
for i in range(2, 31):
    for j in range(i + 1, 31):
        d[i][j] = d[i][j - 1] + d[i - 1][j - 1]

for i in range(int(input())):
    a, b = map(int, input().split())
    print(d[a][b])
