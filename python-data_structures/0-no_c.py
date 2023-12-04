#Function that removes all characters c and C from a string.
def no_c(my_string):
    new_string = " "
    for letters in new_string:
        if letters != "c" or letters != "C":
            new_string += letters
    return new_string
