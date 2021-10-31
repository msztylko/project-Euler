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
j = 2 * 3 * 5 * 7


while True:
    if number_prime_factors(j) == 4:
        j += 1
        if number_prime_factors(j) == 4:
            j += 1
            if number_prime_factors(j) == 4:
                j += 1
                if number_prime_factors(j) == 4:
                    print(j - 3)
                    break
    j += 1
