def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text)
    new_chars_dict = convert_dict_to_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for item in new_chars_dict:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(words):
    word_list = words.split()
    word_count = len(word_list)
    return word_count

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    dict_list = []
    for i in dict:
        if i.isalpha():
            dict_list.append({"char":i,"num":dict[i]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


main()