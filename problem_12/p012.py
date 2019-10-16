import math

def triangle_number(n):
    return int(n*(n+1)/2)


def count_divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n / i])
    divs.extend([n])
    return len(set(divs))


def solution():
    i = 1
    while count_divisors(triangle_number(i)) < 500:
        i += 1
    return triangle_number(i)


if __name__ == "__main__":
#   import cProfile
   print("The value of the first triangle number to have over five hundred divisors is {}".format(solution()))
#   cProfile.run('solution()', sort='cumtime')
