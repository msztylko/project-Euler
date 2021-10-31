def isPandigital(n):
    compare = []
    for i in range(1, len(str(n)) + 1):
        compare.append(str(i))
    if sorted(str(n)) == compare:
        return True


def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def main():
    maxnum = 0
    for i in range(
        3, 7654321, 2
    ):  # 7654321 is the largest possible solution, 8- and 9-digit pandigital numbers are divisible by 3
        if isPrime(i) and isPandigital(i) and i > maxnum:
            maxnum = i

    return maxnum


if __name__ == "__main__":
    print("The largest n-digit pandigital prime is {}".format(main()))
