def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    
    return word_count

def count_letters(text):
    letter_counts = {}
    
    lowercase_text = text.lower()
    
    for char in lowercase_text:
        if char in letter_counts and char.isalpha():
            letter_counts[char] += 1
        elif char.isalpha():
            letter_counts[char] = 1
        else:
            pass
    
    return letter_counts

def sort_list(dictionary):
    list_to_sort = list(dictionary.items())
    
    sorted_list = sorted(list_to_sort, key=lambda x:x[1], reverse=True)
    
    return sorted_list