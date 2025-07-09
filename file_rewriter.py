def replace_all(f1, f2, word, replacement):
    file2 = []
    for words in open(f1).readlines():
        file2.append(words)
    for i in range(len(file2)):
        file2[i] = file2[i].replace(word, replacement)
    with open(f2, 'w') as f:
        f.write(' '.join(file2))

replace_all('file1.txt', 'file2.txt', 'photo', 'image')
