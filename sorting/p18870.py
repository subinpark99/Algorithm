import sys

n = int(sys.stdin.readline())

m = list(map(int, sys.stdin.readline().split()))
s = sorted(set(m))
dic = {s[i]: i for i in range(len(s))}

for i in m:
    print(dic[i], end=' ')
   