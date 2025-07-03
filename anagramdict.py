fin = open('wordd.txt')
fout = fin.read()
word_list = fout.split()

def anagram_dict(words):
    anagrams = {}
    for word in words:
        newword = ''.join(sorted(word))
        if newword not in anagrams:
            anagrams[newword] = [word]
        else:
            anagrams[newword].append(word)               # n.b. lists canot be keys as they are mutable 
    return list(anagrams.values())

t = ['cat', 'dog', 'tac', 'god', 'act', 'hello', 'world', 'doll', 'lold']        
# print(anagram_dict(t))

def large_anagrams(words):
    anagrams = anagram_dict(words)
    for group in anagrams:
        if len(group) > 5:
            print(group)

# print(large_anagrams(word_list))

