input_names = open('p022_names.txt', 'r')
names = input_names.read().split(",")
input_names.close()

for index in range(len(names)):
    names[index] = names[index][1:-1]

names = sorted(names)

def alphabet_score(word):
    name = list(word)
    total = 0
    for letter in name:
        score = ord(letter) - 64
        total += score

    return total

names_score_total = 0

for position, name in enumerate(names, 1):
    name_score = position * alphabet_score(name)
    names_score_total += name_score

print(names_score_total)
