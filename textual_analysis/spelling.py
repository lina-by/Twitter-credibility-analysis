# This module can be used in French
from spellchecker import SpellChecker
import string


def spelling_average(text): # counts the correct words and returns their proportion in the sentence
    t = text.translate(str.maketrans('','',string.punctuation)) # remove the punctuation
    lw = t.split() # list of the words of t
    spell = SpellChecker(language = 'fr', distance = 1)
    n = len(lw)
    c = 0 # number of correct words
    for w in lw:
        if w == spell.correction(w):
            c += 1
    return c/n

def misspelling_average(text):
    return (1 - spelling_average(text))

if __name__ == "__main__":
    print(spelling_average("Non, non, mon cher amoure, je ne vous aimé pa")) # the program does not return that "aimé" and "pa" are misspelled
# it returns 0.9 whereas the sentence is obviously wrong --> not very satisfactory
# This is because we did not consider the context --> language model

# Using language model: jamspell (couldn't install)