# 1

x = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
y = input()
for i in x:
    y = y.replace(i, 'a')
print(len(y))

# 2

s = list(input())
cnt = 1
for i in range(1, len(s)):
    cnt += 1
    if s[i] == 'j':
        if s[i - 1] == 'l' or s[i - 1] == 'n':
            cnt -= 1

    elif s[i] == '-' or s[i] == '=':

        if s[i - 1] == 'z' and s[i - 2] == 'd':
            cnt -= 2
        else:
            cnt -= 1

print(cnt)
