import inflect

def format(word):
    if '-' in word:
        word = word.replace('-', '')

    if ' ' in word:
        word = word.replace(' ', '')

    return word

total = 0

for number in range(1, 1001):
    word = inflect.engine()
    word = word.number_to_words(number)
    total += len(format(word))

print(total)

# is this cheating - googled and dowloaded the inflect package
# not actually sure what its doing with the engine??
