n = int(input())
cnt = 0
strr = 666

while True:
    if '666' in str(strr):
        cnt += 1
    if cnt == n:
        print(strr)
        break

    strr += 1
