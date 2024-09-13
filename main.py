#!/usr/bin/env python3

"""
Bookbot is a simple command-line program that reads text
from a file and generates a report about the text.
"""


def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()

    words = file_contents.split()

    print("\n\n--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the text.")

    character_count_dict = character_count(file_contents)
    for character in sorted(character_count_dict.keys()):
        if character == '\n':
            print("The 'newline' character was found", end=' ')
        else:
            print(f"The '{character}' character was found", end=' ')
        print(f"{character_count_dict.get(character)} times")


def character_count(text):
    """returns character count of text
    :param text: str
    :return: int
    """
    character_count = dict()
    for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count


if __name__ == "__main__":
    main()
