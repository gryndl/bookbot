def main():
    book_path = "books/frankenstein.txt" #location of book/text
    text = get_book_text(book_path) #get text using get_book_text_function and assign it to {text}
    num_words = get_num_words(text) #get word count using get_num_words function and assign it to {num_words}
    chars_dict = get_chars_dict(text) #get letter count and assign it to dictionary chars_dict
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict) #sort chars_dict by num
    
    print(f"--- Begin report of {book_path} ---\n{num_words} words found in the document\n\n")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_num_words(text): #gets total number of words in text and return value to main()
    words = text.split()
    return len(words)

def sort_on(d): #sets to sort by "num" field
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict): #creates sorted list of dictionaries from chars_dict dictionary
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text): #counts characters in text
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


#def get_book_text(path):    
#    with open(path) as f: #open text into f
#        return f.read() #return text to main()

#def num_words(text):
#    words = len(text.split()) #count words in text
#    return words #return count to main()

#def count_letters(text):
#    my_text = text
#    lowered_string = my_text.lower()
#    list1=list(lowered_string)
#    lcDict= {}
#    for l in lowered_string:
#        if l in lcDict:
#            lcDict[l] +=1
#        else:
#            lcDict[l]= 1
#    return lcDict

#def sort_on(letters):
#    print(letters)

#def report(book_path, words, listLetters):
#    print(f"--- Begin report of {book_path} ---\n{words} words found in the document\n\n{listLetters}")

main()