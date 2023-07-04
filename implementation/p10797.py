day = int(input())
num = map(int, input().split())
rst = 0

for i in num:
    if i == day:
        rst += 1

print(rst)
