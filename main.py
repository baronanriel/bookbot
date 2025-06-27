import os

def get_book_text(path_to_file):
    #print("Getting book text!")
    with open(path_to_file) as f:
        file_contents = f.read()
        return(file_contents)

def get_word_count(file_contents):
    return(len(file_contents.split()))

#print("Starting Test!")
frankenstein_path = os.getcwd() + "/books/frankenstein.txt"
file_contents = get_book_text(frankenstein_path)
word_count = get_word_count(file_contents)
print(word_count, "words found in the document")