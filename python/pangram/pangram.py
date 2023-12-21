def is_pangram(sentence):
    return len([letter for letter in set(sentence.lower()) if letter.isalpha()]) == 26