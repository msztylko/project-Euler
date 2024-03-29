import eulerlib, itertools, sys

if sys.version_info.major == 2:
    filterfalse = itertools.ifilterfalse
else:
    filterfalse = itertools.filterfalse


def solution():
    ans = next(filterfalse(test_goldbach, itertools.count(9, 2)))
    return str(ans)


def test_goldbach(n):
    if n % 2 == 0 or eulerlib.is_prime(n):
        return True
    for i in itertools.count(1):
        k = n - 2 * i * i
        if k <= 0:
            return False
        elif eulerlib.is_prime(k):
            return True


if __name__ == "__main__":
    print(solution())
