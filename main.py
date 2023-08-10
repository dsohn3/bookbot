def main():
    book_path = "github.com/dsohn3/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    
    ##Text Count
    num_words = text_count(text)

    ##Letter Count
    letter_num = letter_dict(text)

    #Print Report
    print("Frankenstein Report Start")
    print(f"Frankenstein has {num_words} words")
    dict_list = list(letter_num.items())
    dict_list.sort()
    print(dict_list)
    print("Frankenstein Report End")
    
def text_count(text):
    count = text.split()
    return len(count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def letter_dict(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

main()