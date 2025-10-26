def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import total_words

def main():
    filepath = "books/frankenstein.txt"
    file_contents = get_book_text(filepath)
    print(f"Found {total_words(file_contents)} total words")



main()