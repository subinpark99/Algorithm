T = int(input())

for i in range(1, T + 1):
    l = list(map(int, input().split()))
    print("#{} {}".format(i, max(l)))
