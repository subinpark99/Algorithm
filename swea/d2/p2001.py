T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]

    attach = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            pari = 0

            for a in range(m):
                for b in range(m):
                    pari += arr[i + a][j + b]
            attach.append(pari)

    print("#{} {}".format(tc, max(attach)))
