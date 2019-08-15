def Collatz_len(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
          n = n/2
          counter += 1
        else:
            n = 3*n +1
            counter += 1

    return counter


def solution():
    longest = 0
    number = 0
    for i in range(1000001):
        if Collatz_len(i) > longest:
            longest = Collatz_len(i)
            number = i

    return number

if __name__ == "__main__":
    print("The longest Collatz sequence is produced by number {}".format((solution())))

