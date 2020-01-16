def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while (i * i) <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_list():
    prime_list = []
    for i in range(1_000_000):
        if is_prime(i):
            prime_list.append(i)

    return prime_list


def concat_prime(a, b):
    n1 = int(str(a) + str(b))
    n2 = int(str(b) + str(a))
    if is_prime(n1) and is_prime(n2):
        return True

print(concat_prime(3,))

def main():
    pass