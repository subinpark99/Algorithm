from collections import deque

for i in range(int(input())):
    n, m = map(int, input().split())

    queue = deque(map(int, input().split()))
    lst = deque([i for i in range(n)])
    cnt = 0

    while queue:
        if queue[0] == max(queue):
            cnt += 1
            queue.popleft()
            if lst.popleft() == m:
                print(cnt)

        else:
            queue.append(queue.popleft())
            lst.append(lst.popleft())
