def isPrime(n):
    if n < 2:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

#Poprawić te funkcje bo na pewno nie działają z czymś co ma zera
def isTruncableLeft(n):
    if isPrime(n):
        n = str(n)
        for i in range(len(n) - 1):
            n = n[1:]
            if isPrime(int(n)):
                continue
            else:
                return False

        return True


def isTruncableLeft(n):
    if isPrime(n):
        n = str(n)
        for i in range(len(n) - 1):
            n = n[1:]
            if isPrime(int(n)):
                continue
            else:
                return False

        return True


def main():
    return sum([i for i in range(11, 1000000, 2) if isPrime(i) and isTruncablePrime(i)])

# if __name__ == "__main__":
#     print(main())

print(isTruncableLeft(3797))