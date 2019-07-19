with open("problem_13.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        if line[0].isdigit():
            sum += int(line)

    print("The 10 first digits of this sum are", str(sum)[:10])
