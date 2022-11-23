N = int(input())

for i in range(1, N + 1):
    i = str(i)
    clap = ''
    if i.count('3') or i.count('6') or i.count('9'):
        clap += '-'
        print(clap, end=" ")
    else:
        print(i, end=" ")
