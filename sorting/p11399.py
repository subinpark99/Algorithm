n = int(input())
p = list(map(int, input().split()))
answer = 0
p.sort()
for i in range(len(p)):
    answer += sum(p[:i + 1])

print(answer)
