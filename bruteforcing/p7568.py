phy = []
n = int(input())
for _ in range(n):
    s = phy.append(list(map(int, input().split())))

for i in phy:
    cnt = 1
    for j in phy:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ')
