def is_prime(n):
    if n < 2:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

primes = []
for i in range(2,2000001):
    if is_prime(i) == True:
        primes.append(i)

print(sum(primes))
