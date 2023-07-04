n = int(input())
lst, cnt, last = [], 0, 0

for i in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))

x = sorted(lst, key=lambda y: (x[1], x[0]))

for start, end in x:
    if start >= last:
        cnt += 1
        last = end
print(cnt)
