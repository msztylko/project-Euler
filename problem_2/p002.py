f_number1 = 1
f_number2 = 2
limit = 4000000
sum = 2
while f_number2 < limit:
    f_number1 = f_number1 + f_number2
    if f_number1 % 2 == 0:
        sum += f_number1
    f_number2 = f_number2 + f_number1
    if f_number2 % 2 == 0:
        sum += f_number2

print(sum)