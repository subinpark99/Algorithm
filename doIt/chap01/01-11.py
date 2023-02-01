# +와 - 번갈아 출력

n = int(input('몇 개 출력? '))

for i in range(n):
    if i % 2:  # 홀수
        print('-', end=' ')
    else:      # 짝수
        print('+', end=' ')
print()
