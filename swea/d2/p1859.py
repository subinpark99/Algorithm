T = int(input())

for i in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))

    maxi = N_list[-1]
    profit = 0

    for j in range(N - 2, -1, -1):
        if N_list[j] >= maxi:
            maxi = N_list[j]
        else:
            profit += maxi - N_list[j]
    print("#{} {}".format(i, profit))
