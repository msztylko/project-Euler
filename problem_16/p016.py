def sum_digits(number):
    string = str(number)
    sum = 0
    for i in string:
        sum += int(i)

    return sum


if __name__ == "__main__":
    print("The sum of the digits of the number 2^1000 is equal {}".format(sum_digits(2**1000)))
