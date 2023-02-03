# 시퀀스 원소의 최댓값 출력

from typing import Any, Sequence


def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == '__main__':  # 스크립트 프로그램이 직접 실행될 때 변수 __name__은 __main__임, 다른 모튤에서 import 될 때 실행되지 않음
    num = int(input('원소 수 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요: '))

    print(f'최댓값은 {max_of(x)}임')
