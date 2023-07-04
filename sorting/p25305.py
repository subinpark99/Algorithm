n, m = map(int, input().split())

s = list(map(int, input().split()))
r = sorted(s, reverse=True)
print(r[m - 1])
