import re

grid = []
with open("problem_11.txt", encoding="utf-16-be") as file:
    for line in file:
        if line[0].isdigit():
            line = re.sub(r"0([0-9])", r"\1", line).split()
            new_line = []
            for i in line:
                i = int(i)
                new_line.append(i)
            grid.append(new_line)

# Compute products from left to right
product1 = 0
for i in range(19):
    for j in range(17):
        product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        if product > product1:
            product1 = product
print("lef-right product", product1)

# Compute products from top to bottom
product2 = 0
for i in range(17):
    for j in range(20):
        product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
        if product > product2:
            product2 = product
print("up-down product", product2)

# Compute products from the first diagonal
product3 = 0
for i in range(17):
    for j in range(17):
        product = (
            grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        )
        if product > product3:
            product3 = product
print("first diagonal product", product3)

# Compute products from the second diagonal
product4 = 0
for i in range(19, 3, -1):
    for j in range(0, 17):
        product = (
            grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
        )
        if product > product4:
            product4 = product
print("second diagonal product", product4)

print("Solution", max(product1, product2, product3, product4))


# The same solution computed in a more compact and unfortunately more obscure way
def max_product1():
    return max(
        grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        for i in range(19)
        for j in range(17)
    )


def max_product2():
    return max(
        grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
        for i in range(17)
        for j in range(20)
    )


def max_product3():
    return max(
        grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        for i in range(17)
        for j in range(17)
    )


def max_product4():
    return max(
        grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
        for i in range(19, 3, -1)
        for j in range(17)
    )


print(
    "Solution ", max((max_product1(), max_product2(), max_product3(), max_product4()))
)
