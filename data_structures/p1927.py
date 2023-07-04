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
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, x)
