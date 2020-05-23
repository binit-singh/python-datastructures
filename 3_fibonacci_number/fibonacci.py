# Uses python3
import time


def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    arr = [0, 1]

    for i in range(2, n+1):
        num = arr[i-1] + arr[i-2]
        print(num)
        arr.append(arr[i-1] + arr[i-2])

    return arr[n]


if __name__ == '__main__':
    n = int(input())
    print(calc_fib_fast(n))
