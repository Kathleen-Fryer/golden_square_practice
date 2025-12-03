# A function called count_words that takes a string as an argument 
# and returns the number of words in that string

def count_words(string):
    if string == "":
        return "Empty string, nothing to count"
    count = 0
    for word in string.split(" "):
        count += 1
    if count == 1:
        return f"This string contains {count} word"
    return f"This string contains {count} words"