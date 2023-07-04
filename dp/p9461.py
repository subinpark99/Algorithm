dp = [0 for i in range(100)]
dp[0], dp[1], dp[2] = 1, 1, 1

for i in range(3, len(dp)):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(int(input())):
    n = int(input())
    print(dp[n - 1])
