import time

start = time.time()

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def solution():
    sum = 0
    i = 1
    while fibonacci(i) < 4e6:
        if fibonacci(i) % 2 == 0:
            sum += fibonacci(i)
            i += 1
        else:
            i += 1

    return sum


if __name__ == "__main__":
    print("the sum of the even-valued terms below 4 million in Fibonacci sequence is equal {}".format(solution()))\

end = time.time()

print("solution calculated in ", end - start, "seconds")
