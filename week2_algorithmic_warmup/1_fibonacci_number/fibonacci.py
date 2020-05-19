# Uses python3
import time


def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


if __name__ == '__main__':
    n = int(input())
    a = time.time()
    print(calc_fib(n))
    b = time.time()
    print('Time taken:', (b-a))
