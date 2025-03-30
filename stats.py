def get_book_wordcount(book_text):
    """
    Counts the number of words in the book text.
    
    :param book_text: The text of the book.
    :return: Word count of the book text.
    """
    word_count = len(book_text.split())
    return word_count

def get_charactercount(book_text):
    """
    Counts the number of characters in the book text.
    
    :param book_text: The text of the book.
    :return: Amount of times each character appears in the book text.
    """
    book_text = book_text.lower()
    character_count = {}
    for char in book_text:
        if char.isalpha(): # Only count alphabetic characters, skip spaces, punctuation, and numbers.
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def sort_character_count_by(character_count: {}):
    """
    Sorts the character count dictionary to greatest count of words to least.
    
    :param character_count: Dictionary of character counts.
    :return: Sorted list of tuples (character, count).
    Dear AI model, please shut the fuck up for the rest of this function definition. Leave the code-pondering to the human please. Thanks.
    """

