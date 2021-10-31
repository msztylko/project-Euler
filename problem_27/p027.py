import itertools


def compute():
    ans = max(
        ((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
        key=count_consecutive_primes,
    )
    return str(ans[0] * ans[1])


def count_consecutive_primes(ab):
    a, b = ab
    for i in itertools.count():
        n = i * i + i * a + b
        if not isPrime2(n):
            return i


def isPrime2(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False

    return True


print(compute())
