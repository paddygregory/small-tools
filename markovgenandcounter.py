fin = open('poem.txt')
file = fin.read()
filename = file.split()

#print(filename[1])
cleaned = []
for word in filename:
    word = word.strip('!.?,')
    word = word.lower()
    cleaned.append(word)

bigrams = {}
for i in range(len(cleaned) - 2):
    keys = (cleaned[i], cleaned[i+1])
    values = (cleaned[i+2])
    bigrams.setdefault(keys, []).append(values)

# print(bigrams)

# print(bigrams)
import random
import math


def generate_tex(num=5):
    current = list(random.choice(list(bigrams.keys())))
    result = current.copy()

    for i in range(num - 2):
        next_words = (result[-2], result[-1])
        if not next_words:
            break
        next_word = random.choice(bigrams.get(tuple(next_words), []))
        result.append(next_word)
    current = (result[-1], next_word)
    return ' '.join(result)

# print(generate_tex(50))