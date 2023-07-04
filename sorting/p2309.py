n = []
rst = 0
x, y = 0, 0

for i in range(9):
    n.append(int(input()))

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == sum(n) - 100:
            x, y = n[i], n[j]

n.remove(x)
n.remove(y)
n.sort()
for i in n:
    print(i)
