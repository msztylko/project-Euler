LIMIT = 10 ** 6

# generate primes
primes = []
sieve = list(range(LIMIT))
sieve[1] = 0
for n in sieve:
    if n:
        primes.append(n)
        for i in range(n * n, LIMIT, n):
            sieve[i] = 0

seen = set()
max_hits = 0

for p in primes:
    s = str(p)
    # must contain 0, 1 or 2 in the digits, but not the last one
    if set("012") & set(s[:-1]):
        sub_str, last = s[:-1], s[-1]
        for digit in "012":
            if digit in sub_str:
                hits = 0
                variations = []
                for replacement in "0123456789":
                    new = sub_str.replace(digit, replacement) + last
                    if new[0] != "0" and sieve[int(new)]:
                        hits += 1
                        variations.append(new)
                if hits > max_hits:
                    max_hits = hits
                    print(hits, "valid variations found for", p)
                    print(list(map(int, variations)))
