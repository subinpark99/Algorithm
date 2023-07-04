m = []
for i in range(1, 10):
    n = int(input())
    m.append(n)

print(max(m))
print(m.index(max(m)) + 1)
