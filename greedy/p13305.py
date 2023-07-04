n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

first = road[0] * cost[0]
mim = cost[0]

for i in range(1, n - 1):
    if mim > cost[i]:
        mim = cost[i]
    first += mim * road[i]

print(first)
