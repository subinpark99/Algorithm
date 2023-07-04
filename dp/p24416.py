n = int(input())

def fib(n):
    a, b = 1, 1

    for i in range(n - 2):
        a, b = b, a + b
    return b


def fibonacci(n):
    return n - 2


print(fib(n))
print(fibonacci(n))
