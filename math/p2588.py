a = int(input())
b = input()
rst = []
cnt = 0
for i in reversed(b):
    n = a * int(i)
    print(n)
    rst.append(n * (10 ** cnt))
    cnt += 1
print(sum(rst))
