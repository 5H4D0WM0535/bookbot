def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    wc = word_count(text)
    dic = letter_count(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document\n") 
    for let in dic:
        print(f"The '{let}' character was found {dic[let]} times")
    print("--- End report ---")


def get_text(book):
    with open(book) as f:
        text = f.read()
    return text


def word_count(text):
    return len(text.split())


def letter_count(text):
    dic = {}
    for let in text.lower():
        if let.isalpha():
            if let in dic:
                dic[let] += 1
            else:
                dic[let] = 1
    return dic


main()
