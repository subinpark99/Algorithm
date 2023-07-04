n = int(input())
test = list(map(int, input().split()))
new = []

maxScore = max(test)
for i in test:
    new.append(i / maxScore * 100)
print(sum(new) / n)
