def triangleNumber(n):
    return sum ( [ i for i in range(1, n + 1) ] )

j = 0
n = 0
numberOfDivisors = 0

while numberOfDivisors <= 500:
    numberOfDivisors = 0
    j += 1
    n = triangleNumber(j)

    i = 1
    while i <= n**0.5:
        if n % i == 0:
            numberOfDivisors += 1
        i += 1

    numberOfDivisors *= 2

print ("Solution: ", n)
