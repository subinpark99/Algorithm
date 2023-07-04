s = input().upper()
s_l = list(set(s))
l = []

for i in s_l:
    l.append(s.count(i))

if l.count(max(l)) >= 2:
    print('?')
else:
    print(s_l[l.index(max(l))])
