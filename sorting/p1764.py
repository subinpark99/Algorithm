# 1

import sys

n, m = map(int, sys.stdin.readline().split())
s = set([sys.stdin.readline().strip() for _ in range(n)]) & set([sys.stdin.readline().strip() for _ in range(m)])

print(len(s))
print('\n'.join(sorted(s)))

# 2

import sys

n, m = map(int, sys.stdin.readline().split())
answer = []
listen = [sys.stdin.readline() for _ in range(n)]
dic = {listen[i]: i for i in range(len(listen))}

for i in range(m):
    s = sys.stdin.readline()
    if s in dic:
        answer.append(s)

print(len(answer))
for i in sorted(answer):
    print(i, end='')
