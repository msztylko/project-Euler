import math

for a in range(1, 400):
    for b in range(1, 400):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and  a + b + c == 1000:
           print(a, b, c, a*b*c)


#CORRECT

