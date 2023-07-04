# 에라토스테네스의 체
n = 1000000 * 2
arr = [False, False] + [True] * (n + 1)

for i in range(2, int(n ** 0.5) + 1):
    if arr[i]:
        for j in range(2 * i, n + 1, i):
            arr[j] = False

for _ in range(int(input())):
    m = int(input())

    cnt = 0

    for i in range(2, m // 2 + 1):
        if arr[i] and arr[m - i]:
            cnt += 1

    print(cnt)
