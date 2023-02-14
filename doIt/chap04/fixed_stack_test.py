# FixedStack 사용

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


s = FixedStack(64)  # 최대 64개 푸시 가능

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.푸시:
        x = int(input('데이터 입력: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득참')

    elif menu == Menu.팝:
        try:
            x = s.pop()
            print(f'팝 한 데이터는 {x}임')
        except FixedStack.Empty:
            print('스택이 비어 있음')

    elif menu == Menu.피크:
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}임')
        except FixedStack.Empty:
            print('스택이 비어 있음')

    elif menu == Menu.검색:
        x = int(input('검색할 값 입력: '))
        if x in s:
            print(f'{s.count(x)}개 포함됨, 맨 앞의 위치는 {s.find(x)}임')
        else:
            print('검색할 값을 찾을 수 없음')

    elif menu == Menu.덤프:
        s.dump()

    else:
        break
