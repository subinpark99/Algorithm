stack, rst = [], []
cnt = 1

for i in range(int(input())):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        rst.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        rst.append('-')

if len(stack) != 0:
    print('NO')

else:
    for i in rst:
        print(i)
