from collections import deque

a, b = map(int, input().split())
n = list(map(int, input().split()))

que = deque([i for i in range(1, a + 1)])
cnt = 0

for i in n:
    while True:
        if que[0] == i:
            que.popleft()
            break
        else:
            if que.index(i) <= len(que) // 2:
                que.rotate(-1)
                cnt += 1
            else:
                que.rotate(1)
                cnt += 1
print(cnt)
