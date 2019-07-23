with open('p022_names.txt') as f:
    data = f.readline()
    data = data.split(',')
    eddited = []
    for i in data:
        edited = i.strip('"')
        eddited.append(edited)

score = []
for (i, name) in enumerate(sorted(eddited)):
    nameScore = 0
    for letter in name:
        letterScore = ord(letter) - ord('A') + 1
        nameScore += letterScore
    nameScore *= (i + 1)
    score.append(nameScore)

print(sum(score))

