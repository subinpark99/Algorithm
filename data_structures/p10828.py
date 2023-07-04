import sys

lst = []

for i in range(int(sys.stdin.readline())):
    m = sys.stdin.readline().strip()

    if 'push' in m:
        lst.append(m.split(' ')[1])

    elif 'pop' in m:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())

    elif 'top' in m:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])

    elif 'empty' in m:
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    elif 'size' in m:
        print(len(lst))
