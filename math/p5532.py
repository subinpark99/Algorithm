l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

i = b // d
if b % d != 0:
    i += 1
j = a // c
if a % c != 0:
    j += 1
print(l - max(i, j))
