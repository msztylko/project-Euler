def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def rotate(s):
    return [s[n:] + s[:n] for n in range(1, len(s))]


primes = []
for i in range(2, 1000001):
    if is_prime(i) == True:
        i = str(i)
        primes.append(i)

n_circular_primes = sum(all(pr in primes for pr in rotate(p)) for p in primes)
print("Project Euler 35 Solution = {0}".format(n_circular_primes))
