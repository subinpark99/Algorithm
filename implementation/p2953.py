p = []
winner = 0
for i in range(5):
    n = list(map(int, input().split()))
    p.append(sum(n))
print(p.index(max(p)) + 1, max(p))
