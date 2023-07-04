coin = 1000 - int(input())

cnt = 0

charge = [500, 100, 50, 10, 5, 1]
for i in charge:
    cnt += coin // i
    coin %= i
print(cnt)
