def count_words(text):
    words = text.split()
    return len(words)

def times_count(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(d):
    return d["num"]

def sort_character_counts(char_counts):
    sorted_list = []
    for char in char_counts:
        sorted_list.append({"char": char, "num": char_counts[char]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
