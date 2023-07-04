n = int(input())
rst = n
cnt = 0

while True:

    f = rst // 10
    s = rst % 10
    summ = (f + s) % 10
    rst = (s * 10) + summ
    cnt += 1

    if n == rst:
        break

print(cnt)
