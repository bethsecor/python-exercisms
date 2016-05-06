def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    letter_count = 0
    for letter in alphabet:
        if letter in string: letter_count += 1
    return letter_count == 26
