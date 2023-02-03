# 1000 이하의 소수 나열 알고리즘 개선 1

cnt = 0
ptr = 0  # 이미 찾은 소수의 개수
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):  # 홀수만
    for i in range(1, ptr):
        cnt += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n  # 소수로 배열에 등록
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈 실행 횟수: {cnt}')
