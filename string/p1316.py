ins = int(input())
cnt = ins
for i in range(ins):
    n = input()
    for j in range(0, len(n) - 1):
        if n[j] == n[j + 1]:
            pass
        elif n[j] in n[j + 1:]:
            cnt -= 1
            break
print(cnt)
