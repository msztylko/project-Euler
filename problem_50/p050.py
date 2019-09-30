def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

primes = []
for i in range(1, 1000):
    if is_prime(i):
        primes.append(i)

i = 4
sum = 0
while i < 25:
    sum += primes[i]
    i += 1
    print(i, sum)


sums = []
for i in range()




