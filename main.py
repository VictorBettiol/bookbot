def sort_on(dict):
    return dict["num"]

def main():
    file_path = "books/frankenstein.txt"
    dict = {}
    list_of_dicts = []

    with open(file_path) as f:
        file_contents = f.read()
        lowered_words = file_contents.lower().split()

    for word in lowered_words:
        for letter in word:
            if letter not in dict and letter.isalpha():
                dict[letter] = 1
            elif letter in dict:
                dict[letter] += 1
    
    print(f"--- Begin report of {file_path} ---")
    print(f"{len(lowered_words)} words found in the document")

    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        list_of_dicts.append(new_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    for dict in list_of_dicts:
        print(f"The '{dict["char"]}' character was found {dict["num"]} times")
    
    print("--- End report ---")
    
main()