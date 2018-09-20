import re

def letter_hist(string):
    dictionary = {}
    for char in string:
        char = char.lower()
        if re.match('[a-z]',char):
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
    return dictionary

if __name__ == "__main__":
    
    user_input = input("Please enter a word/phrase: ")

    print(letter_hist(user_input))