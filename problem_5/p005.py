# rangemax = 20
# def div_check(n):
#     for i in range(11,rangemax+1):
#         if n % i == 0:
#             continue
#         else:
#             return False
#     return True
#
# if __name__ == '__main__':
#    num = 2
#    while not div_check(num):
# #       print(num)
#        num += 2
#    print(num)

def evenly_divisible(n, limit):
    for i in range(1, limit + 1):
        if n % i == 0:
            continue
        else:
            return False

    return True

def solution():
    n = 1
    while not evenly_divisible(n, 20):
        n += 1

    return n

if __name__ == "__main__":
    print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}".format(solution()))
