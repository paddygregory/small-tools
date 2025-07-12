import random
from dataclasses import dataclass

# flashcard class
@dataclass
class FlashCard:
    question: str
    answer: str

# flashcard deck
fin = open('flashquiz-questions.txt')
filename = fin.read().split('\n')
deck = []
for line in filename:
    if '|' in line:
        q, a = line.strip().split('|')
        deck.append(FlashCard(q, a))

# quiz loop

correct = 0
incorrect = 0

while True:
    random.shuffle(deck)
    prompt1 = input(f"are you ready for the question?")
    card = random.choice(deck)
    print(f'the question is {card.question}')
    prompt2 = input('type your answer')
    if prompt2.lower().strip() in card.answer.lower().strip():
            correct += 1
            print('correct')
    else:
            incorrect += 1
            print(f'incorrect, the correct answer is {card.answer}')
    prompt1 = input(f"type 'q' to quit or 'n' to continue")
    if prompt1 == 'q':
        break

print(f'you got {correct} correct and {incorrect} incorrect')
