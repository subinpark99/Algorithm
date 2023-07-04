# 1

from queue import PriorityQueue
import sys

n = int(sys.stdin.readline())

arr = PriorityQueue(maxsize=n)
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr.empty():
            print(0)
        else:
            print(arr.get()[1])
    else:
        arr.put((abs(x), x))

# 2

import sys
import heapq

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(x), x))
