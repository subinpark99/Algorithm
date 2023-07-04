n = int(input())
lst = [0] * 301
for i in range(n):
    lst[i] = int(input())

d = [0] * 300

d[0] = lst[0]
d[1] = lst[1] + lst[0]
d[2] = max(lst[0] + lst[2], lst[1] + lst[2])

for i in range(3, n):
    d[i] = max(d[i - 3] + lst[i - 1] + lst[i], d[i - 2] + lst[i])

print(d[n - 1])
