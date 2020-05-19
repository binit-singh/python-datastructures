# Uses python3
import time


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    if b == 0:
        return a
    a_remainder = a % b
    return gcd_fast(b, a_remainder)


if __name__ == "__main__":
    a, b = map(int, input().split())
    # First algo
    tic = time.time()
    print(gcd_naive(a, b))
    toc = time.time()
    print('Time taken:', (toc-tic))

    # Second algo
    tic = time.time()
    print(gcd_fast(a, b))
    toc = time.time()
    print('Time taken fast:', (toc-tic))