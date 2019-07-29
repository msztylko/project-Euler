def solution():
    sum = 1
    for i in range(3, 1002, 2):
        sum += 4*i**2 - 6*i + 6

    print(sum)

solution()

