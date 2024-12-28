# Hangman game developed with Python

import random

words = ("apple", "orange", "banana", "Coconut", "Pineapple")

#dictionary of key:()
hangman_art = {0: ("  ",
                   "  ",
                   "  "),

               1: (" o ",
                   "   ",
                   "   "),

                2: (" o ",
                   " | ",
                   "  "),

                3: (" o ",
                   " /| ",
                   "  "),

                4: (" o ",
                   " /|\\ ",
                   "  "),

                5: (" o ",
                   " /|\\ ",
                   " / "),

                6: (" o ",
                   " /|\\ ",
                   " / \\"),
                   }

for line in hangman_art[3]:
    print(line)

def display_man(wrong_guesses):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guesses_letters = set()
    is_running = True

    







    


if __name__ == "__main__":
    main()
