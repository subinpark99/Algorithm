from collections import deque
import sys

deq = deque()

for i in range(int(sys.stdin.readline())):
    m = sys.stdin.readline().strip()

    if 'push_back' in m:
        deq.append(m.split(' ')[1])

    elif 'push_front' in m:
        deq.appendleft(m.split(' ')[1])

    elif 'pop_front' in m:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())


    elif 'pop_back' in m:
        if len(deq) == 0:
            print(-1)
        else:

            print(deq.pop())

    elif 'front' in m:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])

    elif 'back' in m:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])

    elif 'empty' in m:
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif 'size' in m:
        print(len(deq))
