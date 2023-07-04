n = int(input())
dp = [0] * 34534


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]

    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]


for i in range(n):
    x = int(input())
    if x == 0:
        print(1, 0)
    elif x == 1:
        print(0, 1)
    else:
        print(fibo(x - 1), fibo(x))
