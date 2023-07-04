m = int(input())
n = int(input())

cc = [i ** 2 for i in range(1, 101)]
rst = []
for i in range(m, n + 1):
    for j in cc:
        if j == i:
            rst.append(i)

if len(rst) == 0:
    print(-1)

else:
    print(sum(rst))
    print(rst[0])
