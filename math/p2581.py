import math

n = int(input())
m = int(input())


def s(n):
    if n >= 2:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


answer = []

for i in range(n, m + 1):
    if s(i):
        answer.append(i)
if len(answer) == 0:
    print(-1)
else:
    print(sum(answer), answer[0], sep='\n')
