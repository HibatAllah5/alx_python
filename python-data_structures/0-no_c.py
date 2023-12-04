#Function that removes all characters c and C from a string.
def no_c(my_string):
    for letters in my_string:
        print(my_string.translate({no_c(letters): None for letters in 'Cc'}))
    return my_string
