import itertools

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = list(itertools.permutations(numbers))
for (i, perm) in enumerate(permutations):
    if i == 999999:
        print('The the millionth lexicographic permutation of the digits {0} is'.format(numbers), perm)