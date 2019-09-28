<<<<<<< HEAD
def number_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return len(factors)


# iterator
j = 2*3*5*7


while True:
    if number_prime_factors(j) == 4:
        j += 1
        if number_prime_factors(j) == 4:
            j += 1
            if number_prime_factors(j) == 4:
                j += 1
                if number_prime_factors(j) == 4:
                    print(j-3)
                    break
    j += 1
||||||| merged common ancestors
=======
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
>>>>>>> ff7a7c1e3fca62c27a8c6920bdf761cfa92139ce
