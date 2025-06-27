import os
from stats import get_word_count, get_char_count, compile_report, generate_report

def get_book_text(path_to_file):
    #print("Getting book text!")
    with open(path_to_file) as f:
        file_contents = f.read()
        return(file_contents)

#print("Starting Test!")
frankenstein_path = os.getcwd() + "/books/frankenstein.txt"
file_contents = get_book_text(frankenstein_path)
word_count = get_word_count(file_contents)


char_count = get_char_count(file_contents)
report_data = compile_report(char_count)
generate_report(word_count, report_data)
