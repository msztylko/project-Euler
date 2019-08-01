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

sum = 0
for i in range(3, 1000000):
     if equalFactorial(i) == True:
        sum += i

print(sum)