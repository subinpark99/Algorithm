# 세 정수를 입력받아 중앙값 구하기 1

def med3(a, b, c):
    if a >= b:
        if b > c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


a = int(input('정수 a값: '))
b = int(input('정수 b값: '))
c = int(input('정수 c값: '))

print(f'중앙값은 {med3(a, b, c)}임')


# 중앙값 구하기 2

def medi3(a, b, c):
    if (b >= a >= c) or (b <= a <= c):
        return a
    elif (a > b > c) or (a < b < c):
        return b
    return c


a = int(input('정수 a값: '))
b = int(input('정수 b값: '))
c = int(input('정수 c값: '))

print(f'중앙값은 {medi3(a, b, c)}임')
