n = int(input())
s = 2
cnt = 1
if n == 1:
    print(1)
else:
    while True:
        if s <= n < s + (6 * (cnt)):
            print(cnt + 1)
            break

        s += 6 * cnt
        cnt += 1
