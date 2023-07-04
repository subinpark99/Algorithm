from collections import deque

deque = deque(i for i in range(1, int(input()) + 1))

while len(deque) > 1:
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)

print(deque[0])
