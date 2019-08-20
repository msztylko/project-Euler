def factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    return factorial


def equalFactorial(n):
    n = str(n)
    sum = 0
    for digit in n:
        sum += factorial(int(digit))
    if sum == int(n):

        return True

def solution():
    sum = 0
    for i in range(3, 1000000):
        if equalFactorial(i) == True:
            sum += i

    return sum

if __name__ == "__main__":
    print("The sum of all numbers which are equal to the sum of "
          "the factorial of their digits is equal {}". format(solution()))