# *를 n개 출력하되 w개마다 줄바꿈

n = int(input('몇 개 출력? '))
w = int(input('몇 개마다 줄바꿈? '))

for i in range(n):
    print('*', end=' ')
    if i % w == w - 1:  # n번 판단
        print()

if n % w:  # 1번 판단
    print()
