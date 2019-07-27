list = []
for a in range(2, 101):
    for b in range(2, 101):
        power = a**b
        list.append(power)

solution = len(set(list))
print(solution)