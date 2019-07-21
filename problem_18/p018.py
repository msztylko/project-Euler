import re

def line2list():
    with open("problem_18.txt", "r") as f:
        lines = f.readlines()
        list = []
        for line in lines:
            if line[0].isdigit():
                line = re.sub(r'0([0-9])', r'\1', line)
                line = line.split()
                list.append(line)
    counter = 0
    for i in list:
        counter += 1
        for j in i:
            list[list.index(i)][i.index(j)] = int(j)
    print(counter)

    return list


#m is a number of rows
m = 15
triangle = line2list()
for i in range(m-2, -1, -1):
    for j in range(i+1):
        if (triangle[i+1][j] > triangle[i+1][j+1]):
            triangle[i][j] += triangle[i+1][j]
        else:
            triangle[i][j] += triangle[i+1][j+1]

print(triangle[0][0])
