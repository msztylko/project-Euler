def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def choose_r_from_n(r, n):
    if r <= n:
        return factorial(n) / (factorial(r) * factorial(n - r))


def solution():
    counter = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if choose_r_from_n(r, n) > 1_000_000:
                counter += 1
    print(counter)


if __name__ == "__main__":
    solution()
