#!/opt/homebrew/bin/python3
# the above shebang means i can run this script (on my mac, anyway) by just typing `./main.py` in the terminal.

# python libraries
import sys
# project libraries
import stats
def get_book():
    """
    Reads the first argument and outputs it.

    :return: Content of second system argument.
    """
    try:
        return sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

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

def main():
    """
    Main function to execute the script.
    """
    path_to_book = get_book() 
    book_text = get_book_text(path_to_book)
    book_word_count = stats.get_book_word_count(book_text)
    book_character_count = stats.sort_character_count(stats.get_character_count(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for letter in book_character_count:
        print(f"{letter["letter"]}: {letter["num"]}")

main()