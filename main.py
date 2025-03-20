from stats import get_book_text
from stats import get_word_counts
from stats import get_char_counts
from stats import dict_sorter
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    file_contents = get_book_text(filepath)
    numcount = get_word_counts(file_contents)
    charcount = get_char_counts(file_contents)
    sorted_counts = dict_sorter(charcount)

    print(f"Found {numcount} total words. {sorted_counts}")

if __name__ == "__main__":
    main()