def sumProperDivisors(n):
    divisors = 0
    limit = int(n/2 + 1)
    for i in range(1, limit):
        if n % i == 0:
            divisors += i

    return divisors


def amicablePair():
    amicablePair = {}
    for i in range(1, 10000):
        spdi = sumProperDivisors(i)  #moving spdi from inner loop to here helped to speed up the whole calculation
        for j in range(i + 1, 10000):   #we can start from i+1 to count only (i,j) pairs not (j,i) duplicates
            if spdi == j and sumProperDivisors(j) == i and j != i:
                amicablePair.update({i: j})

    return amicablePair


print("sum of all the amicable numbers under 10000 is equal ", sum(amicablePair().values()) + sum(amicablePair().keys()))