import re

def word_hist(string):
    dictionary = {}
    string = string.strip().lower()
    words = re.findall(r'\b[-a-z\']+\b',string)
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary

if __name__ == "__main__":

    user_input = input("Enter a phrase: ")

    word_counts = word_hist(user_input)

    print(word_counts)

    word_list = []
    for word in word_counts:
        word_list.append((word,word_counts[word]))
    word_list.sort(key=lambda item: item[1],reverse=True)

    top_message = f"Top words:"
    for i in range(3):
        try:
            top_message += f'\n{i + 1}: {word_list[i]}'
        except IndexError:
            break
