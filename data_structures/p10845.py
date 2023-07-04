import sys

lst = []
for i in range(int(sys.stdin.readline())):
    m = sys.stdin.readline().strip()

    if 'push' in m:
        lst.insert(0, m.split(' ')[1])


    elif 'pop' in m:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())


    elif 'front' in m:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])

    elif 'back' in m:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])

    elif 'empty' in m:
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    elif 'size' in m:
        print(len(lst))
