# 1

lst, d = [], []
n = int(input())
for _ in range(n):
    lst.append(int(input()))

for i in range(n - 1):
    d.append(lst[i + 1] - lst[i])


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


dis = gcd(d[0], d[1])

for i in range(1, n - 1):
    dis = gcd(dis, d[i])

print((lst[-1] - lst[0]) // dis + 1 - n)

# 2

import sys

input = sys.stdin.readline
lst, d = [], []
n = int(input())
for _ in range(n):
    lst.append(int(input()))

for i in range(n - 1):
    d.append(lst[i + 1] - lst[i])


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


dis = d[0]

for i in range(1, n - 1):
    dis = gcd(dis, d[i])

cnt = 0
for i in d:
    cnt += i // dis - 1

print(cnt)
