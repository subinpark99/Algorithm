a, b, v = map(int, input().split())

rst = (v - b) / (a - b)

print(int(rst) if rst == int(rst) else int(rst) + 1)
