from collections import deque

n, m = map(int, input().split())
k = deque(i for i in range(1, n + 1))
rst = []

while k:
    for i in range(m - 1):
        k.append(k.popleft())
    rst.append(str(k.popleft()))

print(f'<{", ".join(rst)}>')
