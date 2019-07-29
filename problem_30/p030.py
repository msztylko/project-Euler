sum = 0
for number in range(2, 1000001):
    number = str(number)
    digit_sum = 0
    for digit in number:
        digit_sum += int(digit)**5
    if digit_sum == int(number):
        sum += int(number)

print(sum)