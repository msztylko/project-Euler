def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True


def solution():
    return max(a * b for a in range(100, 1000) for b in range(100, 1000) if is_palindrome(a * b))


if __name__ == "__main__":
    print("The largest palindrome made from the product of two 3-digit numbers is {}".format(solution()))
