while True:
    n = input()
    a = []

    if n == '.':
        break

    for i in n:
        if i == '(' or i == '[':
            a.append(i)
        elif i == ')':
            if a and a[-1] == '(':
                a.pop()
            else:
                a.append(i)
                break

        elif i == ']':
            if a and a[-1] == '[':
                a.pop()
            else:
                a.append(i)
                break

    if len(a) == 0:
        print('yes')
    else:
        print('no')
