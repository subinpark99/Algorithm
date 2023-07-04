s = input()
rst = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        a = s[i:j + 1]
        rst.add(a)

print(len(rst))
