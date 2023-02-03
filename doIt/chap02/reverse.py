# mutable 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence


def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


if __name__ == '__main__':
    nx = int(input('원소 수 입력: '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값 입력: '))

    reverse_array(x)

    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
