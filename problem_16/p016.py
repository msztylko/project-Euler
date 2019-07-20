def sumDigits(number):
    string = str(number)
    sum = 0
    for i in string:
        sum += int(i)
    return print(sum)

sumDigits(2**1000)
git s