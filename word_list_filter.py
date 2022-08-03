def is_in_alphabet(x):
    return x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÜÖÄẞ-/;."


if __name__ == "__main__":
    with open("word_list.txt", 'r') as file:
        word_list = list(map(lambda x: x.strip(), file.readlines()))
    print(word_list)
    print(f"Up to now {len(word_list)} words.")
    for filename in ["new_words.txt"]:
        with open(filename, 'r') as file:
            for line in file.readlines():
                word = line.strip().replace('ß', 'ẞ').upper()
                if (len(word) == 5 and
                        False not in map(is_in_alphabet, word) and
                        word not in word_list):
                    answer = input(f"Add „{word}“ [y/N]?")
                    if answer.startswith("y"):
                        word_list.append(word)
    print(word_list)
    with open("word_list.txt", 'w') as file:
        file.write("\n".join(sorted(word_list)))
    print(len(word_list))
