fin = open('poem.txt')
text = fin.read()
filename = text.split()
fin.close()
# print(filename)

cleaned = []
for word in filename:
    word = word.strip('.,!?()[]{}"\'')
    cleaned.append(word.lower())

# print(cleaned[0])

bigrams = {}
for i in range(len(cleaned) - 2):       # using len to access index
    keys = (cleaned[i], cleaned[i + 1])
    values = (cleaned[i + 2])
    bigrams.setdefault(keys, []).append(values)

# print(bigrams)

count_bigrams = {}
for key, value in bigrams.items():
    count_bigrams[key] = len(value)

# print(count_bigrams)
import random

def generate_text(num=5):
    current = list(random.choice(list(bigrams.keys())))
    results = current.copy()

    for i in range(num - 2):
        next_words = bigrams.get((current[-2], current[-1]), [])
        if not next_words:
            continue
        next_word = random.choice(next_words)
        results.append(next_word)
        current = [current[-1], next_word]
    return ' '.join(results)

# print(generate_text(10))

