fin = open('poem.txt')
fat = fin.read()
filename = fat.split()

import random

cleaned = []
for word in filename:
    word = word.strip('.,!?()[]{}"\'')
    cleaned.append(word.lower())

# print(cleaned)
bigrams = {}
for i in range(len(cleaned) - 2):
    keys = (cleaned[i], cleaned[i + 1])
    values = (cleaned[i + 2])
    bigrams.setdefault(keys, []).append(values)

# print(bigrams)

def generate_text(num = 5):
    current = list(random.choice(list(bigrams.keys())))
    result = current.copy()

    for _ in range(num - 2):
        next_words = bigrams.get((current[-2], current[-1]), [])
        if not next_words:
            continue
        next_word = random.choice(next_words)
        result.append(next_word)
        current = [current[-1], next_word]

    return ' '.join(result)

print(generate_text(50))
