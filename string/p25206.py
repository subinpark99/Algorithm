score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
sumscore = 0
grade = 0
for i in range(20):
    a, b, c = map(str, input().split())

    if c == 'P':
        continue
    else:
        sumscore += float(b)
        grade += score[c] * float(b)

print(grade / sumscore)
