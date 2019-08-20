def binaryPalindromic(n):
    n = "{0:b}".format(n)
    if n == n[::-1]:
        return True
    else:
        return False


def decimalPalindromic(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False


def solution():
    return sum([i for i in range(1000000) if decimalPalindromic(i) and binaryPalindromic(i)])


if __name__ == "__main__":
    print("The sum of all numbers, less than one million, "
          "which are palindromic in base 10 and base 2 is equal {}".format(solution()))