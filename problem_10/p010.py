def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def solution():
    return sum(i for i in range(2, 2000001) if is_prime(i))


if __name__ == "__main__":
    #    import cProfile
    print("The sum of all the primes below two million is equal {}".format(solution()))
#    cProfile.run('solution()', sort='cumtime')
