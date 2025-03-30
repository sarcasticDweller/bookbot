#!/opt/homebrew/bin/python3
# the above shebang means i can run this script (on my mac, anyway) by just typing `./main.py` in the terminal.

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    :param file_path: Path to the book file.
    :return: Content of the book as a string.
    """
    contents = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
        file.close()
    return contents

def get_book_wordcount(book_text):
    """
    Counts the number of words in the book text.
    
    :param book_text: The text of the book.
    :return: Word count of the book text.
    """
    word_count = len(book_text.split())
    return word_count

def main():
    """
    Main function to execute the script.
    """
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    book_word_count = get_book_wordcount(book_text)
    print(f"{book_word_count} words found in the document")

main()