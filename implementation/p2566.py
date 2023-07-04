maxi = []
for i in range(9):
    n = list(map(int, input().split()))
    maxi.append([max(n), n.index(max(n))])

print(max(maxi)[0])
print(maxi.index(max(maxi)) + 1, max(maxi)[1] + 1)
