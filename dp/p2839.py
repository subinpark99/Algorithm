n = int(input())

rst = 0

while n >= 0:
    if n % 5 == 0:
        rst += n // 5
        print(rst)
        break
    n -= 3
    rst += 1
else:
    print(-1)
