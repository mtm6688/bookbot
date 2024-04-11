def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    lower_case = get_char_count(text)
    print(f"There are {word_count} words in the document.")
    print(lower_case)
    
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



main()