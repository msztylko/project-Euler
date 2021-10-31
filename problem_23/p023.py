def abundantNumber(n):
    divisors = 0
    limit = int(n / 2 + 1)
    for i in range(1, limit):
        if n % i == 0:
            divisors += i
    if divisors > n:
        return True


limit = 28123
abundantList = []
for i in range(1, limit):
    if abundantNumber(i) == True:
        abundantList.append(i)

non_ab_sum = [x for x in range(28123)]

for i in range(len(abundantList)):
    for j in range(i, 28123):
        if abundantList[i] + abundantList[j] < 28123:
            non_ab_sum[abundantList[i] + abundantList[j]] = 0
        else:
            break

print(sum(non_ab_sum))
