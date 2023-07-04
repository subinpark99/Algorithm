import sys

while True:
    up, low, num, emp = 0, 0, 0, 0
    sen = sys.stdin.readline().rstrip('\n')

    if not sen:
        break

    for i in sen:
        if i.isupper():
            up += 1
        if i.islower():
            low += 1
        if i.isdigit():
            num += 1
        if i == ' ':
            emp += 1

    print(low, up, num, emp, sep=' ')
