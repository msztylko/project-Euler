# This should work but I don't understand why it takes forever to compute it

# def fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# i = 1
# while len(str(fibonacci(i))) != 1000:
#     i += 1
# print(i, fibonacci(i))


# While this computes the solution in no time
a = 1
b = 0
n = 1
while len(str(a)) != 1000:
    a, b = a + b, a
    n = n + 1
print("%d has 1000 digits, n = %d" % (a, n))
