
def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letter_count_dict = character_counter(file_contents)
        letter_count_list = convert_dict_to_list(letter_count_dict)

    character_reporter(letter_count_list, word_counter(file_contents), f)    

def word_counter(book):
    words = []

    words = book.split()

    return len(words)

def character_counter(book):
    lower_case_book = book.lower()

    letter_count = {}

    for letter in lower_case_book:
        if not letter.isalpha():
            continue
        if letter not in letter_count:
           letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    return letter_count

def sort_on(dict):
    return dict[1]

def character_reporter(list, word_count, file):
    list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {file.name} ---")
    print(f"{word_count} words found in the document")
    print("")
    
    for i in range(0, len(list)):
        print(f"The '{list[i][0]}' character was found {list[i][1]} times")

    
def convert_dict_to_list(dict): 
    return list(dict.items())

    
main()

