def solution():
    sum = 0
    for number in range(2, 1000001):
        number = str(number)
        digit_sum = 0
        for digit in number:
            digit_sum += int(digit)**5
        if digit_sum == int(number):
            sum += int(number)

    return sum

if __name__ == "__main__":
    print("The sum of all the numbers that can be written "
          "as the sum of fifth powers of their digits is equal {}".format(solution()))