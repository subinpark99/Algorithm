cnt = []
for i in range(10):
    n = int(input())
    cnt.append(n % 42)

print(len(set(cnt)))
