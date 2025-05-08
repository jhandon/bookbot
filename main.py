import sys
from stats import count_words, times_count, sort_character_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    result = count_words(text)
    char_count = times_count(text)
    sort_character_list = sort_character_counts(char_count)
    print_report(file_path, result, sort_character_list)

def print_report(file_path, result, sort_character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {result} total words")
    print("--------- Character Count -------")
    for item in sort_character_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(file_path):
        with open(file_path) as f:
            return f.read()

main()
