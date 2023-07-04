x = [0, 1, 2, 3]
for i in range(int(input())):
    a, b = map(int, input().split())

    ai = x.index(a)
    bi = x.index(b)

    x[ai], x[bi] = x[bi], x[ai]
print(x[1])
