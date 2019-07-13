sum1 = 0
sum2 = 0
for i in range(1, 101):
    sum1 = sum1 + i**2
    sum2 = sum2 + i
square = sum2**2
diff = square - sum1
print(diff)