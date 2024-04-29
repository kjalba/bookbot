def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_counts = get_num_letters(text)
    letters_sorted_list = letters_count_to_sorted_list(letters_counts)
    print(f"{letters_counts}")
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for item in letters_sorted_list:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item['letter']}' character was found {item['count']} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def letters_count_to_sorted_list(letters_counts):
    sorted_list = []
    for c in letters_counts:
        sorted_list.append({"letter": c, "count": letters_counts[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_num_letters(text):
    counts = {}
    for letter in text:
        counts[letter.lower()] = counts.get(letter.lower(), 0) + 1
    return counts

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()