# 왼쪽 아래가 직각인 삼각형으로 * 출력

n = int(input('짧은 변 길이 입력: '))

for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()
