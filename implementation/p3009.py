a, b = [], []
c, d = 0, 0
for i in range(3):
    n, m = map(int, input().split())
    a.append(n)
    b.append(m)

for i in range(3):
    if a.count(a[i]) == 1:
        c = a[i]
    if b.count(b[i]) == 1:
        d = b[i]
print(c, d)
