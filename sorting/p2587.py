ans = []
for i in range(5):
    ans.append(int(input()))
mid = sorted(ans)
print(sum(ans) // len(ans), mid[len(ans) // 2], sep='\n')
