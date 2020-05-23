# Uses python3


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_fast(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def lcm_fast(a, b):
    # LCM * GCD = a * b

    lcm = (a *b)/gcd_fast(a, b)

    return int(lcm)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

