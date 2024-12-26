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