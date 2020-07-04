paragraph = 'Lorem ipsum state dolor sit amet tar  etats sed do eiusmod  rat tempor incididunt ut est laborum.'
list = paragraph.split();
anagram_list = []
print(list)

for word_1 in list:
    for word_2 in list:
        if word_1 != word_2 and (sorted(word_1)== sorted(word_2)):
            anagram_list.append(word_1)

print(anagram_list)

