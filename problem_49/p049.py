def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_perm(n, m):
    if sorted(str(n)) == sorted(str(m)):
        return True


primes =[]
for number in range(1000, 10000):
    if is_prime(number):
        primes.append(number)

for i in primes:
    for j in primes:
        if i == j:
            continue
        elif i < j:
            k = j + (j - i)
            if k < 10000 and is_prime(k):
                if is_perm(i, j) and is_perm(i, k):
                    solution = str(i) + str(j) + str(k)

print(solution)





