# 1

import math

n = int(input())
m = list(map(int, input().split()))
rst = 0


def isPrime(a):
    if a >= 2:
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True


for i in m:
    if isPrime(i):
        rst += 1
print(rst)

# 2

n = int(input())
m = list(map(int, input().split()))
rst = 0

for i in m:
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                rst += 1
            break

print(rst)
