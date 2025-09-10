from stats import get_words_count, get_characters_count, sorted_chars
import sys

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    char_count = get_characters_count(get_book_text(book))
    # display a list of characters and their counts ordered by count descending
    # print("\n".join(sorted_chars(char_count)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words_count(get_book_text(book))} total words")
    print("--------- Character Count -------")
    print("\n".join(sorted_chars(char_count)))

main()