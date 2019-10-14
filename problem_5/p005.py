def evenly_divisible(n):
    for i in range(1, 21):
        if n % i == 0:
            continue
        else:
            return False

    return True


def solution():
    n = 20
    while not evenly_divisible(n):
        n += 20

    return n


if __name__ == "__main__":
#    import cProfile
    print("The smallest positive number that is evenly divisible "
          "by all of the numbers from 1 to 20 is {}".format(solution()))
#    cProfile.run('solution()', sort='cumtime')




