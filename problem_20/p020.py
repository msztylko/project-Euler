def solution(n):
    return sum(int(i) for i in str(n))


def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial


if __name__ == "__main__":
    print(
        "The sum of the digits in the number 100! is equal {}".format(
            solution(factorial(100))
        )
    )
