import math


def solution(N=1000):
    counter = 0
    n = d = 1
    for k in range(N):
        n, d = 2 * d + n, d + n
        if int(math.log10(n)) > int(math.log10(d)):
            counter += 1
    return counter


if __name__ == "__main__":
    print(
        f"Number of fractions that contain a numerator with more digits than the denominator {solution()}"
    )
