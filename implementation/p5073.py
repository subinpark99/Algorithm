while True:
    a, b, c = map(int, input().split())
    lst = sorted([a, b, c])

    if a == b == c == 0:
        break

    if sum(lst[0:2]) <= lst[2]:
        print('Invalid')
    else:
        if a == b == c:
            print('Equilateral')
        elif a == b or b == c or a == c:
            print('Isosceles')
        elif a != b != c:
            print('Scalene')
