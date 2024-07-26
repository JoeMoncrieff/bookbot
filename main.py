# Returns the total amount of words in a given string
def count_words(book):
    #Inefficient soln? (space)
    return(len(book.split(" ")))

#Takes a string and returns a dict of characters and how many times they appeared
def count_characters(book):
    #Data cleaning
    book = book.lower()
    output_dict = {}
    #analysis
    for c in book:
        output_dict[c] = output_dict.get(c,0) + 1
    return output_dict

#Opens a book from a specified path and returns it as a string
def open_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

#Dictionary sorter helper
def s_d_h(dictionary):
    return dictionary["qty"]

#Sorts a dictionary and returns a list in descending order
def sort_dictionary(input_dict):
    dict_list = []
    for key in input_dict:
        dict_list.append({"name":key, "qty":input_dict[key]})
    
    dict_list.sort(reverse=True, key=s_d_h)
    return dict_list

#Returns a formatted report analysing a given book/string
def get_report(path,book):
    return_string = ""
    dictionary = count_characters(book)
    num_words = count_words(book)
    dict_list = sort_dictionary(dictionary)
    
    return_string += f"--- Begin report of {path} ---\n"
    return_string += f"{num_words} words found in the document\n\n\n"
    for item in dict_list:
        if item["name"].isalpha():
            return_string += f"The \'{item['name']}\' character was found {item['qty']} times\n"
    return_string += "\n--- End Report ---"
    return return_string



def main():
    path = "books/frankenstein.txt"
    book = open_book(path)
    print(count_words(book))
    print(count_characters(book))
    print(get_report(path, book))
    
main()