def get_book_text(filepath):
    file = ""
    with open(filepath) as f:
        file = f.read()
    return file

def get_word_counts(text):
    split_text = text.split()
    numcount = 0
    for word in split_text:
        numcount += 1
    return numcount

def get_char_counts(text):
    charset = list(text.lower())
    counts = {}

    for character in charset:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
            
    return counts

def dict_sorter(dictionary):
    dictionary = dictionary
    dictionary = {key: value for key, value in dictionary.items() if key.isalpha()} #removes non-alphabetic characters

    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    string_dict = ", ".join(f"{key}: {value}" for key, value in sorted_dict.items())
    
    return string_dict