# 1부터 n까지 정수 합

def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s


x = int(input('x값 입력: '))
print(f'1부터 {x}까지 정수 합은 {sum_1ton(x)}임')
