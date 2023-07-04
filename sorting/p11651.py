import sys

answer = []
for i in range(int(sys.stdin.readline())):
    n = list(map(int, sys.stdin.readline().split()))
    answer.append(n)
answer.sort(key=lambda x: (x[1], x[0]))

for i in answer:
    print(i[0], i[1])
