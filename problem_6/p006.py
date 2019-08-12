def solution():
    return sum(x for x in range(1, 101))**2 - sum(x**2 for x in range(1, 101))

if __name__ == "__main__":
    print("The difference between the sum of the squares of the first one hundred natural "
          "numbers and the square of the sum is equal {}".format(solution()))