import cProfile
import math

#Initial code was super slow, so I used C Profiler to find out that the problems were caused by num_divisors function.
#The function was implemented with new logic and works much faster now.

def triangle_number(n):
    return sum(i for i in range(1, n + 1))

# #Initial num_divisors function
# def num_divisors(n):
#     counter = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             counter += 1
#
#     return counter
# #    return len([i for i in range(1, n + 1) if n % i == 0]) #A bit slower than the version below

def num_divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n / i])
    divs.extend([n])
    return len(set(divs))


def solution():
    i = 1
    while num_divisors(triangle_number(i)) < 500:
        i += 1
    return triangle_number(i)


if __name__ == "__main__":
    print("The value of the first triangle number to have over five hundred divisors is {}".format(solution()))
    cProfile.run('solution()', sort='cumtime')