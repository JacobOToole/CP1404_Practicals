"""
CP1404 Practical
Word occurrences in a string using dictionary
Time estimation: 20 minutes
Actual time: 25m 24s
"""

longest_word_length = 0

text_string = input("Text: ")
words = text_string.split(" ")
words.sort()
string_count = {i: words.count(i) for i in words}

for word in words:
    if len(word) > longest_word_length:
        longest_word_length = len(word)

for i in string_count:
    print(f"{i:{longest_word_length}} : {string_count[i]}")

