#!/usr/bin/env python3

# Created by: Hertz
# Created on: June 7nd, 2022.
# This program asks the user to enter a string and splits it up into
#  words and displays it to the user.


# The program function parse the sentence entered and returns it to the user
def string_parser(sentence):
    sentence_list = sentence.split(" ")
    return sentence_list


def main():
    # Explanation to the user
    print("This program ask the user for a sentence and ")
    print("display each word per line.")
    print("")

    # creates an empty list
    list_of_w = []

    # gets user input
    user_sentence = input("Enter a string: ")
    print("")
    list_of_w.append(user_sentence)

    # calls function
    word_string = string_parser(user_sentence)

    print("Words in your sentence are with no space :")
    print("")

    for w_string in word_string:

        # displaying the string parse to user
        print(w_string)


if __name__ == "__main__":
    main()
