def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def nth_prime(n):
    index = 1
    number = 2
    while index != n:
        number += 1
        if is_prime(number):
            index += 1

    return number


if __name__ == "__main__":
#    import cProfile
    print("The 10 001st prime number is equal {}".format(nth_prime(10001)))
#   cProfile.run('nth_prime(10001)', sort='cumtime')
