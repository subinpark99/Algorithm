import sys

a = int(sys.stdin.readline())
b = set(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
y = list(map(int, sys.stdin.readline().split()))

for i in y:
    if i in b:
        print(1)
    else:
        print(0)
