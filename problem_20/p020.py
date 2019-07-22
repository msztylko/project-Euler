def sumDigits(n):
    solution = sum(int(i) for i in str(n))

    return solution

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial

print(sumDigits(factorial(100)))




