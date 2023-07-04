# 1
N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

for num in arr:
    lt, rt = 0, N - 1
    isExist = False

    while lt <= rt:
        mid = (lt + rt) // 2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    if not isExist:
        print(0)

# 2

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
