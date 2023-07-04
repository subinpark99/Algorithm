# 1

n = int(input())
ip = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if ip[i] > ip[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 2

n = int(input())
ip = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if ip[i] > ip[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
