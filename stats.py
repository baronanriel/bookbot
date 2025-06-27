def get_word_count(file_contents):
    return(len(file_contents.split()))

def get_char_count(file_contents):
    char_dict = {}
    for char in file_contents.lower():
        if char in char_dict.keys():
            char_dict[char] += 1
            continue

        char_dict.update({char: 1})
    return(char_dict)

def sort_on(items):
    return(items["num"])

def compile_report(char_dict):
    report_data = []
    print("running report gen")
    for key in char_dict:
        report_data.append(
            {"char":key, "num":char_dict[key]}
        )
        
    report_data.sort(reverse=True, key=sort_on)
    return(report_data)

def generate_report(word_count, report_data):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for key in report_data:
        if key['char'].isalpha():
            print(f"{key['char']}: {key['num']}")
    print("============= END ===============")