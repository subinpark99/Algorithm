# 구구단 곱셈표

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end=' ')  # i * j를 3자리로 출력
    print()  # 행 변경
