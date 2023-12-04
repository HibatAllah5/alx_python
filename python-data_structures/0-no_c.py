#Function that removes all characters c and C from a string.
def no_c(my_string):
    for letters in my_string:
        if letters != 'C, c':
            print(my_string)
        else:
            print(my_string.translate({no_c(letters): None for letters in 'C, c'}))
    return my_string
