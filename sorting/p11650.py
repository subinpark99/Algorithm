import sys

rst = []
for i in range(int(sys.stdin.readline())):
    n = list(map(int, sys.stdin.readline().split()))
    rst.append(n)

answer = sorted(rst, key=lambda x: (x[0], x[1]))
for i in answer:
    print(i[0], i[1])
