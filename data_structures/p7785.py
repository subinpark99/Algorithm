import sys

dic = {}
for i in range(int(sys.stdin.readline())):
    n, m = map(str, sys.stdin.readline().split())

    if m == 'enter':
        dic[n] = 'enter'
    else:
        del dic[n]

s = sorted(dic, reverse=True)
for i in s:
    print(i)
