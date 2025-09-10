def get_words_count(text):
    words = text.split() #split text into words
    return len(words) #return the number of words

def get_characters_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sorted_chars(dict):
    # Convert the dictionary to a list and return it in format <char>: <num> ordered by num descending
    dict = [{"char": k, "num": v} for k, v in dict.items()]
    dict.sort(key=sort_on, reverse=True)
    return [f"{item['char']}: {item['num']}" for item in dict]