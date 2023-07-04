# 1

n = 123456 * 2
array = [0, 0] + [1] * (n + 1)
primes = []
for i in range(2, int(n ** 0.5) + 1):
    if array[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            array[j] = 0

while True:
    m = int(input())

    if m == 0:
        break

    print(sum(array[m + 1:(2 * m) + 1]))

# 2

n = 123456 * 2 + 1
array = [False, False] + [True for _ in range(n)]

for i in range(2, int(n ** 0.5) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

while True:
    n = int(input())

    if n == 0:
        break

    cnt = 0

    for i in range(n + 1, 2 * n + 1):
        if array[i] == True:
            cnt += 1
    print(cnt)
