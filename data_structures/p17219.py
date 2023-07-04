import sys

n, m = map(int, sys.stdin.readline().split())
dic = dict()

for i in range(n):
    web, pw = sys.stdin.readline().split()
    dic[web] = pw

for i in range(m):
    print(dic[sys.stdin.readline().rstrip()])
