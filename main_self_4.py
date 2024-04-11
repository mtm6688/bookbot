def main():
    test = {'p': 6121, 'r': 20818, 'o': 25225, 'j': 504, "0" : 101}
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    lower_case = get_char_count(text)
    sorted_list = sorted_report(lower_case)

    print(f"--- This is the report for the document located in {book_path} ---")
    print(f"There are {word_count} words in the document.")
    print("")
    for character in sorted_list:
        print(f"The {character['char']} character appears {character['count']} times")
    print("--- End of report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lower = text.lower()
    char_count = {}
    for char in lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_list(dict):
    return dict['count']
    
def sorted_report(dict):
    sorted = []
    for character in dict:
        new_dict = {}
        if character.isalpha():
            new_dict = {'char': character, 'count': dict[character]}
            sorted.append(new_dict)
            sorted.sort(reverse=True, key=sort_list)
    return sorted


#        if character.isalpha():
#            new_dict[character] = dict[character]
#            sorted.append(new_dict)
#            sorted.sort(reverse=True, key=sort_list)
#    return sorted
    
#def print_char_report(my_list):
#    for i in range(0, len(my_list)):
#        new_dict = my_list[i]
#        for char in new_dict:
#            count = new_dict[char]
        
    
main()