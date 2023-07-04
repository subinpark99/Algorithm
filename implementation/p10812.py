n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())

    basket[a - 1:b] = basket[c - 1:b] + basket[a - 1:c - 1]

print(' '.join(map(str, basket)))
