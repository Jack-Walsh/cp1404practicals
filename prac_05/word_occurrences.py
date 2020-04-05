word_dict = {}

text = input("Sentence: ")
for word in text.split(" "):
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print("Text: {}".format(text))

word_max_length = max((len(word) for word in word_dict))
for words in word_dict:
    print("{:{}} : {}".format(words, word_max_length, word_dict[words]))
