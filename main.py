def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    letter_count = count_letters(text)
    letter_count_list = dict_conversion(letter_count)

    letter_count_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} were found in the document\n\n")

    for letter in letter_count_list:
        print(f"The {letter['letter']} character was found {letter['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    words = text.split()
    for word in words:
        for letter in word:
            if letter.isalpha():            
                if letter.lower() in letter_count:
                    letter_count[letter.lower()] += 1
                else:
                    letter_count[letter.lower()] = 1
    return letter_count

def dict_conversion(dictionary):
    dict_list = []
    for k in dictionary:
        dict_list.append({"letter": k, "num": dictionary[k]})
    return dict_list

main()
