def is_pandigital(n):


def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False


def main():
    maxnum = 0
    for i in range(3, 10000000000, 2):
        if isPrime(n) and isPandigital(n) and n > maxnum:
            maxnum = i

    return maxnum


if __name__ == "__main__":
    print("The largest n-digit pandigital prime is {}".format(main()))