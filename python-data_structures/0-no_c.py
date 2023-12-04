#Function that removes all characters c and C from a string.
def no_c(my_string):
    word = (" ")
    new_word = no_c(word)
    for letters in word:
        if letters != "c" and letters != "C":
            new_word += letters
    return new_word       
