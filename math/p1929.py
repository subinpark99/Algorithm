import math

n, m = map(int, input().split())


def prime(a):
    if a >= 2:
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True


for i in range(n, m + 1):
    if prime(i):
        print(i)
