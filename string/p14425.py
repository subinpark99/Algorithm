n, m = map(int, input().split())
a, b, rst = [], [], 0

for i in range(n):
    a.append(input())

for i in range(m):
    b.append(input())

for i in b:
    if i in a:
        rst += 1

print(rst)
