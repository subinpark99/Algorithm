a = int(input())
b = list(map(int, input().split()))

y = 0
m = 0

for i in b:
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15

if y == m:
    print("Y M", m)
elif y > m:
    print("M", m)
else:
    print("Y", y)
