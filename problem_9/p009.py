def solution():
    LIMIT = 1000
    for a in range(1, LIMIT + 1):
        for b in range(a + 1, LIMIT + 1):
            c = LIMIT - a - b
            if a * a + b * b == c * c:
                return a * b * c


if __name__ == "__main__":
	print(solution())