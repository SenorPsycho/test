# Find Longest Word
#    Write a function that takes a sentence and returns the longest word in it.
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

sentence = "The quick brown fox jumps over the lazy dog"
longest_word = find_longest_word(sentence)
