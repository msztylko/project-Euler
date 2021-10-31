# TO DO
# brute-force solution but it needs some work


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while (i * i) <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# def prime_list():
#     prime_list = []
#     for i in range(1_000_000):
#         if is_prime(i):
#             prime_list.append(i)
#
#     return prime_list

prime_list = []
for i in range(1_000):
    if is_prime(i):
        prime_list.append(i)


def concat_prime(a, b):
    n1 = int(str(a) + str(b))
    n2 = int(str(b) + str(a))
    if n1 == n2:
        if is_prime(n1):
            return True
        else:
            return False
    else:
        if is_prime(n1) and is_prime(n2):
            return True
        else:
            return False


def main():
    for i in range(len(prime_list)):
        for j in range(i, len(prime_list)):
            if concat_prime(prime_list[i], prime_list[j]):
                for k in range(j, len(prime_list)):
                    if concat_prime(prime_list[j], prime_list[k]):
                        for l in range(k, len(prime_list)):
                            if concat_prime(prime_list[k], prime_list[l]):
                                return prime_list[l]


if __name__ == "__main__":
    print(main())
