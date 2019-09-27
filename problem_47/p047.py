import math

def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def prime_factors(n):
    prime_factors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)

    return prime_factors


def solution():
    pass

print(prime_factors(98765))
