def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


prime_list = []
for i in range(1000, 9999):
    if is_prime(i):
        prime_list.append(i)


permutations = []
for i in prime_list:
    for j in prime_list:
        if sorted(str(i)) == sorted(str(j)):
            permutations.append(i)


solution = []
for i in permutations:
    for j in permutations:
        for k in permutations:
            if abs(i - j) == abs(j - k) == abs(k - i):
                solution.append(i)

    if len(solution) % 2 == 0:
        print(solution)



