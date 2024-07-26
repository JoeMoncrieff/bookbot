def count_words(book):
    #Inefficient soln? (space)
    return(len(book.split(" ")))

def count_characters(book):
    #Data cleaning
    book = book.lower()
    output_dict = {}
    #analysis
    for c in book:
        output_dict[c] = output_dict.get(c,0) + 1
    return output_dict


def open_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = open_book("books/frankenstein.txt")
    print(count_words(book))
    print(count_characters(book))
    
main()