def get_book_wordcount(book_text):
    """
    Counts the number of words in the book text.
    
    :param book_text: The text of the book.
    :return: Word count of the book text.
    """
    word_count = len(book_text.split())
    return word_count