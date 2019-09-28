#not the most efficient but good for now
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i==0:
            return False

    return True

def prime_factors(n):
    prime_list = []
    for i in range(1, int(n // 2 + 1), 2):
        if n % i ==0 and is_prime(i):
            prime_list.append(i)
    return set(prime_list)


def solution():
    for _ in range(1, 20):
        if prime_factors(_)