def word_counter(word):
    return len(word.split())

print(word_counter("Hello world")) # returns 2

print(word_counter("This is a sentence")) # returns 4

print(word_counter("")) # returns 0