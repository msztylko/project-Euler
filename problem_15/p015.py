# I cannot work out reasonable brute-force solution, so I started looking for some specific algorithms for this problem
# and it turns out that the number of paths from (0, 0) to (n, k) is simply binomial coefficient n+k over n.
# https://en.wikipedia.org/wiki/Lattice_path

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial

solution = factorial(40)/(factorial(20)**2)
print(solution)