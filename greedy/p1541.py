n = input().split('-')
ans = []
for i in n:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    ans.append(cnt)

for i in range(1, len(ans)):
    ans[0] -= ans[i]

print(ans[0])
