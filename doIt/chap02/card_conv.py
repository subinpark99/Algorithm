# 10진수를 입력받아 2~36진수로 변환하여 출력

def card_conv(x: int, r: int) -> str:  # 정숫값 x를 r진수로 변환

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'

    while x > 0:
        d += dchar[x % r]  # 해당 문자를 꺼내 결합
        x //= r

    return d[::-1]  # 역순으로 반환


if __name__ == '__main__':
    while True:
        while True:
            no = int(input('음이 아닌 정수 입력: '))
            if no > 0:
                break

        while True:
            cd = int(input('어떤 진수로 변환? '))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}임')

        retry = input('한 번 더 변환? (Y -> 예, N -> 아니오): ')
        if retry in {'N', 'n'}:
            break
