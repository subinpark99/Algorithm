n, m = map(int, input().split())
coin, cnt = [], 0
for i in range(n):
    coin.append(int(input()))

for i in sorted(coin, reverse=True):
    cnt += m // i
    m %= i

print(cnt)
