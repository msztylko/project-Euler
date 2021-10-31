def solution() -> int:
    return sum(i for i in range(1000) if (i % 3 == 0 or i % 5 == 0))


if __name__ == "__main__":
    print(
        "The sum of all the multiples of 3 or 5 below 1000 is equal to {}".format(
            solution()
        )
    )
