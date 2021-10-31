def largest_prime_factor(n):
    i = 2
    while i ** 2 < n:
        while n % i == 0:
            n /= i
        i += 1

    return int(n)


if __name__ == "__main__":
    print(
        "The largest prime factor of the number 600851475143 is {}".format(
            largest_prime_factor(600851475143)
        )
    )
