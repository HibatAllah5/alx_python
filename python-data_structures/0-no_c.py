#Function that removes all characters c and C from a string.
def no_c(my_string):
    for letters in my_string:
        if 'C, c' in letters:
            print(my_string.translate({ord (i): None for i in 'C, c'}))
    return my_string
