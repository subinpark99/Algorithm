# 1

n = int(input())
rst = 0
while True:
    if rst ** 2 <= n and (rst + 1) ** 2 > n:
        print(rst)
        break

    rst += 1

# 2

print(int((int(input()) ** 0.5)))
