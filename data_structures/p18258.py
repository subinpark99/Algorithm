from collections import deque
import sys

que = deque([])
for _ in range(int(input())):
    n = sys.stdin.readline().split()

    if n[0] == 'push':
        que.append(n[1])

    elif n[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())

    elif n[0] == 'size':
        print(len(que))

    elif n[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)

    elif n[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])

    elif n[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
