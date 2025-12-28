words = ("apple", "banana", "strawberry", "kiwi")

long_word = words[0]

for word in words:
    if word[1] > long_word[1]:
        long_word = word

print(long_word)        