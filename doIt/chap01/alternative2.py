# +와 - 번갈아 출력 2

n = int(input('몇 개 출력? '))

for _ in range(n // 2):
    print('+ -', end=' ')

if n % 2:
    print('+', end=' ')  # n이 홀수일 때만 + 출력

print()
