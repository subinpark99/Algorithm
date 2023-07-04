n, m = map(int, input().split())
a, c = [], []
for i in range(n):
    a.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        w, b = 0, 0

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if a[k][l] != 'W':
                        w += 1
                    if a[k][l] != 'B':
                        b += 1
                else:
                    if a[k][l] != 'W':
                        b += 1
                    if a[k][l] != 'B':
                        w += 1
        c.append(w)
        c.append(b)

print(min(c))
