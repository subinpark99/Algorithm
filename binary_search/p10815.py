import sys

input = sys.stdin.readline
n = int(input())
nlst = set(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))

rst = 0
for i in mlst:
    if i in nlst:
        rst = 1
    else:
        rst = 0
    print(rst, end=' ')
