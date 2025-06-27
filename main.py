import os
import sys
from stats import get_word_count, get_char_count, compile_report, generate_report

def get_book_text(path_to_file):
    # print("Getting book text!")
    with open(path_to_file) as f:
        file_contents = f.read()
        return(file_contents)

try:
    frankenstein_path = os.getcwd() + '/' + sys.argv[1]
    file_contents = get_book_text(frankenstein_path)
    word_count = get_word_count(file_contents)
    book_title = sys.argv[1].split('/')[1]


    char_count = get_char_count(file_contents)
    report_data = compile_report(char_count)
    generate_report(word_count, report_data, book_title)

except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
