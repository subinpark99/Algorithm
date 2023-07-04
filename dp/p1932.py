n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

a, b = arr[0], arr[0]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif i == j:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

print(max(arr[-1]))
