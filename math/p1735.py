def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


a, b = map(int, input().split())
x, y = map(int, input().split())

rst = ((lcm(b, y) // b) * a) + ((lcm(b, y) // y) * x)

n = gcd(rst, lcm(b, y))

print(rst // n, lcm(b, y) // n, sep=' ')
