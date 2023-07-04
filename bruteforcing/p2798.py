from itertools import combinations

n, m = map(int, input().split())
s = list(map(int, input().split()))

rst = list(combinations(s, 3))
answer = []
for i in rst:
    if sum(i) > m:
        continue
    else:
        answer.append(sum(i))

print(max(answer))
