# 비재귀적으로 재귀 함수 구현(꼬리 재귀 제거)

def recur(n: int) -> int:
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2


x = int(input('정수값 입력: '))

recur(x)
